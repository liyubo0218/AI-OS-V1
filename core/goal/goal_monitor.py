from .goal_model import GoalModel


class GoalMonitor:


    def __init__(self):

        self.goals = {}


    def create_goal(
        self,
        goal_id,
        description
    ):

        self.goals[goal_id] = GoalModel(
            description
        )


        return {
            "status": "created"
        }


    def update_goal(
        self,
        goal_id,
        status
    ):

        goal = self.goals.get(
            goal_id
        )


        if goal is None:

            return {
                "status": "failed",
                "error": "goal_not_found"
            }


        goal.update(
            status
        )


        return {
            "status": "updated"
        }


    def get_goal(
        self,
        goal_id
    ):

        goal = self.goals.get(
            goal_id
        )


        if goal is None:

            return None


        return goal.to_dict()
