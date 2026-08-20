class ConflictResolver:


    def resolve(
        self,
        local,
        cloud
    ):

        return {
            "source":"cloud",
            "result":cloud
        }
