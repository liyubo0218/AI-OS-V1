class MacAgentGateway:

    def __init__(self):
        self.name = "mac_agent"


    def create_request(
        self,
        user_input
    ):
        return {
            "request_id": "mac_req_001",
            "input": user_input,
            "source": self.name
        }


    def provide_capability(self):
        return {
            "capability": [
                "file_operation",
                "desktop_task_execution"
            ]
        }


    def handle_response(
        self,
        response
    ):
        return {
            "status": response["status"],
            "result": response["result"]
        }
