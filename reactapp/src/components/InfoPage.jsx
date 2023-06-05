import React from 'react';

const InfoPage = () => {
    return (
        <div>
            <h3>Добро пожаловать на портал Habr!</h3>
            <p>Здесь вы можете читать статьи, посвящённые IT и другим сферам, а также опубликовывать свои собственные.
                Чтобы писать статьи, необходимо зарегистрироваться на сайте. После регистрации вам также станут доступны
                комментарии и лайки.</p>
            <p>На сайте присутствует система модерации. Например, если вы увидели в комментариях рекламу онлайн-казино,
                вы можете оставить комментарий, начинающийся на @moderator и содержащий причину обращения - наши
                модераторы обязательно уберут нежелательный контент. Также модератор имеет право блокировки
                пользователя, оставившего комментарий с нежелательным и оскорбляющим содержанием. Относитесь с уважением
                друг к другу!</p>
        </div>
    );
};

export default InfoPage;