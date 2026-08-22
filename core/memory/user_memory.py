class UserMemory:


    def __init__(
        self,
        storage
    ):

        self.storage = storage


    def save_profile(
        self,
        user_id,
        profile
    ):

        return self.storage.save(
            f"user:{user_id}",
            profile
        )


    def get_profile(
        self,
        user_id
    ):

        return self.storage.get(
            f"user:{user_id}"
        )
