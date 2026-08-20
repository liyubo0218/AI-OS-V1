from runtime.background_worker import BackgroundWorker



class RuntimeManager:


    def __init__(
        self,
        event_publisher=None
    ):

        self.status = "inactive"

        self.worker = BackgroundWorker()

        self.event_publisher = event_publisher



    def start_runtime(self):

        self.status = "active"


        return {
            "runtime":"active"
        }



    def run_task(
        self,
        task
    ):

        result = self.worker.run(
            task
        )


        if self.event_publisher:


            self.event_publisher.publish_task_result(

                task.task_id,

                result

            )


        return result



    def get_status(self):

        return {
            "runtime":self.status
        }
