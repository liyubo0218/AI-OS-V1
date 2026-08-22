class ServiceFeedback:


    def __init__(self):

        self.results = []



    def record(
        self,
        result
    ):

        self.results.append(
            result
        )


        return {
            "status": "recorded"
        }



    def latest(
        self
    ):

        if not self.results:

            return None


        return self.results[-1]
