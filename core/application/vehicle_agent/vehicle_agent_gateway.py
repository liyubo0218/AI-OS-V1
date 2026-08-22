class VehicleAgentGateway:

    def __init__(self):
        self.name = "vehicle_agent"


    def create_request(
        self,
        user_input
    ):
        return {
            "request_id": "vehicle_req_001",
            "input": user_input,
            "source": self.name
        }


    def provide_capability(self):
        return {
            "capability": [
                "vehicle_status",
                "climate_control",
                "navigation",
                "charging"
            ]
        }


    def provide_permission(self):
        return {
            "permission": {
                "climate_control": True,
                "navigation": True
            }
        }


    def handle_response(
        self,
        response
    ):
        return {
            "status": response["status"],
            "result": response["result"]
        }
