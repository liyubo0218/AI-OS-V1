class MemoryClassifier:

    def classify(
        self,
        content
    ):

        text = str(content)


        if any(
            word in text
            for word in [
                "喜欢",
                "偏好",
                "习惯",
                "经常"
            ]
        ):
            return {
                "type": "user",
                "confidence": 0.8
            }


        if any(
            word in text
            for word in [
                "任务",
                "完成",
                "执行",
                "结果"
            ]
        ):
            return {
                "type": "task",
                "confidence": 0.8
            }


        if any(
            word in text
            for word in [
                "目标",
                "计划",
                "进度"
            ]
        ):
            return {
                "type": "goal",
                "confidence": 0.8
            }


        return {
            "type": "context",
            "confidence": 0.5
        }
