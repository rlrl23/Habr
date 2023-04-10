import React from 'react'
import { useParams } from 'react-router-dom'
import { Link } from 'react-router-dom'

const ArticleItem = ({article}) => {
    return (
      <li><Link to={`/article/${article.id}`}> {article.title}</Link>
      <p> {article.short_description} </p>
 </li>
//       <li> {article.short_description} </li>
//       <li> {article.author} </li>
//       <li> {article.created_at} </li>
    )
}

const ArticleList = ({ articles, categories }) => {
let { category_slug } = useParams();
console.log('category', category_slug);
if (category_slug){
let category=categories.filter((category)=> category.slug==category_slug)[0];
console.log('category', category.name);
let articles_by_cat = articles.filter((article)=> article.category==category.name);
articles=articles_by_cat;
}
    return (
    <ul>
    <li> Список статей </li>
    {articles.map((article) => <ArticleItem article={article} />)}
   </ul>
    )
}
export default ArticleList