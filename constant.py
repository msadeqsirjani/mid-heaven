def get_welcome_message(fullname: str) -> str:
    return f'Hello, <b>{fullname}</b>\nThis is a bot available on Telegram directly from MidJourney!\n🔥 Now you can ' \
           f'create any image according to the text description without leaving the messenger!'


def prepare_example_caption(text: str, index: int = 0) -> str:
    if index != 0:
        return f'{index} - example \n\n' \
               f"Description: <b>{text}</b>\n\n" \
               "👉@midheavon_bot"
    else:
        return f"\n\nDescription: <b>{text}</b>\n\n👉@midheavon_bot"


create = "Create 🤖"
create_image = "🖍The picture is being drawn..."
create_description = "Please answer the following questions to describe your structure. \n\n🖋<i>Complete the " \
                     "poll ...</i>"
create_successfull = "Generating photos is successfully completed"
example = "Example 🏞"
cancel = "🔙 Cancel"
about_us = "About us 👁️"
errors = "🛠Bot is undergoing technical work. Please try again later.\n\n<i>We apologize for the inconvenience!</i>"
block = "📌 You can send a request 2 times in 12 hours. \n\nYour request has exceeded the limit. You can use it again " \
        "after 12 hours"
null_description = 'We do not have samples yet.'
description = 'An example of images produced by midjourney'
