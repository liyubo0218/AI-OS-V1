class GoalAutonomyManager:

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


    def update_progress(
        self,
        goal_id,
        progress
    ):
        if goal_id not in self.goals:
            return {
                "status": "failed",
                "result": "goal_not_found"
            }

        self.goals[goal_id]["progress"] = progress

        if progress >= 1:
            self.goals[goal_id]["status"] = "completed"
        else:
            self.goals[goal_id]["status"] = "in_progress"

        return self.goals[goal_id]


    def get_goal(
        self,
        goal_id
    ):
        return self.goals.get(goal_id)


    def check_deviation(
        self,
        goal_id
    ):
        goal = self.goals.get(goal_id)

        if goal is None:
            return {
                "deviation": True
            }

        return {
            "goal_id": goal_id,
            "deviation": False,
            "feedback": "执行符合目标"
        }
