# Mid-Heaven | Telegram Text-to-Image Bot

## Overview

This project is a Telegram bot that converts text messages into images using the state-of-the-art mid-journey model. The bot receives text input from users and generates images based on the provided text, making it a fun and creative tool for expressing messages visually.

## Features

- Converts text messages to images.
- Utilizes the powerful mid-journey model for image generation.
- Integrates seamlessly with Telegram for easy access and usage.
- Supports various text inputs for generating images.

## Prerequisites

Before running the Mid-Heaven, ensure you have the following packages installed:

- `aiogram==2.25.1`
- `aiohttp==3.8.4`
- `aiosignal==1.3.1`
- `async-timeout==4.0.2`
- `attrs==22.2.0`
- `Babel==2.9.1`
- `certifi==2022.12.7`
- `charset-normalizer==3.0.1`
- `colorama==0.4.6`
- `environs==9.5.0`
- `frozenlist==1.3.3`
- `idna==3.4`
- `magic-filter==1.0.9`
- `marshmallow==3.19.0`
- `multidict==6.0.4`
- `openai==0.27.0`
- `packaging==23.0`
- `pydantic==1.10.5`
- `python-dotenv==1.0.0`
- `pytz==2022.7.1`
- `replicate==0.5.0`
- `requests==2.28.2`
- `tqdm==4.64.1`
- `typing_extensions==4.5.0`
- `urllib3==1.26.14`
- `yarl==1.8.2`

You can install these packages using `pip`:

```bash
pip install aiogram aiohttp aiosignal async-timeout attrs Babel certifi charset-normalizer colorama environs frozenlist idna magic-filter marshmallow multidict openai packaging pydantic python-dotenv pytz replicate requests tqdm typing_extensions urllib3 yarl
```

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/msadeqsirjani/mid-heaven.git
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages as mentioned in the "Prerequisites" section.

4. Create a `.env` file in the project directory and add your Telegram Bot API token. You can obtain a token by talking to the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

   ```dotenv
   TELEGRAM_API_TOKEN=your_token_here
   REPLICATE_API_TOKEN=you_toke_here
   OPEN_AI_API_TOKEN=you_token_here
   ```

## Usage

1. Run the bot using the following command:

   ```bash
   python main.py
   ```

2. Start a conversation with your Telegram bot on the Telegram app.

3. Send a text message to the bot, and it will respond with an image generated from the text.

## Contributing

Contributions to this project are welcome! Feel free to open issues, submit pull requests, or suggest improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** This project is for educational and entertainment purposes only. Use it responsibly and respect the privacy and terms of service of the platforms you interact with.

If you have any questions or need further assistance, please contact [msadeqsirjani@yahoo.com](mailto:msadeqsirjani@yahoo.com).
