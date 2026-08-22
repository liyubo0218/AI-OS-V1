from core.advanced_user_model import (
    PreferenceModel,
    BehaviorAnalyzer,
    DecisionPattern,
    PersonalStrategy
)



def test_advanced_user_model():


    preference = PreferenceModel()


    result = preference.update(
        "work_style",
        "efficient"
    )


    assert result["status"] == "updated"


    assert preference.get(
        "work_style"
    ) == "efficient"



    analyzer = BehaviorAnalyzer()


    behavior = analyzer.analyze(
        [
            "plan",
            "execute",
            "review"
        ]
    )


    assert behavior["pattern"] == "identified"



    decision = DecisionPattern()


    decision.record(
        "compare_before_action"
    )


    assert len(
        decision.list_patterns()
    ) == 1



    strategy = PersonalStrategy()


    result = strategy.select(
        "work_task"
    )


    assert result["strategy"] == "personalized"



    print(
        "Advanced User Model Layer PASS"
    )



if __name__ == "__main__":

    test_advanced_user_model()
