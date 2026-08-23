from core.system.config import ConfigManager


def test_config_set_get():

    config = ConfigManager()

    config.set(
        "mode",
        "beta"
    )

    assert (
        config.get("mode")
        == "beta"
    )


def test_config_default():

    config = ConfigManager()

    value = config.get(
        "unknown",
        "default"
    )

    assert (
        value
        == "default"
    )
