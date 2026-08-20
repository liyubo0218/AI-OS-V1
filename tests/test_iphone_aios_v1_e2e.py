from mobile_protocol.request import MobileRequest

from mobile_gateway.protocol_handler import ProtocolHandler

from mobile_gateway.gateway import MobileGateway

from sync.sync_gateway import SyncGateway


from local_runtime.local_runtime import LocalRuntime

from local_runtime.device_agent import LocalDeviceAgent

from local_runtime.offline_queue import OfflineQueue

from local_runtime.sync_bridge import LocalSyncBridge



print("===== iPhone AI-OS V1 E2E =====")



# =========================
# Online Mode
# =========================

print("\n[Online Mode]")


sync_gateway = SyncGateway()



class DemoOrchestrator:


    def run(
        self,
        user_input
    ):

        return {

            "status":"completed",

            "task":user_input

        }



mobile_gateway = MobileGateway(

    DemoOrchestrator(),

    sync_gateway

)



handler = ProtocolHandler(
    mobile_gateway
)



request = MobileRequest(

    "iphone_req_001",

    "iphone_session_001",

    "task_request",

    {
        "text":"在线测试AI-OS"
    }

)



response = handler.handle(
    request
)



print(
    response.to_dict()
)



# =========================
# Offline Mode
# =========================

print("\n[Offline Mode]")


device_agent = LocalDeviceAgent(
    "iPhone"
)



local_runtime = LocalRuntime(
    device_agent
)



print(
    local_runtime.run_local_task(
        "camera_access"
    )
)



queue = local_runtime.queue



print(
    queue.add(
        {
            "type":"user_input",
            "text":"离线任务"
        }
    )
)



# =========================
# Sync Recovery
# =========================

print("\n[Sync Recovery]")


bridge = LocalSyncBridge(

    sync_gateway,

    queue

)



print(
    bridge.sync_pending_events()
)



print(
    sync_gateway.sync()
)



print("\n===== iPhone AI-OS V1 Completed =====")

