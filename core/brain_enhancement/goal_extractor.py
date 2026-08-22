class GoalExtractor:


    def extract(
        self,
        parsed
    ):

        keywords = parsed["keywords"]


        if "提醒" in keywords:

            return {
                "goal": "reminder_task"
            }


        if "任务" in keywords:

            return {
                "goal": "general_task"
            }


        return {
            "goal": "unknown"
        }
