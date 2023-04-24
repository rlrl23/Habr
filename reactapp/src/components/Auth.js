import React from "react";



class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      login: "",
      password: "",
    };
  }
  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  handleSubmit(event) {
    this.props.get_token(this.state.login, this.state.password);
    event.preventDefault();
    window.location.href = "/";
  }

  render() {
    return (
      <div>
        <h2>Введите данные</h2>
        <form className="mt-4 mb-3" onSubmit={(event) => this.handleSubmit(event)}>
          <div className="row g-3 mb-3">
            <div className="col-5">
              <label htmlFor="login" className="form-label"><strong>Nickname</strong></label>
              <input type="text" name="login" className="form-control"
                value={this.state.login}
                placeholder="login" onChange={(event) => this.handleChange(event)} />
            </div>
          </div>
          <div className="row g-3 mb-3">
            <div className="col-5">
              <label htmlFor="password" className="form-label"><strong>Password</strong></label>
              <input type="password" name="password" className="form-control"
                value={this.state.password}
                placeholder="password" onChange={(event) => this.handleChange(event)} />
            </div>
          </div>
          <input type="submit" value="Войти" className='btn btn-primary' />

        </form>
      </div>
    );
  }
}

export default LoginForm;
