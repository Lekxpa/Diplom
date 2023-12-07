from telegram import Update


def start_bot_msg():
    return f'start bot'


def stop_bot_msg():
    return f'stop bot'


def start_msg(update: Update):
    return f'Приветствуем Вас, {update.effective_user.first_name},\n\
        \nна страничке маркетингового агентства\n\
        \n"Продаем всё, быстро и легко!"\n\
        \nНажмите кнопку "menu" для выбора необходимого действия\n\
        \n/menu'


def about_msg():
    return 'Мы - маркетинговое агентство полного цикла по онлайн продвижению малого и среднего бизнеса в Интернете и соцсетях\n\
        \nМы работаем с 2017 года и каждый день увеличиваем прибыль своих клиентов за счет эффективных комплексных решений\n\
        \nУспешно реализовали более 150 проектов\n\
        \n/menu\n\
        \n/more_information'


def information_msg():
    return 'Мы настроены на долгосрочное сотрудничество и партнерские отношения. Наша команда вникает во все тонкости Вашего бизнеса и готовит персональное проработанное коммерческое предложение\n\
        \nУ нас есть разные варианты пакетов и отдельных услуг, которые подойдут под любой тип бизнеса\n\
        \nУ нас вы можете заказать комплекс услуг по продвижению бизнеса\n\
        \n/menu'


def services_msg():
    return 'Наши услуги:\n\
        \nРазработка маркетинговой стратегии и ее внедрение\n\
        \nМаркетинговый аудит бизнеса\n\
        \nАутсорсинг маркетинга\n\
        \nРазработка сайтов\n\
        \nВедение социальных сетей\n\
        \nНастройка Яндекс Директ и Google Adwords, таргетированной рекламы\n\
        \n/menu'


def portfolio_msg():
    return 'Вы можете ознакомиться с некоторыми нашими проектами здесь(кратко):\n\
        \nФинансовый проект "Бенфин" - Комплексное продвижение нового сервиса, разработка маркетинговой стратегии, подбор рекламных каналов и запуск рекламы\n\
        \nСеть студий женского фитнеса «GGym» - Комплексное продвижение бренда, разработка фирменного стиля, привлечение новых посетителей\n\
        \nПекарня «Хлеб с маслом» - разработка и внедрение комплексной стратегии для пекарни\n\
        \nПолная информация по этим и другим проектам представлена в презентации: \n\
        /get_presentation\n\
        \n/menu'


def price_msg():
    return 'Наши цены:\n\
        \nРазработка маркетинговой стратегии и ее внедрение - от 50 000 руб\n\
        \nМаркетинговый аудит бизнеса - от 30 000 руб\n\
        \nАутсорсинг маркетинга - от 30 000 руб\n\
        \nРазработка сайтов - от 15 000 руб\n\
        \nВедение социальных сетей - от 15 000 руб\n\
        \nНастройка Яндекс Директ и Google Adwords, таргетированной рекламы - от 15 000 руб\n\
        \n/menu'


def contacts_msg():
    return 'Наши контакты:\n\
        \nтел.: + 7 495 550 15 05\n\
        \nадрес: Москва, Лесной туп., 25, оф.2\n\
        \nРежим работы: с 10-00 до 21-00\n\
        \nВы можете оставить заявку с Вашими контактными данными - мы свяжемся с Вами в указанное Вами время - обсудим интересующие Вас вопросы!\n\
        \nОставить заявку: /request\n\
        \nили позвонить нам: /call\n\
        \n/menu'


def call():
    return '+ 74955501505\n\
        \n/menu'
    

def send_request():
    return 'Благодарим Вас за заявку! Мы свяжемся с Вами в ближайшее время!\n\
            \n/menu'


def request():
    return 'Нажмите, пожалуйста, кнопку send_request,\n\
        \n/send_request\n\
        \nчтобы автоматически отправить свои данные\n\
        \n(имя и ник в Telegram)\n\
        \nнашему менеджеру,чтобы он смог связаться с Вами,\n\
        \nлибо нажмите кнопку menu для возврата в основное меню\n\
        \n/menu'