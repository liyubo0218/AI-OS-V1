from core.personal_memory_intelligence import (
    PreferenceAnalyzer,
    HabitTracker,
    ContextAssociator,
    UserProfileModel
)



def test_personal_memory_intelligence():


    analyzer = PreferenceAnalyzer()


    result = analyzer.analyze(
        "喜欢使用AI助手"
    )


    assert result["identified"] is True



    tracker = HabitTracker()


    tracker.record(
        "每天查看任务"
    )


    assert len(
        tracker.list_habits()
    ) == 1



    associator = ContextAssociator()


    association = associator.associate(
        "工作",
        "项目任务"
    )


    assert association["associated"] is True



    profile = UserProfileModel()


    profile.update(
        "work_style",
        "efficient"
    )


    assert profile.get(
        "work_style"
    ) == "efficient"



    print(
        "Personal Memory Intelligence Layer PASS"
    )



if __name__ == "__main__":

    test_personal_memory_intelligence()
