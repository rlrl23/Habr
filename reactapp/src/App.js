import logo from './logo.svg';
import './App.css';
import React from 'react';
import ArticleList from './components/Articles.js';
import axios from 'axios';
import Menu from './components/Menu';
import Footer from './components/Footer';
import ArticleDetail from './components/Article_detail.js';
import { BrowserRouter, Route, Routes, Switch } from 'react-router-dom';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'articles': [],
      'categories':[{'name':'Дизайн', 'slug':'disign'},{'name':'Маркетинг', 'slug':'marketing'},{'name':'Web разработка', 'slug':'web_dev'},],
      'comments':[{'id':1, 'article_id':1, 'text':'Гневный комментарий', 'author_id':1}, {'id':2, 'article_id':1, 'text':'Хороший комментарий', 'author_id':1}, {'id':3, 'article_id':2, 'text':'Гневный комментарий', 'author_id':1}],
      'users':[]
    }
  }
  componentDidMount() {

    axios.get('http://127.0.0.1:8000/articles/').then(
      response => {
        const articles = response.data
        this.setState(
          { 'articles': articles }
        )
      }
    ).catch(error => console.log(error))
  }

  render() {
    return (

      <div class='main'>

      <BrowserRouter>
              <Menu categories={this.state.categories}/>
      <Routes>
        <Route exact path='/' element={ <ArticleList articles={this.state.articles} />} />
        <Route path='/:category_slug' element={<ArticleList articles={this.state.articles} categories={this.state.categories} />} />
        <Route path='/article/:id' element={<ArticleDetail articles={this.state.articles} comments={this.state.comments} />} />
        </Routes>
                <Footer />
         </BrowserRouter>
      </div>
    )
  }
}


export default App;

