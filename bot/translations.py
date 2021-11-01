class Messages:

    START_MSG = (
        "Пиши /help"
    )

    HELP_MSG = [
        ".",
        "**Давай узнаем, как я работаю. **\n\n**Шаг 1:** __Вы разрешаете мне загружать видео на ваш канал YouTube. "
        "\n\n**Шаг 2:** __Вы присылаете мне любое видео в Telegram.__\n\n**Шаг 3:** __Чтобы его загрузить тебе необходимо ответить на видео и написать комманду "
        "__/upload "
        "\n\n**Шаг 4:** __Я удаленно скачиваю видео и загружаю его на ваш канал Youtube.__\n\n**Шаг 5:** __Я "
        "отправлю тебе ссылку на загруженный видеоролик.__",
        "**Now lets authorise.**\n\nYou need to give me the access to upload videos to your Youtube account.For that "
        "open the given link and allow access and copy the code. Come back here and type `/authorise copied-code` and "
        "send it.\n\n**Fear not!**\nI'm not a hacker or someone who wants to creep into people's privacy. I respect "
        "one's privacy. I'm here just to help anyone who wants help. If I was a hacker I won't be sitting here "
        "writing Telegram Bots.",
    ]

    NOT_A_REPLY_MSG = "Please reply to some video file."

    NOT_A_MEDIA_MSG = "No media file found. " + NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media"

    DAILY_QOUTA_REACHED = "Looks like you are trying to upload more than 6 videos today! By default youtube only "
    "allows about 6 uploads daily, so this request might fail!!"

    PROCESSING = "Processing....."

    NOT_AUTHENTICATED_MSG = "You have not authenticated me to upload video to any account. see /help to authenticate"

    NO_AUTH_CODE_MSG = "There is no code. Please provide some code"

    AUTH_SUCCESS_MSG = "Congrats, you have successfully authenticated me to upload to Youtube.\nHappy uploading!"

    AUTH_FAILED_MSG = "Authentication failed\nDetails:{}"

    AUTH_DATA_SAVE_SUCCESS = "Successfully saved the given auth data!"
