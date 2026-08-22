class SyncManager:


    def __init__(self):

        self.status = {}



    def sync(
        self,
        task,
        result
    ):

        self.status[task] = result


        return {

            "status": "synced"

        }



    def get(
        self,
        task
    ):

        return self.status.get(
            task
        )
