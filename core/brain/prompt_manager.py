class PromptManager:
    """
    AI-OS Prompt管理层

    负责：
    - 管理秘书角色
    - 构建LLM输入

    不负责：
    - AI推理
    - 任务执行
    """

    def __init__(
        self
    ):
        self.system_role = (
            "你是AI-OS私人秘书，"
            "负责理解用户目标，"
            "调用系统能力协助用户。"
        )


    def get_role(
        self
    ):
        return self.system_role


    def build(
        self,
        user_input,
        context=None
    ):
        return {
            "system": self.system_role,
            "user": user_input,
            "context": context or {}
        }


    def task_prompt(
        self,
        task_type,
        content
    ):
        return {
            "task_type": task_type,
            "instruction": content,
            "role": self.system_role
        }


    def update_role(
        self,
        role
    ):
        self.system_role = role

        return True
