from local_runtime.local_runtime import LocalRuntime

from local_runtime.device_agent import LocalDeviceAgent



device = LocalDeviceAgent(
    "iPhone"
)



runtime = LocalRuntime(
    device
)



print("Local Runtime Ready")



print(
    runtime.run_local_task(
        "camera_access"
    )
)



print(
    runtime.queue_cloud_task(
        {
            "type":"user_input",
            "text":"测试云端任务"
        }
    )
)

