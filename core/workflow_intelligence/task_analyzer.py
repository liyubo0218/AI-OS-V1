class TaskAnalyzer:


    def analyze(
        self,
        task
    ):


        if "完成" in task:

            return {
                "type": "execution",
                "complexity": "normal"
            }


        return {
            "type": "general",
            "complexity": "simple"
        }
