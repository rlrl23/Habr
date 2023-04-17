import logo from './logo.svg';
import './App.css';
import React from 'react';
import ArticleList from './components/Articles.js';
import axios from 'axios';
import Menu from './components/Menu';
import Footer from './components/Footer';
import ArticleDetail from './components/Article_detail.js';
import {BrowserRouter, Route, Routes, Switch} from 'react-router-dom';
import Header from "./components/Header";
import Profile from "./components/Profile";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'articles': [],
            'categories': [],
            'comments': [],
            'authors': []
        }
    }

    componentDidMount() {

        axios.get('http://127.0.0.1:8000/articles/').then(
            response => {
                const articles = response.data
                this.setState(
                    {'articles': articles}
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/categories/').then(
            response => {
                const categories = response.data
                this.setState(
                    {'categories': categories}
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/authors/').then(
            response => {
                const authors = response.data
                this.setState(
                    {'authors': authors}
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/comments/').then(
            response => {
                const comments = response.data
                this.setState(
                    {'comments': comments}
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/likes/').then(
            response => {
                const likes = response.data
                this.setState(
                    {'likes': likes}
                )
            }
        ).catch(error => console.log(error))


    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <Header></Header>
                    <div className='body-container mx-auto pt-3'>
                        <Routes>
                            <Route exact path='/' element={<ArticleList articles={this.state.articles}
                                                                        categories={this.state.categories}
                                                                        authors={this.state.authors}/>}/>
                            <Route path='/:category_slug' element={<ArticleList articles={this.state.articles}
                                                                                categories={this.state.categories}
                                                                                authors={this.state.authors}/>}/>
                            <Route path='/article/:id' element={<ArticleDetail articles={this.state.articles}
                                                                               comments={this.state.comments}
                                                                               categories={this.state.categories}
                                                                               authors={this.state.authors}/>}/>
                            <Route path='/profile' element={<Profile/>}/>
                        </Routes>
                        <Footer/>
                    </div>
                </BrowserRouter>
            </div>
        )
    }
}


export default App;

