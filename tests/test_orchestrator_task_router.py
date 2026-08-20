from core.orchestrator.task_router import TaskRouter



class DemoDevice:


    def execute(
        self,
        data
    ):

        return {
            "type":"device",
            "result":"camera executed"
        }



class DemoNormal:


    def execute(
        self,
        data
    ):

        return {
            "type":"normal",
            "result":"task executed"
        }



router = TaskRouter(

    DemoDevice(),

    DemoNormal()

)



print("Task Router Ready")



print(

    router.execute(

        {
            "goal":
            "帮我拍照"
        }

    )

)



print(

    router.execute(

        {
            "goal":
            "测试普通任务"
        }

    )

)

