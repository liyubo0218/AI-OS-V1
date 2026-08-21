class LLMGateway:

    def __init__(
        self,
        adapter=None
    ):

        self.adapter = adapter


    def generate(
        self,
        prompt,
        context=None
    ):

        if self.adapter:

            return self.adapter.generate(
                prompt,
                context
            )


        return {
            "text": "",
            "model": "none",
            "confidence": 0,
            "status": "unavailable"
        }
