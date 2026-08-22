from core.long_term_goal_intelligence import (
    GoalDecomposer,
    MilestoneTracker,
    DeviationPredictor,
    StrategyAdjuster
)



def test_long_term_goal_intelligence():


    decomposer = GoalDecomposer()

    tracker = MilestoneTracker()

    predictor = DeviationPredictor()

    adjuster = StrategyAdjuster()



    result = decomposer.decompose(
        "complete project"
    )


    assert len(
        result["milestones"]
    ) == 3



    tracker.update(
        "phase_1",
        "completed"
    )


    assert tracker.get(
        "phase_1"
    ) == "completed"



    result = predictor.predict(
        30
    )


    assert result["deviation"] is True



    result = adjuster.suggest(
        True
    )


    assert result["strategy"] == "adjust"



    print(
        "Long-Term Goal Intelligence Layer PASS"
    )



if __name__ == "__main__":

    test_long_term_goal_intelligence()
