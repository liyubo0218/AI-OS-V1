class ExternalServiceManager:

    def __init__(self):
        self.services = {}


    def register_service(
        self,
        service_id,
        service
    ):

        self.services[service_id] = service

        return {
            "status": "registered"
        }


    def execute(
        self,
        service_id,
        action,
        context
    ):

        service = self.services.get(
            service_id
        )


        if service is None:
            return {
                "status": "failed",
                "error": "service_not_found"
            }


        result = service.execute(
            action,
            context
        )


        return {
            "status": "completed",
            "result": result
        }


    def get_status(
        self,
        service_id
    ):

        if service_id in self.services:
            return {
                "status": "available"
            }


        return {
            "status": "unavailable"
        }
