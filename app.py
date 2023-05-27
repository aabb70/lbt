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

def pushMessage(event, text):
    try:
        msg = text[6:]  #取得訊息
        message = TextSendMessage(
            text = msg
        )
        line_bot_api.push_message(to, TextSendMessage(text = msg))  #推播訊息
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImgmap(event):  #圖片地圖
    try:
        image_url = 'https://i.imgur.com/WyVPiHa.jpg'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 1306
        image_url2 = 'https://i.imgur.com/mobIlul.jpg'  #圖片位址
        imgwidth2 = 1040  #原始圖片寛度一定要1040
        imgheight2 = 1007
        message = [
            ImagemapSendMessage(
            base_url=image_url,
            alt_text="熱門商品",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                URIImagemapAction(  #開啟網頁
                    link_uri='https://shopee.tw/aabb7172',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=0, 
                        y=1149, 
                        width=imgwidth*0.5, 
                        height=157  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='https://reurl.cc/x0pbkN',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.5, 
                        y=1149, 
                        width=imgwidth*0.5, 
                        height=157  
                    )
                ),
            ]
            ),
            ImagemapSendMessage(
            base_url=image_url2,
            alt_text="熱門商品",
            base_size=BaseSize(height=imgheight2, width=imgwidth2),  #圖片寬及高
            actions=[
                 URIImagemapAction(  #開啟網頁
                    link_uri='https://shopee.tw/aabb7172',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=0, 
                        y=850, 
                        width=imgwidth*0.5, 
                        height=157  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='https://reurl.cc/2g6km4',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.5, 
                        y=850, 
                        width=imgwidth*0.5, 
                        height=157  
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
def sendImgmap3(event):  #圖片地圖
    try:
        image_url = 'https://i.imgur.com/Y8wKbmm.png'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 850
        message = ImagemapSendMessage(
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
                    link_uri='https://reurl.cc/2gK0v4',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.5, 
                        y=693, 
                        width=imgwidth*0.5, 
                        height=157
                    )
                ),
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImgmap4(event):  #圖片地圖
    try:
        image_url = 'https://i.imgur.com/UBRq9nW.jpg'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 615
        message = ImagemapSendMessage(
            base_url=image_url,
            alt_text="麥芽餅",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                URIImagemapAction(  #開啟網頁
                    link_uri='https://reurl.cc/5qK7ln',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=0, 
                        y=520, 
                        width=imgwidth, 
                        height=95  
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
def funcserach(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇需要使用的功能',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="常見問題", data='action=Func1')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="聯絡方式", data='action=Func2')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="促銷商品", data='action=Func3')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="專人客服", data='action=Func4')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def manageForm(event, text, user_id):  #處理LIFF傳回的FORM資料
    try:
        flist = text[3:].split('/')  #去除前三個「#」字元再分解字串
        T = flist[1][0]
        roomtype = flist[0]  #取得輸入資料
        amount = flist[1]
        tel = flist[2]
        if flist[0] == "男":
            R = "先生"
        elif flist[0] == "女":
            R = "小姐"
        else:
            R = "用戶"
        text1 = "親愛的"+ T + R + "，您的問題我們已經收到，個人資料如下："
        text1 += "\n性別：" + roomtype
        text1 += "\n姓名：" + amount
        text1 += "\n電話：" + tel
        message = TextSendMessage(  #顯示訂房資料
            text = text1
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
    elif backdata.get('action') == 'Func1':
        sendQuickreply(event)
    elif backdata.get('action') == 'Func2':
        sendBack_Func2(event, backdata)
    elif backdata.get('action') == 'Func3':
        try:
            message = TemplateSendMessage(
                alt_text='圖片轉盤樣板',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/MZlMaDT.png',
                            action=PostbackTemplateAction(
                                label='點擊購買',
                                data='action=sell&item=麥芽餅&URL=https://reurl.cc/2gK0v4'
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
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    user_id = event.source.user_id
    print("user_id =", user_id)
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
    elif (text=="@功能查詢"):
        message = funcserach(event)
    elif (text=="@客服"):
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/k1aqgPP.png',
        title='專人客服',
        text='請選擇查詢的類別',
        actions=[
            URITemplateAction(
                label='點擊加入客服好友',
                uri='https://lin.ee/M8o7Dhr'
            )
        ]
    )
)
    elif text[:3] == '###' and len(text) > 3:  
        manageForm(event, text, user_id)
    elif(text=="@熱門商品"):
        sendImgmap(event)
    elif(text=="@洗髮精"):
        sendImgmap2(event)
    elif(text=="@麥芽餅"):
        sendImgmap4(event)
    elif(text=="@促銷商品"):
        try:
            message = TemplateSendMessage(
                alt_text='圖片轉盤樣板',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/MZlMaDT.png',
                            action=PostbackTemplateAction(
                                label='點擊購買',
                                data='action=sell&item=麥芽餅&URL=https://reurl.cc/2gK0v4'
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
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    elif(text=="@意見回饋"):
        reply_text = "https://liff.line.me/1655093260-AD5VDqxd"
        message = TextSendMessage(reply_text)
    elif(text=="@新品上市"):
        message = sendImgmap3(event)
    elif(text=="@常見問題"):
        message = sendQuickreply(event)
    elif(text=="@幫助"):
        reply_text = "歡迎加入本帳號為好友:D\n以下是指令及功能介紹\n>查詢商品\n點擊下方選單即可查看\n>聯絡方式\n請在對話欄輸入'@聯絡方式'即可查看\n>熱門商品\n請在對話欄輸入'@熱門商品'即可看到最熱銷商品\n>常見問題\n請在對話欄輸入'@常見問題'選取您想知道的資訊。\n促銷商品推薦\n請在對話欄輸入'@促銷商品'獲得我們的商品訊息。\n專人客服\n請輸入'@客服'後，點擊加入客服好友，我們會盡速回覆您。"
        message = TextSendMessage(reply_text)
    elif(text=="@聯絡方式"):
        reply_text = "https://shopee.tw/aabb7172\n↑使用蝦皮聊聊來聯絡我們\n\nhttps://reurl.cc/e8kjrQ\n↑使用Facebook粉絲專業聯絡我們\n\nhttps://www.instagram.com/junrulive_001/\n↑使用Instagram來聯絡我們"
        message = TextSendMessage(reply_text)
    else:
        reply_text = "如找不到您所想找的東西，請輸入'@幫助'他會直接回覆您。"
        message = TextSendMessage(reply_text)
        
    line_bot_api.reply_message(event.reply_token, message)
def sendBack_QA1(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = "營業時間週一~週五 10:00-24:00 週末:12:00-23:00 可先來電0917781338洽詢。"
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
def sendBack_Func2(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = "https://shopee.tw/aabb7172\n↑使用蝦皮聊聊來聯絡我們\n\nhttps://reurl.cc/e8kjrQ\n↑使用Facebook粉絲專業聯絡我們\n\nhttps://www.instagram.com/junrulive_001/\n↑使用Instagram來聯絡我們"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendBack_onsale(event, backdata):
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/MZlMaDT.png',
                        action=PostbackTemplateAction(
                            label='點擊購買',
                            data='action=sell&item=麥芽餅&URL=https://reurl.cc/2gK0v4'
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
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)