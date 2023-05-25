import axios from "axios";
import React from "react";

class RegisterUserForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: "",
        };
    };

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value,
        });
    }

    handleSubmit(event) {
        // const headers = this.props.get_headers()
        const data = { username: this.state.username, password: this.state.password }
        axios.post("http://127.0.0.1:8000/authors/", data)
            .then((response) => {
                console.log(this.state.username, this.state.password)
            })
            .catch((error) => console.log(error));
        event.preventDefault();

    }

    render() {
        return (
            <div>
                <h2>Введите данные для регистрации</h2>
                <form className="mt-4 mb-3" onSubmit={(event) => this.handleSubmit(event)}>
                    <div className="row g-3 mb-3">
                        <div className="col-5">
                            <label htmlFor="login" className="form-label"><strong>Имя пользователя</strong></label>
                            <input type="text" name="username" className="form-control"
                                value={this.state.login}
                                placeholder="username" onChange={(event) => this.handleChange(event)} />
                        </div>
                    </div>
                    <div className="row g-3 mb-3">
                        <div className="col-5">
                            <label htmlFor="password" className="form-label"><strong>Пароль</strong></label>
                            <input type="password" name="password" className="form-control"
                                value={this.state.password}
                                placeholder="password" onChange={(event) => this.handleChange(event)} />
                        </div>
                    </div>
                    <input type="submit" value="Зарегистрироваться" className='btn btn-primary' />

                </form>
            </div>
        )
    }
}

export default RegisterUserForm;