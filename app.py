from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import configparser
import random

app = Flask(__name__)

# 讀取config
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
HP = config.get('URLS','HP')
BT = config.get('URLS','BT')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body

    print(body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text
    if (text=="查詢商品"):
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url='https://2.bp.blogspot.com/-juSspSqB2mo/UF1jQJlaHKI/AAAAAAAAAOo/62CPquAChjA/s1600/9477o2.jpg',
        title='查詢商品',
        text='請選擇查詢的類別',
        actions=[
            URITemplateAction(
                label='吉娃娃',
                uri='https://2.bp.blogspot.com/-juSspSqB2mo/UF1jQJlaHKI/AAAAAAAAAOo/62CPquAChjA/s1600/9477o2.jpg'
            ),URITemplateAction(
                label='珍珠奶茶',
                uri='https://2.bp.blogspot.com/-juSspSqB2mo/UF1jQJlaHKI/AAAAAAAAAOo/62CPquAChjA/s1600/9477o2.jpg'
            ),URITemplateAction(
                label='外星狗',
                uri='https://2.bp.blogspot.com/-juSspSqB2mo/UF1jQJlaHKI/AAAAAAAAAOo/62CPquAChjA/s1600/9477o2.jpg'
            )
        ]
    )
)
    elif(text=="直播連結"):
        message = TextSendMessage(reply_text)
        reply_text = HP
    elif(text=="美妝保養"):
        message = TextSendMessage(reply_text)
        reply_text = BT
    elif(text=="手機"):
        message = TextSendMessage(reply_text)
        reply_text = "https://shopee.tw/search?keyword=%E6%89%8B%E6%A9%9F&shop=14084056"
    elif(text=="零食"):
        message = TextSendMessage(reply_text)
        reply_text = "https://shopee.tw/shop/14084056/search?shopCollection=3801770"
    else:
        message = TextSendMessage(reply_text)
        reply_text = text
    
    line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
