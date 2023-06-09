import {Link} from "react-router-dom";
import React from "react";
import axios from "axios";
import Cookies from "universal-cookie";

class Profile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            first_name: '',
            last_name: '',
            description: '',
            date_of_birth: '',
            error: false,
            success: false
        }
    }

    load_profile() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const headers = {'Authorization': 'Token ' + token}
        axios
            .get("http://127.0.0.1:8000/profile/", {headers: headers})
            .then((response) => {
                const profile = response.data
                this.setState({username: profile.username});
                this.setState({first_name: profile.first_name});
                this.setState({last_name: profile.last_name});
                this.setState({description: profile.description});
                this.setState({date_of_birth: profile.date_of_birth});
            })
            .catch((error) => {
                console.log(error)
            });
    }

    componentDidMount() {
        this.load_profile()
    }

    handleChange = (event) => {
        this.setState({success: false});
        this.setState({error: false});
        this.setState(
            {
                [event.target.id]: event.target.value
            }
        );
    }

    handleSubmit = (event) => {
        event.preventDefault()
        const cookies = new Cookies()
        const token = cookies.get('token')
        const headers = {'Authorization': 'Token ' + token}
        axios
            .post("http://127.0.0.1:8000/profile/", this.state, {headers: headers})
            .then((response) => {
                this.setState({success: true});
                const profile = response.data
                this.setState({username: profile.username});
                this.setState({first_name: profile.first_name});
                this.setState({last_name: profile.last_name});
                this.setState({description: profile.description});
                this.setState({date_of_birth: profile.date_of_birth});
            })
            .catch((error) => {
                console.log(error)
                this.setState({error: true});
            });
    }

    render() {
        let success = this.state.success
        let error = this.state.error
        return (
            <div>
                {error && <div className="alert alert-danger" role="alert">
                    Внутренняя ошибка сервера. Изменения не применены
                </div>}
                {success && <div className="alert alert-success" role="alert">
                    Изменения применены
                </div>}
                <h2>Личный кабинет</h2>
                <form onSubmit={this.handleSubmit} className="mt-4 mb-3">
                    <div className="row g-3 mb-3">
                        <div className="col-5">
                            <label htmlFor="username" className="form-label"><strong>Имя пользователя</strong></label>
                            <input onChange={this.handleChange} defaultValue={this.state.username} type="text"
                                   className="form-control"
                                   id="username"/>
                        </div>
                    </div>
                    <div className="row g-3 mb-3">
                        <div className="col-4">
                            <label htmlFor="firstname" className="form-label"><strong>Имя</strong></label>
                            <input onChange={this.handleChange} defaultValue={this.state.first_name} id='first_name'
                                   type="text"
                                   className="form-control"/>
                        </div>
                        <div className="col-4">
                            <label htmlFor="lastname" className="form-label"><strong>Фамилия</strong></label>
                            <input onChange={this.handleChange} defaultValue={this.state.last_name} id='last_name'
                                   type="text"
                                   className="form-control"/>
                        </div>
                        <div className="col-4">
                            <label htmlFor="birth_date" className="form-label"><strong>Дата рождения</strong></label>
                            <input onChange={this.handleChange} id='date_of_birth' type="date"
                                   defaultValue={this.state.date_of_birth}
                                   className="form-control"/>
                        </div>
                    </div>
                    <div className="row g-3 mb-3">
                        <div className="col-12">
                            <label htmlFor="description" className="form-label"><strong>О себе</strong></label>
                            <textarea onChange={this.handleChange} defaultValue={this.state.description}
                                      className="form-control"
                                      id="description"></textarea>
                        </div>
                    </div>
                    <button className='btn btn-primary' type='submit'>Сохранить</button>
                </form>
                <Link to='/create_article'>
                    <button className='btn btn-primary' type='button'>Написать статью</button>
                </Link>
            </div>
        )
    }
}


export default Profile