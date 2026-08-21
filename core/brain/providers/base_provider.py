class BaseProvider:

    def generate(
        self,
        prompt,
        context=None
    ):

        raise NotImplementedError(
            "Provider must implement generate()"
        )
