from core.system.bootstrap import Bootstrap


def test_bootstrap_create():

    system = Bootstrap().create()

    required_modules = [
        "memory",
        "event_bus",
        "brain",
        "secretary",
        "task_manager",
        "device",
        "mobile_gateway",
        "orchestrator",
        "runtime",
        "api",
    ]

    for module in required_modules:
        assert module in system


def test_mobile_gateway_channels():

    system = Bootstrap().create()

    channels = (
        system["mobile_gateway"]
        .available_channels()
    )

    assert "shortcut" in channels
    assert "notification" in channels
    assert "device" in channels
