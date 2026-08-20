from local_runtime.offline_queue import OfflineQueue

from local_runtime.sync_bridge import LocalSyncBridge

from sync.sync_gateway import SyncGateway



queue = OfflineQueue()



queue.add(

    {
        "type":"user_input",

        "text":
        "断网任务测试"
    }

)



sync_gateway = SyncGateway()



bridge = LocalSyncBridge(

    sync_gateway,

    queue

)



print("Offline Event Created")



print(
    bridge.sync_pending_events()
)



print("Sync Result:")



print(
    sync_gateway.sync()
)

