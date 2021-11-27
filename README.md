# Telegram Info
A telegram user or chat information finder

## Installation

```
pip install TelegramInfo
```

## Usage

```py
import pyrogram
import telegraminfo


# For user data
def user_filter(client, message):
    message.reply_text(
        text=telegraminfo.user(message.from_user)
    )
# returns data of user as text


# For chat data
def chat_filter(client, message):
    message.reply_text(
        text=telegraminfo.chat(message.from_chat)
    )
# returns data of chat as text
```
