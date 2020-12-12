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
                    content = {
                      "type": "bubble",
                      "hero": {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "action": {
                          "type": "uri",
                          "uri": "http://linecorp.com/"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "HaoMin夫妻台北場婚禮",
                            "weight": "bold",
                            "size": "xl"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                              {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "地點",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
                                  },
                                  {
                                    "type": "text",
                                    "text": "白金花園酒店Platinum Hotel",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "地址",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
                                  },
                                  {
                                    "type": "text",
                                    "text": "新北市新店區安興路77號",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "時間",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
                                  },
                                  {
                                    "type": "text",
                                    "text": "2021/02/27 (六)",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5
                                  }
                                ]
                              }
                            ]
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                              "type": "uri",
                              "label": "手刀報名去",
                              "uri": "https://www.surveycake.com/s/PQDDM"
                            }
                          },
                          {
                            "type": "spacer",
                            "size": "sm"
                          }
                        ],
                        "flex": 0
                      },
                      "styles": {
                        "header": {
                          "separator": False
                        }
                      }
                    }
                    line_bot_api.reply_message(
                        event.reply_token,
                        FlexSendMessage(
                            alt_text="手刀報名去",
                            contents=content
                        )
                    )
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
