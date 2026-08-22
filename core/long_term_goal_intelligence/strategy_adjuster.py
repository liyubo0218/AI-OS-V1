class StrategyAdjuster:


    def suggest(
        self,
        deviation
    ):


        if deviation:

            return {

                "strategy": "adjust"

            }


        return {

            "strategy": "continue"

        }
