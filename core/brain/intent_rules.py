
INTENT_RULES = {

    "reminder": [
        "提醒",
        "通知"
    ],

    "task": [
        "任务",
        "完成"
    ],

    "query": [
        "查询",
        "查看"
    ]
}


def match_intent(text):

    for intent, keywords in INTENT_RULES.items():

        for keyword in keywords:

            if keyword in text:

                return intent


    return "unknown"
