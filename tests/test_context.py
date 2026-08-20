from core.context.context_manager import ContextManager


context = ContextManager()

result = context.create_context(
    "帮我测试AI-OS"
)

print(result)

context.update_context(
    {
        "task_state": "planned"
    }
)

print(
    context.get_context()
)
