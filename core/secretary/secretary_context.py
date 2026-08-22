class SecretaryContext:
    """
    AI-OS 私人秘书上下文整理器

    负责：
    - 统一用户请求上下文
    - 整理设备来源信息
    - 合并记忆上下文

    不负责：
    - 模型推理
    - 数据保存
    - 手机执行
    """

    def build(
        self,
        request,
        memory_context=None,
        device_context=None,
        task_context=None
    ):
        return {
            "user_input": request.get(
                "user_input",
                ""
            ),
            "source": request.get(
                "source",
                "unknown"
            ),
            "memory_context": (
                memory_context
                or {}
            ),
            "device_context": (
                device_context
                or {}
            ),
            "task_context": (
                task_context
                or {}
            )
        }
