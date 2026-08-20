from mobile_gateway.protocol_handler import ProtocolHandler

from mobile_protocol.request import MobileRequest

from mobile_gateway.gateway import MobileGateway

from sync.sync_gateway import SyncGateway



class DemoOrchestrator:


    def run(
        self,
        user_input
    ):

        return {
            "task":
            user_input,

            "status":
            "completed"
        }




sync_gateway = SyncGateway()



mobile_gateway = MobileGateway(

    DemoOrchestrator(),

    sync_gateway

)



handler = ProtocolHandler(

    mobile_gateway

)



request = MobileRequest(

    "req_001",

    "session_001",

    "task_request",

    {
        "text":
        "测试Mobile Protocol链路"
    }

)



response = handler.handle(
    request
)



print("Mobile Protocol Gateway Ready")

print(
    response.to_dict()
)
