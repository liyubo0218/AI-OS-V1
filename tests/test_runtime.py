from core.runtime.runtime import Runtime


def test_runtime_start_stop():

    runtime = Runtime()

    assert (
        runtime.get_status()["status"]
        == "stopped"
    )

    result = runtime.start()

    assert (
        result["status"]
        == "running"
    )

    result = runtime.stop()

    assert (
        result["status"]
        == "stopped"
    )



def test_runtime_without_orchestrator():

    runtime = Runtime()

    result = runtime.handle(
        "test"
    )

    assert (
        result["status"]
        == "error"
    )



def test_runtime_alias():

    from core.runtime.runtime import RuntimeCore

    runtime = RuntimeCore()

    assert isinstance(
        runtime,
        Runtime
    )
