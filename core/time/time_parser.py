from datetime import datetime, timedelta


class TimeParser:
    """
    AI-OS 时间解析层

    负责：
    - 解析基础时间表达
    - 转换标准 deadline

    不负责：
    - 任务创建
    - 提醒发送
    - 日历同步
    """

    def parse(
        self,
        text
    ):
        now = datetime.now()

        result = {
            "deadline": None
        }

        target = now

        if "明天" in text:
            target = target + timedelta(
                days=1
            )

        elif "今天" in text:
            target = now

        hour = None

        if "上午" in text:
            hour = 9

        elif "下午" in text:
            hour = 15

        elif "晚上" in text:
            hour = 20

        if "点" in text:
            try:
                before = text.split(
                    "点"
                )[0]

                number = ""

                for char in reversed(before):
                    if char.isdigit():
                        number = char + number
                    else:
                        break

                if number:
                    hour = int(number)

            except Exception:
                pass

        if hour is not None:
            target = target.replace(
                hour=hour,
                minute=0,
                second=0,
                microsecond=0
            )

            result["deadline"] = (
                target.isoformat()
            )

        return result
