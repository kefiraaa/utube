class Messages:

    START_MSG = (
        "Пиши /help"
    )

    HELP_MSG = [
        ".",
        "**Давай узнаем, как я работаю. **\n\n**Шаг 1:** __Вы разрешаете мне загружать видео на ваш канал YouTube. "
        "\n\n**Шаг 2:** __Вы присылаете мне любое видео в Telegram.__\n\n**Шаг 3:** __Чтобы его загрузить тебе необходимо ответить на видео и написать комманду "
        "__/u "
        "\n\n**Шаг 4:** __Я удаленно скачиваю видео и загружаю его на ваш канал Youtube.__\n\n**Шаг 5:** __Я "
        "отправлю тебе ссылку на загруженный видеоролик.__",
        "**Давай перейдём к авторзиации.**\n\nВы должны предоставить мне доступ для загрузки видео в свой аккаунт Youtube. "
        "Нажмите на кнопку 'Авторизация' либо скопируйте ссылку у кнокпки и перейдите по ней. "
        "Далее разрешите доступ и скопируйте код.Вернись сюда и напечатай `/a 'и ваш код' ",
    ]

    NOT_A_REPLY_MSG = "Пожалуйста, ответьте на какой-нибудь видеофайл. "

    NOT_A_MEDIA_MSG = "Медиа-файл не найден. " + NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "Не верный формат файла. "

    DAILY_QOUTA_REACHED = "Похоже, сегодня вы пытаетесь загрузить более 6 видео! По умолчанию YouTube "
    "позволяет загрузить около 6 загрузок в день. "

    PROCESSING = "Обработка..... "

    NOT_AUTHENTICATED_MSG = "Вы не аутентифицировали меня для загрузки видео в какую-либо учетную запись. напишите /help "

    NO_AUTH_CODE_MSG = "Кода нет. Пожалуйста, предоставьте код "

    AUTH_SUCCESS_MSG = "Поздравляем, вы успешно аутентифицировали канал для загрузки на Youtube. \nУдачной загрузки! "

    AUTH_FAILED_MSG = "Ошибка аутентификации \nДетали :{}"

    AUTH_DATA_SAVE_SUCCESS = "Данные авторизации успешно сохранены! "
