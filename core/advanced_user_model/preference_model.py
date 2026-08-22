class PreferenceModel:


    def __init__(self):

        self.preferences = {}



    def update(
        self,
        key,
        value
    ):

        self.preferences[key] = value


        return {
            "status": "updated"
        }



    def get(
        self,
        key
    ):

        return self.preferences.get(
            key
        )
