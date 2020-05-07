from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, PostbackEvent
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '@按鈕樣板':
                        func.sendButton(event)
    
                    elif mtext == '@確認樣板':
                        func.sendConfirm(event)
    
                    elif mtext == '@轉盤樣板':
                        func.sendCarousel(event)
    
                    elif mtext == '@圖片轉盤':
                        func.sendImgCarousel(event)
    
                    elif mtext == '@購買披薩':
                        func.sendPizza(event)
    
                    elif mtext == '@yes':
                        func.sendYes(event)
    
            if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
                if backdata.get('action') == 'buy':
                    sendBack_buy(event, backdata)
                elif backdata.get('action') == 'sell':
                    sendBack_sell(event, backdata)

        return HttpResponse()

    else:
        return HttpResponseBadRequest()
def sendBack_buy(event, backdata):  #處理Postback
    try:
        text1 = '感謝您購買披薩，我們將盡快為您製作。\n(action 的值為 ' + backdata.get('action') + ')'
        text1 += '\n(可將處理程式寫在此處。)'
        message = TextSendMessage(  #傳送文字
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_sell(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = '點選的是賣 ' + backdata.get('item')
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
