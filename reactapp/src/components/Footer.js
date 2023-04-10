
const today = new Date();
const year=today.getFullYear()

const Footer = () => {
    return (<footer>
        <p>©{year} Okay Habr | Все права защищены</p>
    </footer>
    )
}
export default Footer