class ReminderEngine:


    def check(
        self,
        goal
    ):


        if goal is None:

            return {
                "reminder": False
            }


        if goal.get("deadline"):

            return {
                "reminder": True
            }


        return {
            "reminder": False
        }
