class DeviationDetector:


    def check(
        self,
        goal
    ):


        if goal is None:

            return {
                "deviation": False
            }


        if goal.get("progress", 0) == 0:

            return {
                "deviation": True
            }


        return {
            "deviation": False
        }
