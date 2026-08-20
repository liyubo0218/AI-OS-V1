class GoalMonitor:

    def __init__(self):

        self.goals = {}


    def create_goal(
        self,
        goal_id,
        goal
    ):

        self.goals[goal_id] = {

            "goal_id": goal_id,

            "goal": goal,

            "status": "created",

            "progress": 0
        }


        return self.goals[goal_id]



    def update_status(
        self,
        goal_id,
        status
    ):

        if goal_id in self.goals:

            self.goals[goal_id]["status"] = status


            if status == "completed":

                self.goals[goal_id]["progress"] = 100


            return self.goals[goal_id]


        return None



    def get_goal(
        self,
        goal_id
    ):

        return self.goals.get(
            goal_id
        )


    def get_all_goals(
        self
    ):

        return list(
            self.goals.values()
        )
