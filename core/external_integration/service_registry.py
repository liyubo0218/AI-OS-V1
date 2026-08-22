class ServiceRegistry:


    def __init__(self):

        self.services = {}



    def register(
        self,
        name,
        service
    ):

        self.services[name] = service


        return {
            "status": "registered"
        }



    def get(
        self,
        name
    ):

        return self.services.get(
            name
        )
