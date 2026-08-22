class ChatGPTRequest:

    def __init__(
        self,
        request_id,
        user_input,
        context=None,
        mode="reasoning"
    ):

        self.request_id = request_id

        self.user_input = user_input

        self.context = context or {}

        self.mode = mode



    def to_dict(self):

        return {
            "request_id": self.request_id,
            "user_input": self.user_input,
            "context": self.context,
            "mode": self.mode
        }
