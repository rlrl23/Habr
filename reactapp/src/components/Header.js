import { Link, NavLink, useNavigate } from "react-router-dom";
import React from 'react';

class Header extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        };
    }
    render() {
        return (
            <div id='my_header'
                className='bg-primary w-100 d-flex py-2 px-4 align-items-center justify-content-between'>
                <NavLink to='/'>
                    <div className='d-flex text-light'>
                        <div><i className="bi bi-braces"></i></div>
                        <div className='ms-2' id='habr_title'><strong>Habr</strong></div>
                    </div>
                </NavLink>
                <div className='d-flex'>
                    <div className='text-light'><i className="bi bi-bell"></i></div>
                    <div className='text-light ms-4'><i className="bi bi-info-circle"></i></div>
                    {this.props.is_auth() ?
                        <div className='d-flex'>
                            <NavLink to='/profile'>
                                <div title={'Личный кабинет'} className='text-light ms-4'><i className="bi bi-person"></i></div>
                            </NavLink>
                            <button onClick={() => this.props.logout()}>  <i className="bi bi-box-arrow-right ms-4"></i></button>
                        </div> :
                        <div className='d-flex'>
                            <NavLink to='/register'>
                                <div className='text-light ms-4'><i className="bi bi-r-square"></i></div>
                            </NavLink>
                            <NavLink to='/login'>
                                <div className='text-light ms-4'><i className="bi bi-box-arrow-in-left"></i></div>
                            </NavLink>

                        </div>}

                </div>
            </div>
        )
    }
}

export default Header;