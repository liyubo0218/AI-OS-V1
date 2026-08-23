from core.interface.api import AIOSAPI
from core.system.bootstrap import Bootstrap


def test_health_check():

    api = AIOSAPI()

    result = api.health_check()

    assert result["status"] == "ok"



def test_api_request():

    system = Bootstrap().create()

    api = system["api"]

    result = api.handle_request(
        {
            "user_input": "提醒我明天上午9点开会"
        }
    )

    assert result["status"] == "success"

    assert (
        result["result"]["intent"]["intent"]
        == "create_task"
    )



def test_api_without_runtime():

    api = AIOSAPI()

    result = api.handle_request(
        {
            "user_input": "test"
        }
    )

    assert result["status"] == "error"
