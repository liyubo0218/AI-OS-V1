from sync.sync_gateway import SyncGateway

from sync.sync_event import SyncEvent



gateway = SyncGateway()



event = SyncEvent(
    "evt_001",
    "user_input",
    {
        "text":"测试同步"
    }
)



print(
    gateway.receive_event(
        event
    )
)



print("Sync Gateway Ready")



print(
    gateway.sync()
)
