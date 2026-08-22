class RiskDetector:


    def detect(
        self,
        status
    ):


        if status == "delayed":

            return {

                "risk": True

            }


        return {

            "risk": False

        }
