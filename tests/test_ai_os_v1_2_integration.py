from core.brain.context.brain_adapter import BrainAdapter
from core.memory_v2 import MemoryEngine
from core.workflow_v2 import WorkflowEngine
from core.extension_runtime_v2 import (
    ExtensionRegistry,
    LifecycleManager,
    RuntimeStatus
)
from core.device_connector import ConnectorManager
from core.goal_v2 import ActiveGoalMonitor


def test_ai_os_v1_2_integration():


    # 1. Understand User

    brain = BrainAdapter()

    result = brain.understand(
        "帮我完成项目任务"
    )

    assert result["goal"] == "general_task"



    # 2. Memory

    memory = MemoryEngine()

    memory.save_history(
        {
            "task": "project task",
            "status": "new"
        }
    )

    memories = memory.search(
        "project"
    )

    assert len(memories) == 1



    # 3. Workflow Engine 2.0

    workflow = WorkflowEngine()

    created = workflow.create_workflow(
        [
            "plan",
            "execute"
        ]
    )

    assert created["status"] == "created"


    completed = workflow.run()

    assert completed["status"] == "completed"



    # 4. Extension Runtime 2.0

    registry = ExtensionRegistry()

    lifecycle = LifecycleManager()

    status = RuntimeStatus()


    registry.register(
        "task_extension",
        {}
    )

    lifecycle.start(
        "task_extension"
    )

    status.update(
        "task_extension",
        "running"
    )


    assert status.get(
        "task_extension"
    ) == "running"



    # 5. Device Connector

    connector = ConnectorManager()


    connector.add_device(
        "computer",
        {
            "type": "pc"
        }
    )


    connection = connector.connect(
        "computer"
    )


    assert connection["status"] == "connected"



    # 6. Goal Monitor

    monitor = ActiveGoalMonitor()


    monitor.create_goal(
        "001",
        "完成项目任务"
    )


    monitor.tracker.update_progress(
        "001",
        100
    )


    goal_status = monitor.monitor_goal(
        "001"
    )


    assert goal_status["deviation"]["deviation"] is False



    print(
        "AI-OS V1.2 INTEGRATION PASS"
    )


if __name__ == "__main__":

    test_ai_os_v1_2_integration()
