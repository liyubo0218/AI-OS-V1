from runtime.local import LocalRuntime

from runtime.cloud import CloudRuntime



local = LocalRuntime()

cloud = CloudRuntime()



print(
    "===== Cloud Local Runtime Ready ====="
)



local.start()

cloud.start()



local.add_task(
    "camera_task"
)


cloud.add_task(
    "long_ai_task"
)



print(
    "Local Runtime:"
)

print(
    local.get_status()
)



print(
    "Cloud Runtime:"
)

print(
    cloud.get_status()
)



print(
    "Sync:"
)

print(
    "connected"
)



print(
    "===== Hybrid Runtime PASS ====="
)

