class ProactiveEngine:
    """
    AI-OS Proactive Engine V1.8

    负责：
    - 判断是否需要用户关注
    - 生成建议

    不负责：
    - 创建任务
    - 执行任务
    - 修改目标
    """

    def check_attention(
        self,
        insight
    ):
        if insight.get(
            "state"
        ) in [
            "stalled",
            "stagnant"
        ]:

            return {
                "need_attention": True,
                "reason": "目标长期没有推进"
            }

        return {
            "need_attention": False,
            "reason": "目标状态正常"
        }


    def generate_suggestion(
        self,
        insight
    ):
        attention = self.check_attention(
            insight
        )

        if attention["need_attention"]:
            return {
                "suggestion":
                    "目标可能停滞，是否需要安排下一阶段任务？"
            }

        return {
            "suggestion":
                "目标正在正常推进"
        }
