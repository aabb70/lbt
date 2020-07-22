from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import configparser
from urllib.parse import parse_qsl

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
def sendImgmap(event):  #圖片地圖
    try:
        image_url = 'https://i.imgur.com/kPVORK4.png'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 850
        image_url2 = 'https://i.imgur.com/mEiVuBQ.jpg'  #圖片位址
        imgwidth2 = 1040  #原始圖片寛度一定要1040
        imgheight2 = 780
        message = [
            ImagemapSendMessage(
            base_url=image_url,
            alt_text="圖片地圖範例",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                URIImagemapAction(  #開啟網頁
                    link_uri='https://shopee.tw/aabb7172',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=0, 
                        y=693, 
                        width=imgwidth*0.5, 
                        height=157  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='https://reurl.cc/Qdy7OM',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.5, 
                        y=693, 
                        width=imgwidth*0.5, 
                        height=157  
                    )
                ),
            ]
            ),
            ImagemapSendMessage(
            base_url=image_url2,
            alt_text="圖片地圖範例",
            base_size=BaseSize(height=imgheight2, width=imgwidth2),  #圖片寬及高
            actions=[
                URIImagemapAction(  #開啟網頁
                    link_uri='https://reurl.cc/Qdy7OM',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=0, 
                        y=0, 
                        width=imgwidth2, 
                        height=imgheight2  
                    )
                ),
            ]
        )
    ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImgmap2(event):  #圖片地圖
    try:
        image_url = 'https://i.imgur.com/mEiVuBQ.jpg'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 780
        message = ImagemapSendMessage(
            base_url=image_url,
            alt_text="圖片地圖範例",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                URIImagemapAction(  #開啟網頁
                    link_uri='https://reurl.cc/Qdy7OM',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=0, 
                        y=0, 
                        width=imgwidth, 
                        height=imgheight  
                    )
                ),
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇您的問題',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="營業時間", data='action=QA1')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="購買須知", data='action=QA2')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="取貨方式", data='action=QA3')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
# 接受BACKDATA訊息，回送問題回答
@handler.add(PostbackEvent)
def handle_postback(event):
    backdata = dict(parse_qsl(event.postback.data))
    if backdata.get('action') == 'QA1':
        sendBack_QA1(event, backdata)
    elif backdata.get('action') == 'sell':
        sendBack_sell(event, backdata)
    elif backdata.get('action') == 'QA2':
        sendBack_QA2(event, backdata)
    elif backdata.get('action') == 'QA3':
        sendBack_QA3(event, backdata)
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
                uri='https://shopee.tw/shop/26108934/search?page=0&shopCollection=37027391'
            ),URITemplateAction(
                label='香水',
                uri='https://shopee.tw/shop/26108934/search?page=0&shopCollection=37027388'
            ),URITemplateAction(
                label='身體清潔,保養',
                uri='https://shopee.tw/shop/26108934/search?page=0&shopCollection=37027389'
            )
        ]
    )
)

    elif(text=="@熱門商品"):
        sendImgmap(event)
    elif(text=="洗髮精"):
        sendImgmap2(event)
    elif(text=="@促銷商品"):
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/MZlMaDT.png',
                        action=PostbackTemplateAction(
                            label='點擊購買',
                            data='action=sell&item=麥芽餅&URL=https://reurl.cc/R4Qq4G'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/qtOiw17.png',
                        action=PostbackTemplateAction(
                            label='點擊購買',
                            data='action=sell&item=KIN卡碧絲洗髮精&URL=https://reurl.cc/nzRNEv'
                        )
                    )
                ]
            )
        )
    elif(text=="@常見問題"):
        message = sendQuickreply(event)
    elif(text=="@直播連結"):
        reply_text = HP
        message = TextSendMessage(reply_text)
    elif(text=="@幫助"):
        reply_text = "歡迎加入本帳號為好友:D\n以下是指令及功能介紹\n>查詢商品\n點擊下方選單即可查看\n>聯絡方式\n請在對話欄輸入'@聯絡方式'即可查看\n>熱門商品\n請在對話欄輸入'@熱門商品'即可看到最熱銷商品\n>常見問題\n請在對話欄輸入'@常見問題'選取您想知道的資訊。"
        message = TextSendMessage(reply_text)
    elif(text=="@聯絡方式"):
        reply_text = "https://shopee.tw/aabb7172↑使用蝦皮聊聊來聯絡我們\n\nhttps://reurl.cc/4R63KV\n↑使用Facebook粉絲專業聯絡我們\n\nhttps://www.instagram.com/junrulive_001/\n↑使用Instagram來聯絡我們"
        message = TextSendMessage(reply_text)
    else:
        reply_text = "如找不到您所想找的東西，請輸入 @幫助 他會直接回覆您。"
        message = TextSendMessage(reply_text)
    
    line_bot_api.reply_message(event.reply_token, message)
def sendBack_QA1(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = "營業時間週一~週五 10:00-22:00 週六 10:00-23:00 可先來電0917781338洽詢。"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendBack_QA2(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = "庫存變動快,網頁標示之尚餘數量不代表即時庫存量,請多多詢問有無現貨。"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendBack_QA3(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = "一般宅配、超商取貨\n請抽空來電詢問庫存量,以免臨時缺貨而擔誤您保貴的時間"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendBack_sell(event, backdata):  #處理Postback
    try:
        message = [
            TextSendMessage(  #傳送文字
                text = "歡迎選購"+ backdata.get('item')+",以下是購買連結。"
        ),
            TextSendMessage(  #傳送文字
                text = backdata.get('URL')
        )
    ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)