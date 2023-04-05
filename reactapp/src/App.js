import logo from './logo.svg';
import './App.css';
import React from 'react';
import ArticleList from './components/Articles.js';
import axios from 'axios';
import Menu from './components/Menu';
import Footer from './components/Footer';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'articles': []
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
      <div>
        <Menu />
        <ArticleList articles={this.state.articles} />
        <Footer />
      </div>
    )
  }
}


export default App;

