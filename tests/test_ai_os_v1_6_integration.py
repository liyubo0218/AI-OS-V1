from core.long_term_goal_intelligence import (
    GoalDecomposer,
    MilestoneTracker,
    DeviationPredictor,
    StrategyAdjuster
)

from core.cross_environment_context import (
    ContextCollector,
    EnvironmentModel,
    ContextSync,
    ContextManager
)

from core.decision_support_intelligence import (
    InformationAnalyzer,
    OptionComparator,
    RiskAnalyzer,
    RecommendationEngine
)


def test_ai_os_v1_6_integration():


    # 1. Long-Term Goal Intelligence

    decomposer = GoalDecomposer()
    tracker = MilestoneTracker()
    predictor = DeviationPredictor()
    adjuster = StrategyAdjuster()


    goal = decomposer.decompose(
        "build AI system"
    )

    assert len(
        goal["milestones"]
    ) == 3


    tracker.update(
        "phase_1",
        "completed"
    )

    assert tracker.get(
        "phase_1"
    ) == "completed"


    deviation = predictor.predict(
        30
    )

    assert deviation["deviation"] is True


    strategy = adjuster.suggest(
        True
    )

    assert strategy["strategy"] == "adjust"



    # 2. Cross-Environment Context

    collector = ContextCollector()
    model = EnvironmentModel()
    sync = ContextSync()
    manager = ContextManager()


    context = collector.collect(
        "computer",
        {
            "task": "development"
        }
    )

    assert context["environment"] == "computer"


    model.update(
        "office",
        "active"
    )

    assert model.get(
        "office"
    ) == "active"


    result = sync.sync(
        collector.list_contexts()
    )

    assert result["status"] == "synced"


    result = manager.activate(
        context
    )

    assert result["status"] == "activated"



    # 3. Decision Support Intelligence

    analyzer = InformationAnalyzer()
    comparator = OptionComparator()
    risk = RiskAnalyzer()
    recommender = RecommendationEngine()


    info = analyzer.analyze(
        "project data"
    )

    assert info["status"] == "analyzed"


    options = comparator.compare(
        [
            "option_a",
            "option_b"
        ]
    )

    assert options["comparison"] == "completed"


    risk_result = risk.analyze(
        "option_a"
    )

    assert risk_result["risk"] == "evaluated"


    recommendation = recommender.recommend(
        risk_result
    )

    assert recommendation["recommendation"] == "generated"



    print(
        "AI-OS V1.6 INTEGRATION PASS"
    )


if __name__ == "__main__":

    test_ai_os_v1_6_integration()
