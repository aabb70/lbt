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
import t1

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
            original_content_url = "https://cdn.discordapp.com/attachments/682086463265177652/707961786938425434/70756594_2871486492880328_5131557763402432512_n.jpg",
            preview_image_url = "https://fairmedia.tw/wp-content/uploads/20191112002764.jpg"
        )
    elif(text=="@促銷商品"):
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='文字訊息',
                            text='賣披薩'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/qaAdBkR.png',
                        action=PostbackTemplateAction(
                            label='回傳訊息',
                            data='action=sell&item=飲料'
                        )
                    )
                ]
            )
        )
    elif(text=="@直播連結"):
        reply_text = HP
        message = TextSendMessage(reply_text)
    elif(text=="@幫助"):
        reply_text = "歡迎加入本帳號為好友:D\n以下是指令及功能介紹\n>查詢商品\n點擊下方選單即可查看\n>聯絡方式\n請在對話欄輸入'@聯絡方式'即可查看\n>熱門商品\n\n在對話欄輸入'@熱門商品'即可看到最熱銷商品"
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