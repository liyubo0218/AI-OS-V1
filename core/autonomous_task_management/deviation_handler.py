class DeviationHandler:


    def handle(
        self,
        status
    ):


        if status == "delayed":

            return {
                "action": "remind"
            }


        return {
            "action": "continue"
        }
