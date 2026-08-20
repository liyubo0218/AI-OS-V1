class ChatGPTResponse:

    def __init__(
        self,
        request_id,
        response,
        model="chatgpt-model"
    ):

        self.request_id = request_id

        self.model = model

        self.response = response

        self.confidence = 0.95



    def to_dict(self):

        return {
            "request_id": self.request_id,
            "model": self.model,
            "response": self.response,
            "confidence": self.confidence
        }
