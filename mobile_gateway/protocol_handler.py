from mobile_protocol.response import MobileResponse


class ProtocolHandler:


    def __init__(
        self,
        mobile_gateway
    ):

        self.mobile_gateway = mobile_gateway



    def handle(
        self,
        request
    ):


        user_input = request.payload.get(
            "text",
            ""
        )


        result = self.mobile_gateway.handle_request(
            {
                "user_input":
                user_input
            }
        )


        return MobileResponse(

            request.request_id,

            "success",

            result

        )
