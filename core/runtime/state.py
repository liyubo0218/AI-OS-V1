class RuntimeState:
    """
    AI-OS Runtime 状态模型

    负责：
    - 保存系统运行状态
    - 提供状态读取

    不负责：
    - 用户记忆
    - AI推理
    - 任务管理
    """

    def __init__(
        self
    ):
        self.state = {
            "status": "stopped",
            "current_task": None,
            "last_request": None,
            "last_result": None
        }


    def update(
        self,
        key,
        value
    ):
        self.state[key] = value

        return True


    def get(
        self,
        key=None
    ):
        if key:
            return self.state.get(
                key
            )

        return self.state


    def reset(
        self
    ):
        self.state = {
            "status": "stopped",
            "current_task": None,
            "last_request": None,
            "last_result": None
        }

        return True
