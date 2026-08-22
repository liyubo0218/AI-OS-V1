class HistoryMemory:


    def __init__(self):

        self.history = []


    def save(
        self,
        record
    ):

        self.history.append(
            record
        )

        return {
            "status": "saved"
        }


    def get_all(self):

        return self.history
