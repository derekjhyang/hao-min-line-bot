from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from .message import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == "POST":
        signature = request.META["HTTP_X_LINE_SIGNATURE"]
        body = request.body.decode("utf-8")

        try:
            events = parser.parse(body, signature)  # parse the requested event
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if event.message.text == "婚紗輪播":
                    msg = StickerMessage(package_id="11538", sticker_id="51626497")
                    line_bot_api.reply_message(event.reply_token, msg)
                elif event.message.text == "報名婚禮":
                    msg = WeddingRegistrationMessage()
                    line_bot_api.reply_message(
                        event.reply_token,
                        FlexSendMessage(alt_text="手刀報名去", contents=msg.content()),
                    )
                elif event.message.text == "交通資訊":
                    msg = FlexSendMessage(
                        alt_text="如何抵達白金花園酒店",
                        contents=TrafficLocationMessage().content(),
                    )
                    line_bot_api.reply_message(event.reply_token, msg)
                else:
                    msg = StickerMessage(package_id="11537", sticker_id="52002758")
                    line_bot_api.reply_message(event.reply_token, msg)

            elif isinstance(event, PostbackEvent):  # Post Back Event
                if event.postback.data == "taken_by_metro_and_bus":
                    msg = ImageSendMessage(
                        original_content_url="https://upload.cc/i1/2020/12/13/qQ3Rgw.jpg",
                        preview_image_url="https://upload.cc/i1/2020/12/13/qQ3Rgw.jpg"
                    )
                    line_bot_api.reply_message(event.reply_token, msg)
                elif event.postback.data == "taken_by_shuttle":
                    msg = ImageSendMessage(
                        original_content_url="https://upload.cc/i1/2020/12/13/9kRd7I.jpg",
                        preview_image_url="https://upload.cc/i1/2020/12/13/9kRd7I.jpg"
                    )
                    line_bot_api.reply_message(event.reply_token, msg)
                elif event.postback.data == "location_map":
                    msg = LocationMessage(
                        title="新店白金花園酒店",
                        address="新北市新店區安興路77號",
                        latitude=24.97505893694744,
                        longitude=121.51534850259982,
                    )
                    line_bot_api.reply_message(event.reply_token, msg)
                elif event.postback.data == "park_info":
                    msg = TextMessage(
                        text="本飯店設有全平面車位共130席。若停滿的話可至旁邊的「新店安坑停車場」停車。(共114席)"
                    )
                    line_bot_api.reply_message(event.reply_token, msg)


        return HttpResponse()
    else:
        return HttpResponseBadRequest()
