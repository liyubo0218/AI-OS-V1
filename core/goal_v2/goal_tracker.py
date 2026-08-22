class GoalTracker:


    def __init__(self):

        self.goals = {}


    def create_goal(
        self,
        goal_id,
        description
    ):

        self.goals[goal_id] = {

            "description": description,

            "progress": 0,

            "status": "created"

        }


        return {
            "status": "created"
        }



    def update_progress(
        self,
        goal_id,
        progress
    ):

        if goal_id not in self.goals:

            return {
                "status": "failed"
            }


        self.goals[goal_id]["progress"] = progress


        if progress >= 100:

            self.goals[goal_id]["status"] = "completed"

        else:

            self.goals[goal_id]["status"] = "running"


        return {
            "status": "updated"
        }



    def get_goal(
        self,
        goal_id
    ):

        return self.goals.get(
            goal_id
        )
