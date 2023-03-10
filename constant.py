def get_welcome_message(fullname: str) -> str:
    return f'Hello, <b>{fullname}</b>\nThis is a bot available on Telegram directly from MidJourney!\nπ₯ Now you can ' \
           f'create any image according to the text description without leaving the messenger!'


def prepare_example_caption(text: str, index: int = 0) -> str:
    if index != 0:
        return f'{index} - example \n\n' \
               f"Description: <b>{text}</b>\n\n" \
               "π@midheavon_bot"
    else:
        return f"\n\nDescription: <b>{text}</b>\n\nπ@midheavon_bot"


create = "Create π€"
create_image = "πThe picture is being drawn..."
create_description = "Please describe the picture in your imagination using words. \n\nπ<i>Enter text...</i>"
example = "Example π"
cancel = "π Cancel"
about_us = "About us ποΈ"
errors = "π Bot is undergoing technical work. Please try again later.\n\n<i>We apologize for the inconvenience!</i>"
block = "π You can send a request 2 times in 12 hours. \n\nYour request has exceeded the limit. You can use it again " \
        "after 12 hours"
null_description = 'We do not have samples yet.'
description = 'An example of images produced by midjourney'
