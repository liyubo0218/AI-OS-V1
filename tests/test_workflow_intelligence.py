from core.workflow_intelligence import (
    TaskAnalyzer,
    StrategySelector,
    WorkflowOptimizer,
    DynamicAdjuster
)


def test_workflow_intelligence():


    analyzer = TaskAnalyzer()

    analysis = analyzer.analyze(
        "完成项目任务"
    )


    assert analysis["type"] == "execution"



    selector = StrategySelector()

    strategy = selector.select(
        analysis
    )


    assert strategy["strategy"] == "step_execution"



    optimizer = WorkflowOptimizer()

    result = optimizer.optimize(
        [
            "step1",
            "step2"
        ]
    )


    assert result["optimized"] is True



    adjuster = DynamicAdjuster()

    adjustment = adjuster.adjust(
        result,
        "failed"
    )


    assert adjustment["action"] == "retry"



    print(
        "Workflow Intelligence Layer PASS"
    )


if __name__ == "__main__":

    test_workflow_intelligence()
