class StatusPredictor:


    def predict(
        self,
        progress
    ):


        if progress >= 100:

            return {
                "status": "completed"
            }


        return {
            "status": "in_progress"
        }
