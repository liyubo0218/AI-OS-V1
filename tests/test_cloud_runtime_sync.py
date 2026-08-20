from runtime.runtime_manager import RuntimeManager

from runtime.task_runtime import TaskRuntime

from runtime.event_publisher import RuntimeEventPublisher

from sync.sync_gateway import SyncGateway



sync_gateway = SyncGateway()



publisher = RuntimeEventPublisher(
    sync_gateway
)



runtime = RuntimeManager(
    publisher
)



print("Runtime Started")


print(
    runtime.start_runtime()
)



task = TaskRuntime(
    "task_001"
)



print("Task Running")


print(
    runtime.run_task(
        task
    )
)



print("Sync State:")


print(
    sync_gateway.sync()
)
