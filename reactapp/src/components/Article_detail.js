import React from 'react'
import { useParams } from 'react-router-dom'

const СommentItem = ({comment, authors}) => {
let author=authors.filter((author)=> author.id==comment.user)[0];
    return (
     <div>
    <p>{comment.text}</p>
     <div>{author.username}  {comment.created_at}</div>
     </div>)
}

const ArticleDetail = ({ articles, comments, categories, authors }) => {
let { id } = useParams();
console.log('id', id);
console.log('comments',comments);
let article = articles.filter((article)=> article.id==id)[0];
let author=authors.filter((author)=> author.id==article.author)[0];
let filtered_comments=comments.filter((comment)=> comment.article==id);
console.log('filtered_comments', filtered_comments);
comments=filtered_comments;
    return (
    <div>
    <h2> {article.title}</h2>
    <p>{article.full_description}</p>
    <div> {author.username} </div>
    <div> {article.created_at} </div>
    <h2> Комментарии </h2>
<div class='comment_container'>
    {comments.map((comment) => <СommentItem comment={comment} authors={authors} />)}
 </div>
  </div>
    )
}
export default ArticleDetail