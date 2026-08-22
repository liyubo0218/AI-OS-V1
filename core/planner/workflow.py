class Workflow:


    def __init__(
        self,
        steps=None
    ):

        self.steps = steps or []


    def add_step(
        self,
        step
    ):

        self.steps.append(step)


    def to_dict(self):

        return {
            "steps": self.steps
        }
