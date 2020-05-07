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
    if (text=="@查詢商品"):
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/uaCoaSQ.png',
        title='查詢商品',
        text='請選擇查詢的類別',
        actions=[
            URITemplateAction(
                label='居家生活',
                uri='https://shopee.tw/shop/14084056/search?shopCollection=15337481'
            ),URITemplateAction(
                label='3C',
                uri='https://shopee.tw/search?keyword=%E5%90%8B&shop=14084056'
            ),URITemplateAction(
                label='美妝',
                uri='https://shopee.tw/shop/14084056/search?shopCollection=17513740'
            ),URITemplateAction(
                label='零食',
                uri='https://shopee.tw/shop/14084056/search?page=0&shopCollection=30087730'
            )
        ]
    )
)

    elif(text=="@熱門商品"):
        message = ImageSendMessage (
            original_content_url = "https://vignette.wikia.nocookie.net/bahapedia/images/e/ef/025c3937969d2ff9591374cb6dcd0cad.JPG/revision/latest/top-crop/width/360/height/450?cb=20180806122947&path-prefix=zh"
            preview_image_url = "https://fairmedia.tw/wp-content/uploads/20191112002764.jpg"
        )
    elif(text=="@直播連結"):
        reply_text = HP
        message = TextSendMessage(reply_text)
    elif(text=="@美妝保養"):
        reply_text = BT
        message = TextSendMessage(reply_text)
    elif(text=="@手機"):
        reply_text = "https://shopee.tw/search?keyword=%E6%89%8B%E6%A9%9F&shop=14084056"
        message = TextSendMessage(reply_text)
    elif(text=="@零食"):
        reply_text = "https://shopee.tw/shop/14084056/search?shopCollection=3801770"
        message = TextSendMessage(reply_text)
    elif(text=="@幫助"):
        reply_text = "歡迎加入本帳號為好友:D\n以下是指令及功能介紹\n>查詢商品\n點擊下方選單即可查看\n>聯絡方式\n請在對話欄輸入'@聯絡方式'即可查看"
        message = TextSendMessage(reply_text)
    elif(text=="@聯絡方式"):
        reply_text = "https://reurl.cc/Qd56r0\n↑使用蝦皮聊聊來聯絡我們\n\nhttps://reurl.cc/4R63KV\n↑使用Facebook粉絲專業聯絡我們\n\nhttps://reurl.cc/yZDe2l\n↑使用Instagram來聯絡我們"
        message = TextSendMessage(reply_text)
    else:
        reply_text = text
        message = TextSendMessage(reply_text)
    
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)