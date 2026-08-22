class ContextManager:


    def __init__(self):

        self.active = None



    def activate(
        self,
        context
    ):

        self.active = context


        return {

            "status": "activated"

        }



    def current(
        self
    ):

        return self.active
