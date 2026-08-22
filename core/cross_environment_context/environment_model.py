class EnvironmentModel:


    def __init__(self):

        self.environments = {}



    def update(
        self,
        name,
        state
    ):

        self.environments[name] = state


        return {

            "status": "updated"

        }



    def get(
        self,
        name
    ):

        return self.environments.get(
            name
        )
