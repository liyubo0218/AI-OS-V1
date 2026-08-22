class UserProfileModel:


    def __init__(self):

        self.profile = {}



    def update(
        self,
        key,
        value
    ):

        self.profile[key] = value


        return {
            "status": "updated"
        }



    def get(
        self,
        key
    ):

        return self.profile.get(
            key
        )
