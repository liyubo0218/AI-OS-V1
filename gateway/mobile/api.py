class MobileAPI:


    def __init__(
        self,
        runtime=None
    ):

        self.runtime = runtime


    def handle(
        self,
        request
    ):

        if self.runtime is None:

            return {
                "status": "failed",
                "error": "runtime_not_connected"
            }


        return self.runtime.execute(
            request.to_dict()
        )
