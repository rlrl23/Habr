import React from 'react';
import withRouter from './withRouter';
import {useParams, } from 'react-router-dom'
import axios from "axios";

class ArticleDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: this.props.articles,
      comments: this.props.comments,
      categories: this.props.categories,
      authors: this.props.authors,
      article:{},
      my_comment: "",
      article_id: 1,
      parent:'',
    };
  }
componentDidMount() {
    axios
    .get("http://127.0.0.1:8000/articles/"+this.props.params.id)
      .then((response) => {
        const article = response.data;
        this.setState({ article: article });
      })
      .catch((error) => console.log(error));

    axios
      .get("http://127.0.0.1:8000/comments/")
      .then((response) => {
        const comments = response.data;
        this.setState({ comments: comments });
      })
      .catch((error) => console.log(error));}

    handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  handleSubmit(event) {
    this.props.write_comment(this.state.my_comment, this.state.article_id, this.state.parent);
  }

  set_like(to_user, to_comment, to_article, likes_count){
    this.props.like(to_user, to_comment, to_article);
    if (to_article){
    this.state.article.liked_article=likes_count+1;}
    else {
    window.location.reload(false);
    }}

  answer_comment(author, text, parent){
    var s = document.getElementById('comment_id');
    s.innerHTML = author+' : '+ text;
    document.getElementById('close_button').classList.remove('invisible');
    this.state.parent=parent;
  }

  close_answer(){
   var s = document.getElementById('comment_id');
    s.innerHTML = '';
    document.getElementById('close_button').classList.add('invisible');
    this.state.parent='';
  }

render(){
//let comments= this.state.article.comment_article;
//let comments_count= this.state.article.comment_article;
//let count=comments_count.length;
console.log('article', this.state.article);
//console.log('categories', this.state.categories);
//console.log('authors', this.state.authors);
//    console.log('this.props', this.props.params);
   let id = Number(this.props.params.id);
   this.state.article_id= id;
   console.log('this.state.article_id', this.state.article_id);
   let article = this.state.articles.filter((article) => article.id == id)[0];
//   this.state.article = article;
   let filtered_comments = this.state.comments.filter((comment) => comment.article == id);
    console.log('filtered_comments', filtered_comments);
    this.state.comments = filtered_comments;
console.log('article', this.state.article);
    return (
        <div>
            <h2>{this.state.article.title}</h2>
            <span className="badge text-bg-secondary">{this.state.article.category}</span>
            <p className='mt-2' style={{textAlign: "justify"}}>{this.state.article['full_description']}</p>
            <div className="d-flex justify-content-between">
                <div>
                    <span>Автор: <strong>{this.state.article.author}</strong></span>
                    <span className='ms-4'>Опубликовано: {this.state.article['created_at']}</span>
                </div>
                <div>
                    <span className='text-danger'>{this.state.article.liked_article}</span>
                    {this.props.is_auth() ?
                    <i onClick={(to_user, to_comment, to_article, likes_count)=>{this.set_like(to_user=null, to_comment=null,to_article=this.state.article.id, likes_count=this.state.article.liked_article)}} className="ms-2 me-4 bi bi-heart-fill text-danger"></i>
                    :
                    (<i className="ms-2 me-4 bi bi-heart-fill text-danger"></i>)}

                    <span>{this.state.article.comment_article}</span>
                   <i className="ms-2 bi bi-chat-right-text"></i>
                </div>
            </div>
            <h4 className='mt-4 mb-3'>Комментарии</h4>
            <div>
                {this.state.comments.map((comment) =>
                 <div className="card mb-3">
            <div className="card-body">
                <div>
                    <strong>{comment.user}</strong>
                    <span className='mx-2'>{comment['created_at']}</span>
                    <span className='text-danger'>{comment.liked_comment}</span>
                    {this.props.is_auth() ?
                    <i onClick={(to_user, to_comment, to_article, likes_count)=>{this.set_like(to_user=null, to_comment=comment.id, to_article=null, likes_count=comment.liked_comment)}} className="ms-2 me-4 bi bi-heart-fill text-danger"></i>
                    :
                    <i className="ms-2 me-4 bi bi-heart-fill text-danger"></i>}
                    {this.props.is_auth()&&
                    <span onClick={(author, text, parent)=>{this.answer_comment(author=comment.user, text=comment.text, parent=comment.id ) }} className="badge text-bg-secondary float-end">Ответить</span>
                    }
                    <div>
                        {comment.text}
                    </div>
                </div>
            </div>
        </div>)}


{this.props.is_auth()&&
<form className="mt-4 mb-3" onSubmit={(event) => this.handleSubmit(event)}>
  <div className="row g-3 mb-3">
    <div className="col-5">
     <strong  >Прокомментировать</strong>
     <div >
     <button id='close_button' onClick={()=>{this.close_answer()}} type="button" class="btn-close float-end invisible" aria-label="Close"></button>
     <p id="comment_id"></p>
     </div>
      <textarea type="text" name="my_comment" className="form-control"
        value={this.state.my_comment}
        placeholder="" onChange={(event) => this.handleChange(event)}> </textarea>
    </div>
  </div>
  <input type="submit" value="Отправить" className='btn btn-primary' />

</form>}

            </div>
        </div>
    )
}}
export default withRouter(ArticleDetail)