import re

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
                    txt_msg = TextMessage(text="籌備中，敬請期待" + chr(0x100078))
                    sticker_msg = StickerMessage(
                        package_id="11538", sticker_id="51626497"
                    )
                    line_bot_api.reply_message(
                        event.reply_token, [txt_msg, sticker_msg]
                    )
                elif event.message.text == "報名婚禮":
                    flex_msg = FlexSendMessage(
                        alt_text="手刀報名去",
                        contents=WeddingRegistrationMessage().content(),
                    )
                    txt_msg = TextMessage(
                        text="趕緊登記預留您的專屬貴賓座位喔。"
                        + chr(0x100080) * 3
                        + "\n也歡迎填寫表單留下祝福，我們也會收到您的心意喔！"
                        + chr(0x10007A) * 3
                    )
                    line_bot_api.reply_message(event.reply_token, [flex_msg, txt_msg])
                elif event.message.text == "交通資訊":
                    msg = FlexSendMessage(
                        alt_text="如何抵達白金花園酒店",
                        contents=TrafficLocationMessage().content(),
                    )
                    line_bot_api.reply_message(event.reply_token, msg)
                elif event.message.text in ["hi", "Hi", "HI", "hello", "Hello", "HELLO", "嗨", "哈囉", "安安", "你好", "您好"]:
                    msg = StickerMessage(package_id="11538", sticker_id="51626494")
                    line_bot_api.reply_message(event.reply_token, msg)
                elif event.message.text in ["恭喜", "congrats"]:
                    msg = StickerMessage(package_id="11537", sticker_id="52002752")
                    line_bot_api.reply_message(event.reply_token, msg)
                else:
                    msg = StickerMessage(package_id="11537", sticker_id="52002758")
                    line_bot_api.reply_message(event.reply_token, msg)

            elif isinstance(event, PostbackEvent):  # Post Back Event
                if event.postback.data == "taken_by_metro_and_bus":
                    txt_msg = TextMessage(
                        text="提醒您防疫期間搭乘大眾運輸請務必配戴口罩"
                        + chr(0x100020)
                        + "。\n不然阿中部長會森氣氣喔"
                        + chr(0x10001D)
                        + "~~"
                    )
                    img_msg = ImageSendMessage(
                        original_content_url="https://upload.cc/i1/2020/12/13/qQ3Rgw.jpg",
                        preview_image_url="https://upload.cc/i1/2020/12/13/qQ3Rgw.jpg",
                    )
                    line_bot_api.reply_message(event.reply_token, [txt_msg, img_msg])
                elif event.postback.data == "taken_by_shuttle":
                    txt_msg = TextMessage(
                        text="白金花園酒店目前提供給賓客的捷運接駁車時刻表如下，請大家務必準時上車"
                        + chr(0x100049)
                        + "，逾時不候"
                        + chr(0x10007C)
                        + "。\n希望您可以玩的盡興，感謝您的大駕光臨。"
                        + chr(0x100078) * 3
                    )
                    img_msg = ImageSendMessage(
                        original_content_url="https://upload.cc/i1/2020/12/13/9kRd7I.jpg",
                        preview_image_url="https://upload.cc/i1/2020/12/13/9kRd7I.jpg",
                    )
                    line_bot_api.reply_message(event.reply_token, [txt_msg, img_msg])
                elif event.postback.data == "location_map":
                    txt_msg = TextMessage(
                        text="導航資訊如下，點選下方連結並開啟Google地圖導航至飯店"
                        + chr(0x100049)
                        + "。\n\n"
                        + "提醒您開車不喝酒，喝酒不開車。德瑞克關心您～～"
                        + chr(0x100081) * 3
                    )
                    loc_msg = LocationMessage(
                        title="新店白金花園酒店",
                        address="新北市新店區安興路77號",
                        latitude=24.97505893694744,
                        longitude=121.51534850259982,
                    )
                    line_bot_api.reply_message(event.reply_token, [txt_msg, loc_msg])
                elif event.postback.data == "park_info":
                    msg = TextMessage(
                        text="本飯店設有全平面車位共130席。若停滿的話可至旁邊的「新店安坑停車場」停車。(共114席)"
                    )
                    line_bot_api.reply_message(event.reply_token, msg)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
