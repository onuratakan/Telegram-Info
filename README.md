```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/Telegram-Info/blob/main/LICENSE
```

---

## Installation

```
pip install TelegramInfo
```

---

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

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
