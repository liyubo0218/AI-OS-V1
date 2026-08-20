class MockConnector:


    def send(
        self,
        request
    ):

        return {
            "response":
            "Mock ChatGPT Response: "
            + request.user_input
        }
