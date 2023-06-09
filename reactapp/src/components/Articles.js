import React from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';
import Categories from "./Categories";

const ArticleItem = ({ article}) => {

    return (
        <div className="mt-4" style={{ width: 550 }}>
            <div className="card card1">
                <div className="card-header">
                    <span className="badge text-bg-secondary">{article.category.name}</span><br />
                </div>
                <div className="card-body overflow-auto" style={{ height: 200 }}>
                    <h5 className="card-title1"><Link className='title' to={`/article/${article.id}`}> {article.title}</Link></h5>
                    <p className="card-text">
                        {article['short_description']}
                    </p>
                </div>
                <div className="card-footer text-body-secondary d-flex justify-content-between">
                    <div>{article['created_at']} <strong className="author1">{article.author}</strong></div>
                    <div>
                        <span className='text-danger'>{article.liked_article}</span>
                        <i className="ms-2 me-4 bi bi-heart-fill text-danger"></i>
                        <span>{article.comment_article}</span>
                        <i className="ms-2 bi bi-chat-right-text"></i>
                    </div>
                </div>
            </div>
        </div>
    )
}

const ArticleList = ({ articles, categories }) => {

    let { category_slug } = useParams();
    if (category_slug) {
        let articles_by_cat = articles.filter((article) => article.category.slug == category_slug);
        articles = articles_by_cat;
    }
    return (
        <div>
            <Categories categories={categories} />
            <div className='mt-2 d-flex flex-wrap justify-content-between'>
                {articles.map((article) => <ArticleItem article={article}/>)}
            </div>
        </div>
    )

}
export default ArticleList