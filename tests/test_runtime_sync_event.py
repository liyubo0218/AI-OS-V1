from runtime.event_publisher import RuntimeEventPublisher

from sync.sync_gateway import SyncGateway



sync_gateway = SyncGateway()



publisher = RuntimeEventPublisher(
    sync_gateway
)



result = publisher.publish_task_result(

    "task_001",

    {
        "status":"completed",
        "message":"AI-OS任务完成"
    }

)



print("Runtime Sync Event Ready")

print(result)



print(
    sync_gateway.sync()
)
