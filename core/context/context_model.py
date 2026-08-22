from datetime import datetime


class ContextModel:


    def __init__(
        self,
        user=None,
        task=None
    ):

        self.user = user

        self.task = task

        self.created_at = datetime.utcnow()


    def to_dict(self):

        return {

            "user": self.user,

            "task": self.task,

            "created_at":
                self.created_at.isoformat()

        }
