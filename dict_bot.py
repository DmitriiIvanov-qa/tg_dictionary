# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить  — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='6158552639:AAEb-hSQ2NxSDXoGU2hIKQntEChn0O0DMdY', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'регресс': 'проверить что новый функционал не сломал существующий',
    'адаптив': 'адаптивный дизайн, адаптация интерфейса к использованию на разных экранах',
    'аджайл': 'от англ. Agile. Общий термин, который описывает ценности и принципы гибкой разработки программного обеспечения, а также практические подходы к разработке. Понятие Agile стало популярным после публикации Манифеста гибкой разработки программного обеспечения в 2001 году',
    'айдишник': 'id, идентификатор',
    'альфа': 'этап разработки программного обеспечения, на котором разработчики добавляют в программу новые функции, а тестировщики испытывают программу. Это внутренний или непубличный этап',
    'апишка': 'API, программный интерфейс приложения или интерфейс прикладного программирования',
    'апрув': 'или гаг. апрувнуть - от англ. Approve. Одобрение, одобрить, утвердить',
    'аутсорс': 'аутсорсинг, передача компанией части операционной деятельности другой компании',
    'баг': 'от англ. Bug — жучок, клоп. Ошибка в программе',
    'бахнуть': ' что-то быстро сделать, изменить или дополнить функциональность приложения',
    'бета': 'бета-версия, приложение на стадии публичного тестирования',
    'бот': 'сокращение от «робот». Ботом называют программу, которая автоматизирует интерфейс. Пример — автоответчик в чате',
    'бэкап': 'или гаг. бэкапить — резервная копия или процесс создания резервной копии приложения',
    'бэкенд': 'от англ. Back-end. Программно-аппаратная или серверная часть приложения',
    'бэклог': 'от англ. Backlog. Перечень рабочих задач команды разработчиков, упорядоченный по приотритету',
    'ворнинг': 'от англ. Warning — предупреждение. Предупреждающее сообщение в интерфейсе',
    'войтивайти': 'шуточное выражение, обозначает процесс переквалификации далекого от IT-сферы специалиста в разработчика',
    'выкатить': 'сделать доступным для пользователей. Например, «выкатили новую версию сайта» значит сделали новую версию сайта доступной для пользователей',
    'выпадашка': 'выпадающее меню, то же, что и «дропдаун»',
    'галера': 'компания, в которой платят низкие зарплаты и не ценят разработчиков',
    'гит': 'система контроля версий Git или сервис GitHub',
    'говнокод': 'плохой, некачественный код',
    'градиент': 'плавный переход из одного цвета в другой',
    'грумить': 'от англ. Grooming. Приводить в порядок, «причесывать»',
    'движок': 'в веб-разработке так называют системы управления контентом',
    'дебажить': 'устранять ошибки, баги',
    'деплой': 'развёртывание, публикация рабочей версии приложения. Пример: задеплоить сайт — перенести сайт с тестового на рабочий сервер, сделать его доступным для пользователей',
    'деплоить': 'развёртывавать, публиковать рабочую версию приложения. Пример: задеплоить сайт — перенести сайт с тестового на рабочий сервер, сделать его доступным для пользователей',
    'джун': 'от англ. Junior. Младший разработчик. Специалист без опыта или с минимальным опытом работы',
    'джуниор': 'от англ. Junior. Младший разработчик. Специалист без опыта или с минимальным опытом работы',
    'дезигнер': 'презрительно-снисходительное название дизайнера',
    'докеризировать': 'завернуть приложение в докер (платформу для разработки, доставки и запуска контейнерных приложений)',   
    'драй': 'от англ. DRY, don’t repeat yourself. Принцип программирования, предлагающий избегать повторений кода',
    'дропдаун': 'выпадающее меню, то же, что и «выпадашка»',
    'дропнуть': 'от англ. Drop. Удалить, отключить, сбросить или обнулить что-либо',
    'жаба': 'язык программирования Java',
    'жабаскрипт': 'язык программирования JavaScript',
    'залить': 'загрузить. Например, «залить файлы на сервер»',
    'запилить': 'сделать что-то, добавить какую-то функциональность',
    'змея': 'язык программирования Python',
    'исходник': 'файлы, в которых находится исходный код приложения, или сам исходный код',
    'итерация': 'повторение. «Мы сделали несколько итераций» — мы повторили шаг несколько раз',
    'колл': 'от англ. Call. Созвон, онлайн-конференция, онлайн-совещание',
    'коммит': 'от англ. To commit — совершать. В контексте работы над приложением — сохранять код в репозитории',
    'коммитить': 'от англ. To commit — совершать. В контексте работы над приложением — сохранять код в репозитории',
    'конфа': 'конференция',
    'копипаста': 'от англ. Copy-Paste. Скопированный откуда-то код',
    'костыль': 'код, который нужен, чтобы исправить несовершенство ранее написанного кода',
    'легаси': 'от англ. Legacy. Морально устаревший код, который не обновляется, но используется. Или код, который разработчик получил по наследству от предыдущих разработчиков',
    'либа': 'от англ. Library — библиотека. Речь идет о библиотеках кода, например, React',
    'линтер': 'общее нарицательное название программ, которые анализируют код и предупреждают разработчика об ошибках',
    'лист': 'от англ. List — список',
    'локалка': 'локальный. Например, локальный сервер или сеть',
    'мидл': 'от англ. Middle — средний. Уровень разработчика, следующий за джуниором. Опыт и уровень знаний миддла позволяет ему самостоятельно решать серьезные задачи',
    'мёржить': 'от англ. Merge, сливать. Речь идет об объединении или слиянии веток кода',
    'меншить': 'от англ. Mention — упоминание. Упоминанать в чатах или соцсетях. «Менши меня, когда будет готово» значит «упомяни меня, когда будет готово»',
    'навбар': 'навигационный блок на сайте или в интерфейсе программы',
    'накатить': ' внести изменения, задеплоить новую версию приложения. Противоположное термину «откатить»',
    'опенсорс': 'от англ. Open Source. Программное обеспечение с открытым исходным кодом',
    'опен-сорс': 'от англ. Open Source. Программное обеспечение с открытым исходным кодом',
    'откатить': 'удалить изменения, вернуть предыдущую версию приложения. Противоположное термину «накатить»',
    'ось': 'операционная система',
    'падаван': 'ироничное название стажера или джуниора',
    'пилот': 'пробная (пилотная) версия продукта',
    'питон': 'язык программирования Python',
    'подвал': 'то же, что и «футер». Элемент структуры страницы, который находится в нижней части и содержит служебную информацию — контакты, ссылки на соцсети, публичная оферта и т. д',
    'поплыла вёрстка': 'некорректное отображение страницы в браузере',
    'продакшн': 'обозначение кода для рабочей версии приложения',
    'продакшен': 'обозначение кода для рабочей версии приложения',
    'продакшн-код': 'обозначение кода для рабочей версии приложения',
    'пушить': 'использовать команду push, публиковать что-то',
    'пэхапэ': 'язык программирования PHP, то же, что и «пыха»',
    'пыха': 'язык программирования PHP, то же, что и «пэхапэ»',
    'рекурсия': 'описание процесса с помощью самого процесса. Например, выражение «рекурсивный вызов функции» описывает ситуацию, в которой функция вызывает сама себя',
    'релиз': 'программное обеспечение на стадии публичного использования. Стабильная версия программы, которая прошла тестирование',
    'релокация': 'перевод сотрудника или бизнеса в другое место внутри страны или за границу',
    'репа': 'репозиторий, хранилище данных. Например, код программы можно хранить в репозитории на GitHub',
    'ридми': 'файл Readme, в котором содержится информация о программе',
    'ругаться': 'например, линтер ругается — сообщения об ошибках в коде, работе сервиса и так далее',
    'сабж': 'от английского Subject — тема, предмет. «По сабжу» — по теме обсуждения',
    'свитчнуть': 'переключить. От английского switch',
    'свичнуть': 'переключить. От английского switch',
    'сетка': 'модульная сетка, используется для дизайна и верстки страниц',
    'сеньор': 'от англ. Senior — старший разработчик',
    'синьор': 'от англ. Senior — старший разработчик',
    'слетело': 'сломалось',
    'снести': 'удалить',
    'сорец': 'от англ. Source. Исходный код',
    'сорцы': 'от англ. Source. Исходный код',
    'стек': 'изначально абстрактный тип данных. В разговорной речи используется для обозначения списка технологий, которые использует разработчик или компания. Пример: «Наш стек — HTML/CSS, JavaScript, React»',
    'собес': 'собеседование',
    'софт': 'от англ. Software — программное обеспечение',
    'софт-скиллы': 'от англ. Soft skills — знания и качества специалиста, прямо не связанные с профессиональной деятельностью. Примеры: коммуникабельность, проактивность',
    'спринт': 'короткий промежуток времени (до 4 недель), в течение которого scrum-команда выполняет определенный объем работы',
    'таска': 'от англ. Task. Задание, задача',
    'тачка': 'компьютер',
    'темплейт': 'от английского Template — шаблон',
    'тестировщик': 'специалист по тестированию программного обеспечения',
    'тимлид': 'от английского Team Lead — руководитель команды. Координатор группы программистов',
    'убить': 'удалить что-то. Например, «убить профиль» означает удалить профиль',
    'фидбек': 'от англ. Feedback — обратная связь',
    'Фиксить': 'от англ. Fix. Чинить, починить, исправить',
    'пофиксить': ' от англ. Fix. Чинить, починить, исправить',
    'фича': 'функция, возможность. От англ. Feature',
    'фреймворк': 'от англ. Framework — каркас. Инструмент разработки, набор типовых шаблонных решений, упрощающих работу программиста. Примеры: Laravel, Bootstrap',
    'фронтенд': 'от англ. Front-end — клиентская часть приложения',
    'хатэмээль': 'HTML, язык гипертекстовой разметки',
    'хатээмэль': 'HTML, язык гипертекстовой разметки',
    'хардкодить': 'статически прописывать в коде данные, которые должны вычисляться динамически. Плохая практика, антипаттерн в программировании',
    'хацкер': 'ироничное название начинающего специалиста, который считает себя опытным программистом. От английского Hacker и Cool Hacker',
    'кулхацкер': 'ироничное название начинающего специалиста, который считает себя опытным программистом. От английского Hacker и Cool Hacker',
    'хедер': 'элемент структуры веб-страницы, находится в верхней части и содержит логотип, меню, служебную информацию',
    'хэдер': 'элемент структуры веб-страницы, находится в верхней части и содержит логотип, меню, служебную информацию',
    'хотфикс': 'от англ. Hotfix. Срочное исправление критических ошибок, уязвимостей или недоработок в программе',
    'цэмээс': 'от англ. CMS — Content Management System, система управления контентом',
    'цээмэс': 'от англ. CMS — Content Management System, система управления контентом',
    'цээсэс': 'от англ. CSS — Cascading Style Sheets, каскадные таблицы стилей',
    'чекать': 'от англ. Check. Проверять, проверить',
    'чекнуть': 'от англ. Check. Проверять, проверить',
    'прочекать': 'от англ. Check. Проверять, проверить',
    'юзать': 'от английского To use — использовать',
    'ява': 'язык программирования Java',
    'яваскрипт': 'язык программирования JavaScript',
    'яп': 'язык программирования',
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, регресс', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
