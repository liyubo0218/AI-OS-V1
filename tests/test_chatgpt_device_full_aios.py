from core.agent.task_adapter import ChatGPTTaskAdapter

from core.workflow.full_workflow import ChatGPTDeviceWorkflow



class DemoOrchestrator:


    def execute_device_task(
        self,
        task
    ):

        return {

            "device":
            "iphone_001",

            "status":
            "completed",

            "result":
            "拍照完成"

        }



class DemoMemory:


    def save(
        self,
        type,
        content
    ):

        return {

            "status":
            "saved"

        }



class DemoGoal:


    pass



workflow = ChatGPTDeviceWorkflow(

    ChatGPTTaskAdapter(),

    DemoOrchestrator(),

    DemoMemory(),

    DemoGoal()

)



print("ChatGPT Full AI-OS Workflow Ready")



print(

    workflow.run(

        "帮我拍一张照片"

    )

)



print("===== Completed =====")

