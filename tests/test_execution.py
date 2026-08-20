from execution.execution_engine import ExecutionEngine


engine = ExecutionEngine()


plan = {
    "task_id": "task_001",
    "goal": "帮我测试AI-OS",
    "steps": [
        "分析任务",
        "执行测试",
        "返回结果"
    ],
    "status": "ready"
}


result = engine.execute(plan)


print("Execution Engine Ready")

print("Status:")
print(result["status"])

print("Completed Steps:")
for step in result["completed_steps"]:
    print(step)

print("Result:")
print(result["result"])
