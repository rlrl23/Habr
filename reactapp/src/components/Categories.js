import {Link} from "react-router-dom";

const CategoryItem = ({category}) => {
    return (
        <Link to={`/${category.slug}`}>
            <div className='btn btn-primary'>
                <strong>{category.name}</strong>
            </div>
        </Link>
    )
}

const Categories = ({categories}) => {
    return (
        <div className='d-flex justify-content-start' style={{gap: 20}}>
            {categories.map((category) => <CategoryItem category={category}/>)}
        </div>
    )
}

export default Categories