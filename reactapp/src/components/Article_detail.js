import React from 'react'
import {useParams} from 'react-router-dom'

const CommentItem = ({comment, authors}) => {
    const author = authors.filter((author) => author.id === comment.user)[0];
    return (
        <div className="card mb-3">
            <div className="card-body">
                <div>
                    <strong>{author.username}</strong>
                    <span className='mx-2'>{comment['created_at']}</span>
                    <span className='text-danger'>1</span>
                    <i className="ms-2 me-4 bi bi-heart-fill text-danger"></i>
                    <div>
                        {comment.text}
                    </div>
                </div>
            </div>
        </div>
    )
}

const ArticleDetail = ({articles, comments, categories, authors}) => {
    let {id} = useParams();
    console.log('id', id);
    console.log('comments', comments);
    let article = articles.filter((article) => article.id == id)[0];
    let author = authors.filter((author) => author.id == article.author)[0];
    let filtered_comments = comments.filter((comment) => comment.article == id);
    console.log('filtered_comments', filtered_comments);
    comments = filtered_comments;
    const category = categories.filter((category) => category['id'] === article['category'])[0];
    return (
        <div>
            <h2>{article.title}</h2>
            <span className="badge text-bg-secondary">{category['name']}</span>
            <p className='mt-2' style={{textAlign: "justify"}}>{article['full_description']}</p>
            <div className="d-flex justify-content-between">
                <div>
                    <span>Автор: <strong>{author.username}</strong></span>
                    <span className='ms-4'>Опубликовано: {article['created_at']}</span>
                </div>
                <div>
                    <span className='text-danger'>4</span>
                    <i className="ms-2 me-4 bi bi-heart-fill text-danger"></i>
                    <span>5</span>
                    <i className="ms-2 bi bi-chat-right-text"></i>
                </div>
            </div>
            <h4 className='mt-4 mb-3'>Комментарии</h4>
            <div>
                {comments.map((comment) => <CommentItem comment={comment} authors={authors}/>)}
            </div>
        </div>
    )
}
export default ArticleDetail