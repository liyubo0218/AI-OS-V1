class ContextInterpreter:


    def interpret(
        self,
        parsed
    ):

        keywords = parsed["keywords"]


        context = {}


        if "明天" in keywords:

            context["time"] = "tomorrow"


        if "今天" in keywords:

            context["time"] = "today"


        return context
