import logo from "./logo.svg";
import "./App.css";
import React from "react";
import ArticleList from "./components/Articles.js";
import axios from "axios";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import ArticleDetail from "./components/Article_detail.js";
import {BrowserRouter, Route, Routes, Switch, Link, Navigate} from "react-router-dom";
import Header from "./components/Header";
import Profile from "./components/Profile";
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie";
import ArticleCreate from "./components/ArticleCreate";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            articles: [],
            categories: [],
            comments: [],
            likes: [],
            authors: [],
            token: "",
            id: "",
        };
    }

    get_token(username, password) {
        const data = {username: username, password: password};

        axios
            .post("http://127.0.0.1:8000/api-token-auth/", data)
            .then((response) => {
                console.log('response.data', response.data);
                this.set_token(response.data["token"], response.data['id']);
            })
            .catch((error) => alert("Неверный пароль или логин"));
    }

    set_token(token, id) {

        const cookies = new Cookies();
        cookies.set("token", token);
        cookies.set('id', id);
        this.setState({token: token, id: id}, () => this.load_data());
    }

    is_auth() {
        return !!this.state.token;
    }

    logout() {
        this.set_token("");
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({token: token}, () => this.load_data())
    }

    write_comment(text, article, parent_id = null) {
        const data = {
            text: text,
            user: 2,
//  this.state.id,
            article: article, parent_id: parent_id
        };
        axios
            .post("http://127.0.0.1:8000/comments/", data, {headers: this.get_headers()})
            .then((response) => {
                this.load_data();
            })
            .catch((error) => alert(error));
    }

    async create_article(title, category, short_description, full_description, is_draft) {
        if (!this.state.id) {
            console.log('Не обнаружен айди автора')
            return 1
        }
        const data = {
            title: title,
            category: Number(category),
            short_description: short_description,
            full_description: full_description,
            is_published: !is_draft,
            author: Number(this.state.id)
        }
        let err = 0
        try {
            await axios.post(`http://127.0.0.1:8000/articles/`, data, {headers: this.get_headers()});
            this.load_data();
        } catch (error) {
            console.log(error)
            err = 1
        }
        return err
    }

    load_data() {
        const headers = this.get_headers()

        axios
            .get("http://127.0.0.1:8000/list/articles", {headers: headers})
            .then((response) => {
                const articles = response.data;
                this.setState({articles: articles});
            })
            .catch((error) => console.log(error));

        axios
            .get("http://127.0.0.1:8000/categories/", {headers: headers})
            .then((response) => {
                const categories = response.data;
                this.setState({categories: categories});
            })
            .catch((error) => console.log(error));

        axios
            .get("http://127.0.0.1:8000/authors/", {headers: headers})
            .then((response) => {
                const authors = response.data;
                this.setState({authors: authors});
            })
            .catch((error) => console.log(error));

        axios
            .get("http://127.0.0.1:8000/comments/", {headers: headers})
            .then((response) => {
                const comments = response.data;
                this.setState({comments: comments});
            })
            .catch((error) => console.log(error));

        axios
            .get("http://127.0.0.1:8000/likes/", {headers: headers})
            .then((response) => {
                const likes = response.data;
                this.setState({likes: likes});
            })
            .catch((error) => console.log(error));
    }

    componentDidMount() {
        this.get_token_from_storage();
    }

    render() {
        console.log('this.state.token', this.state.token);
        console.log('I am', this.state.id);
        console.log('Headers', this.get_headers())
        return (
            <div>
                <BrowserRouter>
                    <Header is_auth={() => this.is_auth()} logout={() => this.logout()}></Header>
                    <div className="body-container mx-auto pt-3">
                        <Routes>
                            <Route
                                exact
                                path="/"
                                element={
                                    <ArticleList
                                        articles={this.state.articles}
                                        categories={this.state.categories}
                                    />
                                }
                            />
                            <Route
                                exact
                                path="/login"
                                element={
                                    <LoginForm
                                        get_token={(username, password) => this.get_token(username, password)}


                                    />
                                }
                            />


                            <Route
                                path="/:category_slug"
                                element={
                                    <ArticleList
                                        articles={this.state.articles}
                                        categories={this.state.categories}
                                        authors={this.state.authors}
                                    />
                                }
                            />
                            <Route
                                path="/article/:id"
                                element={
                                    <ArticleDetail
                                        articles={this.state.articles}
                                        comments={this.state.comments}
                                        is_auth={() => this.is_auth()}
                                        write_comment={(text, article, parent_id) => this.write_comment(text, article, parent_id)}
                                    />
                                }
                            />
                            <Route path="/profile" element={<Profile/>}/>
                            {this.is_auth() ?
                                <Route path="/create_article"
                                       element={<ArticleCreate
                                           categories={this.state.categories}
                                           create_article={(title, category, short_description, full_description,
                                                            is_draft) => this.create_article(title, category,
                                               short_description, full_description, is_draft)}/>}/>
                                : null}
                        </Routes>
                        <Footer/>
                    </div>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
