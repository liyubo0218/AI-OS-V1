class BrainRequest:

    def __init__(
        self,
        request_id,
        user_input,
        source="unknown",
        session_id=None,
        context=None
    ):
        self.request_id = request_id
        self.user_input = user_input
        self.source = source
        self.session_id = session_id
        self.context = context or {}

    def to_dict(self):

        return {
            "request_id": self.request_id,
            "user_input": self.user_input,
            "source": self.source,
            "session_id": self.session_id,
            "context": self.context
        }
