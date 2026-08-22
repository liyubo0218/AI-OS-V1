class Runtime:
    """
    AI-OS Runtime运行管理层

    负责：
    - 系统启动
    - 管理运行状态
    - 统一请求入口

    不负责：
    - AI推理
    - 手机控制
    - 任务规划
    """

    def __init__(
        self,
        orchestrator=None
    ):
        self.orchestrator = orchestrator
        self.status = "stopped"


    def start(
        self
    ):
        self.status = "running"

        return {
            "status": self.status
        }


    def stop(
        self
    ):
        self.status = "stopped"

        return {
            "status": self.status
        }


    def handle(
        self,
        user_input
    ):
        if self.status != "running":
            self.start()

        if not self.orchestrator:
            return {
                "status": "error",
                "message": "orchestrator unavailable"
            }

        return self.orchestrator.process(
            user_input
        )


    def get_status(
        self
    ):
        return {
            "status": self.status
        }

# AI-OS compatibility alias
# 保持旧接口兼容
RuntimeCore = Runtime
