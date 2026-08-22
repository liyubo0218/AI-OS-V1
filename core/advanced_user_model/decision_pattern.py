class DecisionPattern:


    def __init__(self):

        self.patterns = []



    def record(
        self,
        decision
    ):

        self.patterns.append(
            decision
        )


        return {
            "status": "recorded"
        }



    def list_patterns(
        self
    ):

        return self.patterns
