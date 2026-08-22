from .service_registry import ServiceRegistry



class ServiceManager:


    def __init__(self):

        self.registry = ServiceRegistry()



    def add_service(
        self,
        name,
        service
    ):

        return self.registry.register(
            name,
            service
        )



    def get_service(
        self,
        name
    ):

        return self.registry.get(
            name
        )
