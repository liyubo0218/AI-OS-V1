class RuntimeState:

    IDLE = "IDLE"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    VALID_STATES = {
        IDLE,
        RUNNING,
        COMPLETED,
        FAILED
    }


    def __init__(self):
        self.current = self.IDLE


    def set_state(
        self,
        state
    ):
        if state not in self.VALID_STATES:
            self.current = self.FAILED

            return {
                "status": "failed",
                "state": self.current
            }

        self.current = state

        return {
            "status": "updated",
            "state": self.current
        }


    def get_state(self):
        return self.current
