class PreferenceAnalyzer:


    def analyze(
        self,
        data
    ):


        if "喜欢" in data:

            return {
                "preference": data,
                "identified": True
            }


        return {
            "preference": None,
            "identified": False
        }
