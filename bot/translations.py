class Messages:

    START_MSG = (
        "Hi there {}.\n\nI'm Youtube Uploader Bot.You can use me to upload any telegram video to youtube "
        "once you authorise me.You can know more from /help.\n\nThank you."
    )

    HELP_MSG = [
        ".",
        ""
        "****\n\n**Step 1:**"
        "**Now lets authorise.**\n\nYou need to give me the access to upload videos to your Youtube account.For that "
        "open the given link and allow access and copy the code. Come back here and type `/authorise copied-code` and "
        "send it.\n\n",
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
