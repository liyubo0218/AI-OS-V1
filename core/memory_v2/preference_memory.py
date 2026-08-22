class PreferenceMemory:


    def __init__(self):

        self.preferences = {}


    def save(
        self,
        user_id,
        preference
    ):

        self.preferences[user_id] = preference

        return {
            "status": "saved"
        }


    def get(
        self,
        user_id
    ):

        return self.preferences.get(
            user_id,
            {}
        )
