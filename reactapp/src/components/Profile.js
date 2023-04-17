const Profile = () => {
    return (
        <div>
            <h2>Личный кабинет</h2>
            <form className="mt-4 mb-3">
                <div className="row g-3 mb-3">
                    <div className="col-5">
                        <label htmlFor="username" className="form-label"><strong>Имя пользователя</strong></label>
                        <input type="text" className="form-control" id="username"/>
                    </div>
                </div>
                <div className="row g-3 mb-3">
                    <div className="col-4">
                        <label htmlFor="firstname" className="form-label"><strong>Имя</strong></label>
                        <input id='firstname' type="text" className="form-control"/>
                    </div>
                    <div className="col-4">
                        <label htmlFor="lastname" className="form-label"><strong>Фамилия</strong></label>
                        <input id='lastname' type="text" className="form-control"/>
                    </div>
                    <div className="col-4">
                        <label htmlFor="birth_date" className="form-label"><strong>Дата рождения</strong></label>
                        <input id='birth_date' type="date" className="form-control"/>
                    </div>
                </div>
                <div className="row g-3 mb-3">
                    <div className="col-12">
                        <label htmlFor="description" className="form-label"><strong>О себе</strong></label>
                        <textarea className="form-control" id="description"></textarea>
                    </div>
                </div>
                <button className='btn btn-primary' type='submit'>Сохранить</button>
            </form>
            <button className='btn btn-primary' type='button'>Написать статью</button>
        </div>
    )
}

export default Profile