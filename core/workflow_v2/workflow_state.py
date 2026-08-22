class WorkflowState:


    def __init__(self):

        self.state = "created"



    def update(
        self,
        state
    ):

        self.state = state

        return self.state



    def get(
        self
    ):

        return self.state
