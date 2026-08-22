class LanguageParser:


    def parse(
        self,
        text
    ):

        keywords = []


        for word in [
            "提醒",
            "通知",
            "明天",
            "今天",
            "会议",
            "开会",
            "任务"
        ]:

            if word in text:

                keywords.append(word)


        return {
            "text": text,
            "keywords": keywords
        }
