import React from 'react'
import { useParams } from 'react-router-dom'
import { Link } from 'react-router-dom'

const ArticleItem = ({article, categories, authors}) => {
let category=categories.filter((category)=> category.id==article.category)[0];
let author=authors.filter((author)=> author.id==article.author)[0];
    return (
    <div class='art_item'>
    <div class='title_container'>
     <Link class='title' to={`/article/${article.id}`}> {article.title}</Link>
      <div class='category'>{category.name}</div>
       </div>
      <p class='art_text'> {article.short_description} </p>
      <div>{article.created_at} {author.username}</div>
 </div>

    )
}

const ArticleList = ({ articles, categories, authors }) => {
let { category_slug } = useParams();
if (category_slug){
let category=categories.filter((category)=> category.slug==category_slug)[0];
let articles_by_cat = articles.filter((article)=> article.category==category.id);

articles=articles_by_cat;};
    return (
    <div class='art_container'>
    {articles.map((article) => <ArticleItem article={article} categories={categories} authors={authors} />)}
    </div>
    )

}
export default ArticleList