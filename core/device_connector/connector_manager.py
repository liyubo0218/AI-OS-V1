from .device_registry import DeviceRegistry
from .connection_status import ConnectionStatus



class ConnectorManager:


    def __init__(self):

        self.registry = DeviceRegistry()

        self.status = ConnectionStatus()



    def add_device(
        self,
        name,
        device
    ):

        return self.registry.register(
            name,
            device
        )



    def connect(
        self,
        name
    ):

        device = self.registry.get(
            name
        )


        if device is None:

            return {
                "status": "not_found"
            }


        self.status.update(
            name,
            "connected"
        )


        return {
            "status": "connected"
        }



    def get_status(
        self,
        name
    ):

        return self.status.get(
            name
        )
