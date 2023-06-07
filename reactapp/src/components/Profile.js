import {Link} from "react-router-dom";
import React from "react";
import axios from "axios";
import Cookies from "universal-cookie";

class Profile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            profile: props.profile
        }
    }

    componentDidMount() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const headers = {'Authorization': 'Token ' + token}
        axios
            .get("http://127.0.0.1:8000/profile/", {headers: headers})
            .then((response) => {
                const profile = response.data
                this.setState({profile: profile});
            })
            .catch((error) => console.log(error));
    }

    render() {
        return (
            <div>
                <h2>Личный кабинет</h2>
                <form className="mt-4 mb-3">
                    <div className="row g-3 mb-3">
                        <div className="col-5">
                            <label htmlFor="username" className="form-label"><strong>Имя пользователя</strong></label>
                            <input defaultValue={this.state.profile.username} type="text" className="form-control" id="username"/>
                        </div>
                    </div>
                    <div className="row g-3 mb-3">
                        <div className="col-4">
                            <label htmlFor="firstname" className="form-label"><strong>Имя</strong></label>
                            <input defaultValue={this.state.profile.firstname} id='firstname' type="text" className="form-control"/>
                        </div>
                        <div className="col-4">
                            <label htmlFor="lastname" className="form-label"><strong>Фамилия</strong></label>
                            <input defaultValue={this.state.profile.lastname} id='lastname' type="text" className="form-control"/>
                        </div>
                        <div className="col-4">
                            <label htmlFor="birth_date" className="form-label"><strong>Дата рождения</strong></label>
                            <input id='birth_date' type="date" className="form-control"/>
                        </div>
                    </div>
                    <div className="row g-3 mb-3">
                        <div className="col-12">
                            <label htmlFor="description" className="form-label"><strong>О себе</strong></label>
                            <textarea defaultValue={this.state.profile.description} className="form-control"
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