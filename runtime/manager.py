from runtime.status import RuntimeStatus



class RuntimeManager:


    def __init__(self):

        self.status = RuntimeStatus()



    def start(
        self
    ):

        self.status.start()



    def update_task(
        self,
        task
    ):

        self.status.set_task(
            task
        )



    def get_status(
        self
    ):

        return self.status.to_dict()

