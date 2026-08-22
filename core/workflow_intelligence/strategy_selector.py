class StrategySelector:


    def select(
        self,
        analysis
    ):


        if analysis["complexity"] == "normal":

            return {
                "strategy": "step_execution"
            }


        return {
            "strategy": "direct_execution"
        }
