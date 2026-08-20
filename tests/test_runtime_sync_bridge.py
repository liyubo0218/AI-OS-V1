from runtime.local import LocalRuntime

from runtime.cloud import CloudRuntime

from runtime.sync_bridge import RuntimeSyncBridge



local = LocalRuntime()

cloud = CloudRuntime()



local.start()

cloud.start()



bridge = RuntimeSyncBridge(

    local,

    cloud

)



print(
    "===== Runtime Sync Bridge Ready ====="
)



print(
    "Local Task:"
)

local.add_task(

    "camera_task"

)


print(

    local.get_status()

)



print(
    "Sync To Cloud:"
)

print(

    bridge.sync_task(

        "camera_task"

    )

)



print(

    cloud.get_status()

)



print(
    "Cloud Result:"
)

print(

    bridge.sync_result(

        "camera_completed"

    )

)



print(

    local.get_status()

)



print(
    "===== Sync Bridge PASS ====="
)

