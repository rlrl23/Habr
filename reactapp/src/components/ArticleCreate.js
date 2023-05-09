import $ from 'jquery'

function createArticle(event) {
    event.preventDefault()
    if (event.target.name === 'publish') {
        console.log($('#article_create_form').serializeArray())
    }
}

const ArticleCreate = ({categories}) => {
    return (
        <div>
            <h2>Создание статьи</h2>
            <form id='article_create_form'>
                <div className="row g-3 mb-3">
                    <div className="col-5">
                        <label htmlFor="title" className="form-label">Название</label>
                        <input name='title' type="text" className="form-control" id="title"/>
                    </div>
                    <div className="col-3">
                        <label htmlFor="category" className="form-label">Категория</label>
                        <select name='category' className="form-control" id="category">
                            {categories.map((category) => <option value={category.id}>{category.name}</option>)}
                        </select>
                    </div>
                </div>
                <div className="mb-3">
                    <label htmlFor="short_description" className="form-label">Краткое описание</label>
                    <textarea name='short_description' className="form-control" id="short_description"
                              rows="3"></textarea>
                </div>
                <div className="mb-3">
                    <label htmlFor="full_description" className="form-label">Полный текст</label>
                    <textarea name='full_description' className="form-control" id="full_description"
                              rows="5"></textarea>
                </div>
                <button name="draft" onClick={createArticle} className='btn btn-primary me-2' type='submit'>
                    Сохранить черновик
                </button>
                <button name="publish" onClick={createArticle} className='btn btn-primary' type='submit'>
                    Опубликовать
                </button>
            </form>
        </div>
    )
}

export default ArticleCreate