from abc import ABC, abstractmethod
from linebot.models import *

class Message(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def content(self):
        pass


class WeddingRegistrationMessage(Message):

    def content(self):
        return {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://upload.cc/i1/2020/12/13/g5FyIj.jpg",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": "https://upload.cc/i1/2020/12/13/g5FyIj.jpg"
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

class TrafficLocationMessage(Message):

    def content(self):
        return {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "搭乘大眾運輸",
                                "size": "xl"
                            }
                        ]
                    },
                    "hero": {
                        "type": "image",
                        "url": "https://upload.cc/i1/2020/12/13/Wk3u15.jpg",
                        "size": "full"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "搭捷運/公車",
                                    "data": "taken_by_metro_and_bus"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "接駁車",
                                    "data": "taken_by_shuttle"
                                }
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "自行開車前往",
                                "size": "xl"
                            }
                        ]
                    },
                    "hero": {
                        "type": "image",
                        "url": "https://upload.cc/i1/2020/12/13/Wb6BCc.jpg",
                        "size": "full"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "導航地圖",
                                    "data": "location_map"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "停車資訊",
                                    "data": "park_info"
                                }
                            }
                        ]
                    }
                }
            ]
        }

class ShuttleBusMessage(Message):
    def content(self):
        return {
            "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://upload.cc/i1/2020/12/13/9kRd7I.jpg",
                    "size": "full",
                    "margin": "sm",
                    "align": "center",
                    "position": "absolute"
                }
        }

class MetroAndBusMessage(Message):
    def content(self):
        return {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://upload.cc/i1/2020/12/13/qQ3Rgw.jpg",
                "size": "full",
                "margin": "sm",
                "align": "center",
                "position": "absolute"
            }
        }

if __name__ == '__main__':
    w = WeddingRegistrationMessage()
    print(w.content())
    t = TrafficLocationMessage()
    print(t.content())