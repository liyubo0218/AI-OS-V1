class DeviationPredictor:


    def predict(
        self,
        progress
    ):


        if progress < 50:

            return {

                "deviation": True

            }


        return {

            "deviation": False

        }
