from .brain_state import BrainState


class BrainController:


    def __init__(self):

        self.state = BrainState.IDLE


    def process(
        self,
        user_input
    ):

        self.state = BrainState.ANALYZING


        result = {
            "status": "received",
            "input": user_input,
            "state": self.state.value
        }


        self.state = BrainState.COMPLETED


        result["final_state"] = self.state.value


        return result


    def get_state(self):

        return self.state.value
