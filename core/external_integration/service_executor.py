class ServiceExecutor:


    def execute(
        self,
        service,
        request=None
    ):


        if service is None:

            return {
                "status": "failed"
            }


        return {

            "status": "executed",

            "service": service,

            "request": request

        }
