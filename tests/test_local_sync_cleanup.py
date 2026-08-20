from local_runtime.offline_queue import OfflineQueue

from local_runtime.sync_bridge import LocalSyncBridge

from sync.sync_gateway import SyncGateway



queue = OfflineQueue()



queue.add(
    {
        "type":"user_input",
        "text":"测试清理队列"
    }
)



print("Queue Before Sync:")

print(
    queue.size()
)



gateway = SyncGateway()



bridge = LocalSyncBridge(
    gateway,
    queue
)



print("Sync Result:")

print(
    bridge.sync_pending_events()
)



print("Queue After Sync:")

print(
    queue.size()
)

