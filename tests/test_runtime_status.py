from runtime.manager import RuntimeManager



runtime = RuntimeManager()



print("AI-OS Runtime Ready")



print(
    runtime.get_status()
)



runtime.start()



runtime.update_task(

    "测试任务"

)



print(
    runtime.get_status()
)

