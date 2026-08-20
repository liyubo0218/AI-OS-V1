class CloudRuntime:


    def __init__(self):

        self.status = "inactive"

        self.tasks = []



    def start(
        self
    ):

        self.status = "active"



    def add_task(
        self,
        task
    ):

        self.tasks.append(task)



    def get_status(
        self
    ):

        return {

            "runtime":
            "cloud",

            "status":
            self.status,

            "tasks":
            self.tasks

        }

