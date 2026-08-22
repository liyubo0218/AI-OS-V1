class LifecycleManager:


    def __init__(self):

        self.states = {}



    def start(
        self,
        name
    ):

        self.states[name] = "running"

        return {
            "status": "started"
        }



    def stop(
        self,
        name
    ):

        self.states[name] = "stopped"

        return {
            "status": "stopped"
        }
