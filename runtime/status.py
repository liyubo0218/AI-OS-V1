class RuntimeStatus:


    def __init__(self):

        self.system = "stopped"

        self.task = "idle"

        self.session = None



    def start(self):

        self.system = "running"



    def stop(self):

        self.system = "stopped"



    def set_task(
        self,
        task
    ):

        self.task = task



    def set_session(
        self,
        session
    ):

        self.session = session



    def to_dict(
        self
    ):

        return {

            "system":
            self.system,

            "task":
            self.task,

            "session":
            self.session

        }
