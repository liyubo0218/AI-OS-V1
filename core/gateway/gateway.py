class Gateway:

    def __init__(self):
        self.devices = {}
        self.requests = {}


    def register_device(
        self,
        device
    ):

        if not device:
            return {
                "status": "failed",
                "reason": "invalid_device"
            }


        device_id = device.get(
            "device_id"
        )

        self.devices[device_id] = {
            "device_id": device_id,
            "device_type": device.get(
                "device_type",
                ""
            ),
            "status": device.get(
                "status",
                "offline"
            )
        }


        return {
            "device_id": device_id,
            "registered": True
        }


    def send_request(
        self,
        device_id,
        request
    ):

        if device_id not in self.devices:
            return {
                "status": "device_unavailable"
            }


        request_id = (
            f"request_{len(self.requests)+1:03d}"
        )


        self.requests[request_id] = {
            "request_id": request_id,
            "device_id": device_id,
            "request": request,
            "status": "sent"
        }


        return {
            "request_id": request_id,
            "status": "sent"
        }


    def get_device_status(
        self,
        device_id
    ):

        device = self.devices.get(
            device_id
        )

        if not device:
            return {
                "status": "not_found"
            }


        return device


    def handle_response(
        self,
        response
    ):

        request_id = response.get(
            "request_id"
        )

        if request_id not in self.requests:
            return {
                "processed": False
            }


        self.requests[request_id][
            "response"
        ] = response

        self.requests[request_id][
            "status"
        ] = response.get(
            "status",
            "completed"
        )


        return {
            "processed": True
        }
