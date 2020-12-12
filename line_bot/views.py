from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature) # parse the requested event
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if event.message.text == '婚紗輪播':
                    pass
                elif event.message.text == '報名婚禮':
                    pass
                elif event.message.text == '交通資訊':
                    line_bot_api.reply_message(
                        event.reply_token,
                        LocationMessage(
                            title='新店白金花園酒店',
                            address='新北市新店區安興路77號',
                            latitude=24.97505893694744,
                            longitude=121.51534850259982
                        )
                    )

            elif isinstance(event, PostbackEvent): # Post Back Event
                pass


        return HttpResponse()
    else:
        return HttpResponseBadRequest()
