class ContextCollector:


    def __init__(self):

        self.contexts = []



    def collect(
        self,
        environment,
        data
    ):

        context = {

            "environment": environment,

            "data": data

        }


        self.contexts.append(
            context
        )


        return context



    def list_contexts(
        self
    ):

        return self.contexts
