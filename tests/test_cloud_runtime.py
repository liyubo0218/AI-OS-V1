from runtime.runtime_manager import RuntimeManager

from runtime.task_runtime import TaskRuntime



runtime = RuntimeManager()



print("Runtime Started")


print(
    runtime.start_runtime()
)



task = TaskRuntime(
    "task_001"
)


print("Task:")


print(
    runtime.run_task(
        task
    )
)



print("App Disconnect")


print(
    {
        "device":"iphone_001",
        "status":"offline"
    }
)



print("Runtime Status:")


print(
    runtime.get_status()
)
