from .api import MobileAPI


class MobileServer:


    def __init__(
        self,
        runtime=None
    ):

        self.api = MobileAPI(
            runtime
        )


    def receive(
        self,
        request
    ):

        return self.api.handle(
            request
        )
