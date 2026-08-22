class HabitTracker:


    def __init__(self):

        self.habits = []



    def record(
        self,
        habit
    ):

        self.habits.append(
            habit
        )


        return {
            "status": "recorded"
        }



    def list_habits(
        self
    ):

        return self.habits
