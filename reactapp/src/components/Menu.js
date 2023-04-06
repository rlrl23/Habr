import { Link } from 'react-router-dom'

const CategoryItem = ({category}) => {
    return (
<li> <Link to={`/${category.slug}`}>{category.name}</Link></li>
)}

const Menu = ({categories}) => {
    return (
        <header>
            <div class="container">
                <a href="/" class="logo">Okay Habr</a>
                <nav>
                    <ul class='nav'>
                        <li><a href="/">Главная</a></li>
{categories.map((category)=> <CategoryItem category={category}/> )}
                        <li><a href="">Личный кабинет</a></li>
                    </ul>
                </nav>
            </div>
        </header>
    )
}

export default Menu