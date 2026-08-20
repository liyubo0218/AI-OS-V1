class RuntimeOrchestrator:


    def __init__(
        self,
        runtime_router
    ):

        self.runtime_router = runtime_router



    def execute(
        self,
        task
    ):


        route = self.runtime_router.route(

            task

        )


        if route["runtime"] == "local":


            return {

                "status":
                "completed",

                "runtime":
                "local",

                "task":
                task

            }



        if route["runtime"] == "cloud":


            return {

                "status":
                "completed",

                "runtime":
                "cloud",

                "task":
                task

            }



        return {

            "status":
            "unknown"

        }

