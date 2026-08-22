from core.cross_environment_context import (
    ContextCollector,
    EnvironmentModel,
    ContextSync,
    ContextManager
)



def test_cross_environment_context():


    collector = ContextCollector()

    model = EnvironmentModel()

    sync = ContextSync()

    manager = ContextManager()



    context = collector.collect(
        "computer",
        {
            "task": "work"
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



    print(
        "Cross-Environment Context Layer PASS"
    )



if __name__ == "__main__":

    test_cross_environment_context()
