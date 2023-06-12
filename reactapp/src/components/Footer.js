import './Styles.css'

const today = new Date();
const year = today.getFullYear()

const Footer = () => {
    return (
        <div class="footer fixed-bottom">
            <div class="footer_bottom_item">
                <p>© {year} Okay Habr</p>
                <p>Группа GBdev_1_OKAYGEEK | Все права защищены</p>
            </div>
        </div>
    )
}
export default Footer
