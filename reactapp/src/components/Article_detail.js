import React from 'react'
import { useParams } from 'react-router-dom'


const ArticleDetail = ({ articles }) => {
let { id } = useParams();
console.log('id', id);

let article = articles.filter((article)=> article.id==id)[0];

    return (
    <ul>
    <li> {article.title}
      <p> {article.short_description} </p>
      <li> {article.author} </li>
      <li> {article.created_at} </li>
 </li>
   </ul>
    )
}
export default ArticleDetail