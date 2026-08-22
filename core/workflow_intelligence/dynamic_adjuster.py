class DynamicAdjuster:


    def adjust(
        self,
        workflow,
        result
    ):


        if result == "failed":

            return {
                "action": "retry"
            }


        return {
            "action": "continue"
        }
