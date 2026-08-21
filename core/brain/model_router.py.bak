class ModelRouter:

    def __init__(
        self,
        default_adapter=None
    ):

        self.default_adapter = default_adapter


    def route(
        self,
        prompt,
        context=None
    ):

        if self.default_adapter:

            return self.default_adapter.generate(
                prompt,
                context
            )


        return {
            "text": "",
            "model": "none",
            "confidence": 0,
            "status": "unavailable"
        }
