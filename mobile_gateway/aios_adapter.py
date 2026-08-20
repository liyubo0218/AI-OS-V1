class MobileAIOSAdapter:


    def __init__(
        self,
        aios
    ):

        self.aios = aios



    def handle(
        self,
        request
    ):


        user_input = request.get(
            "text",
            ""
        )


        result = self.aios.run(
            user_input
        )


        return {

            "status":
            "success",

            "data":
            result

        }
