from core.brain.context.brain_adapter import BrainAdapter
from core.memory_v2 import MemoryEngine
from core.workflow_intelligence import (
    TaskAnalyzer,
    StrategySelector,
    WorkflowOptimizer
)
from core.workflow_v2 import WorkflowEngine
from core.device_capability import (
    CapabilityManager,
    CapabilityExecutor
)
from core.external_integration import (
    ServiceManager,
    ServiceExecutor,
    ServiceFeedback
)
from core.goal_v2 import ActiveGoalMonitor



def test_ai_os_v1_3_integration():


    # 1. User Understanding

    brain = BrainAdapter()

    goal = brain.understand(
        "完成项目任务"
    )

    assert goal["goal"] == "general_task"



    # 2. Memory

    memory = MemoryEngine()

    memory.save_history(
        {
            "task": "project",
            "status": "start"
        }
    )


    assert len(
        memory.search("project")
    ) == 1



    # 3. Workflow Intelligence

    analyzer = TaskAnalyzer()

    analysis = analyzer.analyze(
        "完成项目任务"
    )


    strategy = StrategySelector().select(
        analysis
    )


    optimized = WorkflowOptimizer().optimize(
        [
            "plan",
            "execute"
        ]
    )


    assert strategy["strategy"] == "step_execution"

    assert optimized["optimized"] is True



    # 4. Workflow Engine

    workflow = WorkflowEngine()


    workflow.create_workflow(
        [
            "plan",
            "execute"
        ]
    )


    result = workflow.run()


    assert result["status"] == "completed"



    # 5. Device Capability

    capability = CapabilityManager()

    executor = CapabilityExecutor()


    capability.add_capability(
        "computer",
        {
            "type": "desktop"
        }
    )


    capability.enable(
        "computer"
    )


    device_result = executor.execute(
        "computer"
    )


    assert device_result["status"] == "executed"



    # 6. External Service

    service = ServiceManager()

    service_executor = ServiceExecutor()

    feedback = ServiceFeedback()


    service.add_service(
        "calendar",
        {
            "type": "schedule"
        }
    )


    service_result = service_executor.execute(
        service.get_service("calendar")
    )


    feedback.record(
        service_result
    )


    assert feedback.latest() == service_result



    # 7. Goal Monitor

    monitor = ActiveGoalMonitor()


    monitor.create_goal(
        "001",
        "完成项目任务"
    )


    monitor.tracker.update_progress(
        "001",
        100
    )


    status = monitor.monitor_goal(
        "001"
    )


    assert status["deviation"]["deviation"] is False



    print(
        "AI-OS V1.3 INTEGRATION PASS"
    )



if __name__ == "__main__":

    test_ai_os_v1_3_integration()
