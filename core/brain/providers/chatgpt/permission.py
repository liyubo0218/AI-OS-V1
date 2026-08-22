class ChatGPTPermission:


    def check(
        self,
        request
    ):

        return {
            "allowed": True,
            "reason": "permission granted"
        }
