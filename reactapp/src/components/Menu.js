import { Link } from "react-router-dom";

const CategoryItem = ({ category }) => {
  return (
    <div class="cat_item">
      {" "}
      <Link class="link" to={`/${category.slug}`}>
        {category.name}
      </Link>{" "}
    </div>
  );
};

const Menu = ({ categories }) => {
  return (
    <header>
      <div class="menu_line">
        <img
          class="logo"
          src="https://cdn4.iconfinder.com/data/icons/programming-line-style/32/Bracket_Code-1024.png"
        />
        <a href="/" class="name">
          Okay Habr
        </a>
        <a href="/" class="profile">
          login
        </a>
        <a href="#" class="help">
          <img
            class="logo"
            src="https://e7.pngegg.com/pngimages/114/375/png-clipart-white-and-blue-information-logo-information-sign-symbol-visitor-center-tourist-miscellaneous-blue.png"
          />
        </a>
        <a href="#" class="profile">
          <img
            class="logo"
            src="https://img2.freepng.ru/20180630/eae/kisspng-business-lissauer-eriks-dental-group-dentistry-i-5b37c6148893a5.3156102215303818445594.jpg"
          />
        </a>
        <button class="logout">
          <img
            class="logout"
            src="https://w7.pngwing.com/pngs/873/996/png-transparent-computer-icons-window-door-furniture-door-blue-angle-furniture.png"
          />
        </button>
      </div>
      <nav>
        <div class="cat_container">
          {categories.map((category) => (
            <CategoryItem category={category} />
          ))}
        </div>
      </nav>
    </header>
  );
};

export default Menu;
