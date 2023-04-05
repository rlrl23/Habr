import React from 'react'

const ArticleItem = ({article}) => {
    return (
      <li> {article.title}
      <p> {article.short_description} </p>
 </li>
//       <li> {article.short_description} </li>
//       <li> {article.author} </li>
//       <li> {article.created_at} </li>
    )
}

const ArticleList = ({ articles }) => {
    return (<ul>
    <li> Список статей </li>

    {articles.map((article) => <ArticleItem article={article} />)}
   </ul>
    )
}
export default ArticleList