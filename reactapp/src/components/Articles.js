import React from 'react'
import {useParams} from 'react-router-dom'
import {Link} from 'react-router-dom'
import Categories from "./Categories";

const ArticleItem = ({article, categories, authors}) => {
    let author = authors.filter((author) => author.id == article.author)[0];
    const category = categories.filter((category) => category['id'] === article['category'])[0];
    return (
        <div style={{width: 550}}>
            <div className="card">
                <div className="card-header">
                    <span className="badge text-bg-secondary">{category['name']}</span><br/>
                </div>
                <div className="card-body overflow-auto" style={{height: 200}}>
                    <h5 className="card-title"><Link className='title' to={`/article/${article.id}`}> {article.title}</Link></h5>
                    <p className="card-text">
                        {article['short_description']}
                    </p>
                </div>
                <div className="card-footer text-body-secondary d-flex justify-content-between">
                    <div>{article['created_at']} <strong>{author.username}</strong></div>
                    <div>
                        <span className='text-danger'>4</span>
                        <i className="ms-2 me-4 bi bi-heart-fill text-danger"></i>
                        <span>5</span>
                        <i className="ms-2 bi bi-chat-right-text"></i>
                    </div>
                </div>
            </div>
        </div>
    )
}

const ArticleList = ({articles, categories, authors}) => {
    let {category_slug} = useParams();
    if (category_slug) {
        let category = categories.filter((category) => category.slug == category_slug)[0];
        let articles_by_cat = articles.filter((article) => article.category == category.id);

        articles = articles_by_cat;
    }
    return (
        <div>
            <Categories categories={categories}/>
            <div className='mt-4 d-flex flex-wrap justify-content-between'>
                {articles.map((article) => <ArticleItem article={article} categories={categories} authors={authors}/>)}
            </div>
        </div>
    )

}
export default ArticleList