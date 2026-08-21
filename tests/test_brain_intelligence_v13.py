from core.brain.intelligence.brain_intelligence import BrainIntelligence


def test_brain_intelligence_v13():

    brain = BrainIntelligence()

    result = brain.analyze(
        "帮我准备会议"
    )

    assert result["goal"] == "帮我准备会议"

    assert result["recommendation"] == "send_to_planner"

    print(
        "Brain Intelligence V1.3 PASS"
    )


if __name__ == "__main__":
    test_brain_intelligence_v13()
