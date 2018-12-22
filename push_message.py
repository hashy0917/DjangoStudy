#!/usr/bin/python

from linebot import LineBotApi
from linebot.models import TextSendMessage

LINE_CHANNEL_ACCESS_TOKEN = ""

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def linepush(message):
    user_id = ""
    messages = TextSendMessage(text=message)
    line_bot_api.push_message(user_id, messages=messages)


if __name__ == "__main__":
    message = input("送信したいメッセージを入力してください\n")
    linepush(message)
