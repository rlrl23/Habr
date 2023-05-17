import React from "react";
import {Navigate} from "react-router-dom";

class ArticleCreate extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            title: '',
            category: '',
            short_description: '',
            full_description: '',
            is_draft: false,
            redirect: false,
            error: false
        }
    }

    handleChange = (event) => {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleCheckbox = (event) => {
        this.setState(
            {
                ['is_draft']: !(this.state.is_draft)
            }
        );
    }

    handleSubmit = async (event) => {
        event.preventDefault()
        const err = await this.props.create_article(this.state.title, this.state.category, this.state.short_description,
            this.state.full_description, this.state.is_draft)
        err === 1 ? this.setState({error: true}) : this.setState({redirect: true})
    }

    render() {
        let redirect = this.state.redirect
        let error = this.state.error
        return (
            <div>
                {error && <p>Внутрення ошибка сервера</p>}
                {redirect && (
                    <Navigate to="/" replace={true}/>
                )}
                <h2>Создание статьи</h2>
                <form onSubmit={this.handleSubmit} id='article_create_form'>
                    <div className="row g-3 mb-3">
                        <div className="col-5">
                            <label htmlFor="title" className="form-label">Название</label>
                            <input required onChange={this.handleChange} name='title' type="text"
                                   className="form-control" id="title"/>
                        </div>
                        <div className="col-3">
                            <label htmlFor="category" className="form-label">Категория</label>
                            <select required onChange={this.handleChange} name='category' className="form-control"
                                    id="category">
                                <option disabled selected></option>
                                {this.props.categories.map((category) => <option key={category.id}
                                                                                 value={category.id}>{category.name}</option>)}
                            </select>
                        </div>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="short_description" className="form-label">Краткое описание</label>
                        <textarea required onChange={this.handleChange} name='short_description'
                                  className="form-control" id="short_description"
                                  rows="3"></textarea>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="full_description" className="form-label">Полный текст</label>
                        <textarea required onChange={this.handleChange} name='full_description' className="form-control"
                                  id="full_description"
                                  rows="5"></textarea>
                    </div>
                    <div className="form-check mb-3">
                        <input checked={this.state.is_draft} onChange={this.handleCheckbox} id="is_draft"
                               name='is_draft' className="form-check-input" type="checkbox"/>
                        <label className="form-check-label" htmlFor="is_draft">
                            Черновик
                        </label>
                    </div>
                    <button className='btn btn-primary me-2' type='submit'>
                        Сохранить
                    </button>
                </form>
            </div>
        )
    }
}

export default ArticleCreate