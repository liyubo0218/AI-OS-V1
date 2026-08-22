class iPhoneAgentGateway:

    def __init__(self):
        self.name = "iphone_agent"


    def create_request(
        self,
        user_input
    ):
        return {
            "request_id": "req_001",
            "input": user_input,
            "source": self.name
        }


    def handle_response(
        self,
        response
    ):
        return {
            "status": response["status"],
            "result": response["result"]
        }
