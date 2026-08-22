from datetime import datetime


class GoalModel:


    def __init__(
        self,
        goal
    ):

        self.goal = goal

        self.status = "created"

        self.created_at = datetime.utcnow()


    def update(
        self,
        status
    ):

        self.status = status


    def to_dict(self):

        return {
            "goal": self.goal,
            "status": self.status,
            "created_at":
                self.created_at.isoformat()
        }
