from core.decision_support_intelligence import (
    InformationAnalyzer,
    OptionComparator,
    RiskAnalyzer,
    RecommendationEngine
)



def test_decision_support_intelligence():


    analyzer = InformationAnalyzer()

    comparator = OptionComparator()

    risk = RiskAnalyzer()

    recommender = RecommendationEngine()



    result = analyzer.analyze(
        "project information"
    )

    assert result["status"] == "analyzed"



    result = comparator.compare(
        [
            "option_a",
            "option_b"
        ]
    )

    assert result["comparison"] == "completed"



    result = risk.analyze(
        "option_a"
    )

    assert result["risk"] == "evaluated"



    result = recommender.recommend(
        result
    )

    assert result["recommendation"] == "generated"



    print(
        "Decision Support Intelligence Layer PASS"
    )



if __name__ == "__main__":

    test_decision_support_intelligence()
