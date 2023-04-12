import {BrowserRouter, Link} from "react-router-dom";

const Header = () => {
    return (
        <BrowserRouter>
            <div id='my_header'
                 className='bg-primary w-100 d-flex py-2 px-4 align-items-center justify-content-between'>
                <Link to='/'>
                    <div className='d-flex text-light'>
                        <div><i className="bi bi-braces"></i></div>
                        <div className='ms-2' id='habr_title'><strong>Habr</strong></div>
                    </div>
                </Link>
                <div className='d-flex'>
                    <div className='text-light' ><i className="bi bi-bell"></i></div>
                    <div className='text-light ms-4'><i className="bi bi-info-circle"></i></div>
                    <div className='text-light ms-4'><i className="bi bi-person"></i></div>
                    <div className='text-light ms-4'><i className="bi bi-box-arrow-left"></i></div>
                </div>
            </div>
        </BrowserRouter>
    )
}
export default Header