class MobileGateway:

    def __init__(self):
        self.name = "mobile_gateway"
        self.routes = {}


    def register_agent(
        self,
        name,
        agent
    ):
        self.routes[name] = agent

        return {
            "status": "registered",
            "agent": name
        }


    def authenticate_device(
        self,
        device
    ):
        if (
            "device_id" in device
            and "permission_scope" in device
        ):
            return {
                "authenticated": True
            }

        return {
            "authenticated": False
        }


    def handle_request(
        self,
        request
    ):

        auth = self.authenticate_device(
            request.get("device", {})
        )

        if not auth["authenticated"]:
            return {
                "status": "failed",
                "error": "unauthorized_device"
            }


        target = request.get(
            "target"
        )

        agent = self.routes.get(
            target
        )

        if agent is None:
            return {
                "status": "failed",
                "error": "agent_not_found"
            }


        response = agent.execute(
            request.get("input")
        )


        return {
            "request_id": request["request_id"],
            "status": response["status"],
            "result": response["result"]
        }
