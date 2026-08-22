from core.brain import IntentEngine


def test_intent():

    engine = IntentEngine()


    result = engine.analyze(
        "提醒我明天开会"
    )


    assert result["intent"] == "reminder"


    print(
        "Intent Engine PASS"
    )


if __name__ == "__main__":

    test_intent()
