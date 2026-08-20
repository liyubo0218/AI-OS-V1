import os

from sync.gateway import SyncGateway

from sync.storage import SyncStorage



file = "test_sync_events.json"



if os.path.exists(file):

    os.remove(file)



gateway = SyncGateway(

    SyncStorage(file)

)



print(
    "Sync Persistence Ready"
)



print(

    gateway.store_event(

        "task_update",

        {
            "task":
            "offline_test"
        }

    )

)



print(
    "Before Restart:"
)

print(

    gateway.get_events()

)



# 模拟重新启动

new_gateway = SyncGateway(

    SyncStorage(file)

)



print(
    "After Restart:"
)

print(

    new_gateway.get_events()

)



print(
    "Recovery PASS"
)


