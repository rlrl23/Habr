
const today = new Date();
const year=today.getFullYear()

const Footer = () => {
    return (<footer>
        <div class="waves">
            <div class="wave" id="wave1"></div>
        </div>
        <ul class="menu">
            <li><a href="/">Главная</a></li>
            <li><a href="#">Помощь</a></li>
        </ul>
        <p>©{year} Okay Habr | Все права защищены</p>
    </footer>
    )
}


export default Footer