import { Link } from "react-router-dom"

const CategoryItem = ({ category }) => {
    return (
        <div class="btn1">
            <Link to={`/${category.slug}`}>
                <p class="p1">{category.name}</p>
            </Link>
        </div>
    )
}

const Categories = ({ categories }) => {
    return (

        <button class="button">
            {categories.map((category) => <CategoryItem category={category} />)}
        </button>

    )
}

export default Categories