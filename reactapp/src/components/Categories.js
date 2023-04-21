import {Link} from "react-router-dom";

const CategoryItem = ({category}) => {
    return (
        <Link to={`/${category.slug}`}>
        <div className='btn btn-primary category-item flex-fill'>
             <strong>{category.name}</strong>
        </div>
        </Link>
    )
}

const Categories = ({categories}) => {
    return (
        <div className='d-flex justify-content-between align-items-center' style={{gap: 20}}>
            {categories.map((category) => <CategoryItem category={category}/>)}
        </div>
    )
}

export default Categories