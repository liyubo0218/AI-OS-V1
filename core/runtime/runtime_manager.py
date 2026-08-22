from .runtime import Runtime


class RuntimeManager:
    """
    AI-OS Runtime 生命周期管理器

    负责：
    - 创建Runtime
    - 管理Runtime状态
    - 提供统一运行入口

    不负责：
    - AI推理
    - 任务执行
    - 手机控制
    """

    def __init__(
        self
    ):
        self.runtime = None


    def create_runtime(
        self,
        orchestrator=None
    ):
        self.runtime = Runtime(
            orchestrator
        )

        return self.runtime


    def get_runtime(
        self
    ):
        return self.runtime


    def start(
        self
    ):
        if not self.runtime:
            return {
                "status": "error",
                "message": "runtime unavailable"
            }

        return self.runtime.start()


    def stop(
        self
    ):
        if not self.runtime:
            return {
                "status": "error",
                "message": "runtime unavailable"
            }

        return self.runtime.stop()
