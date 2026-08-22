from core.multi_device_intelligence import (
    DeviceState,
    CapabilityMapper,
    DeviceSelector,
    TaskRouter,
    SyncManager
)



def test_multi_device_intelligence():


    state = DeviceState()

    mapper = CapabilityMapper()

    selector = DeviceSelector()

    router = TaskRouter()

    sync = SyncManager()



    state.update(
        "phone",
        "online"
    )

    assert state.get(
        "phone"
    ) == "online"



    mapper.register(
        "computer",
        [
            "file_operation"
        ]
    )

    assert mapper.get_capability(
        "computer"
    ) == [
        "file_operation"
    ]



    device = selector.select(
        [
            {
                "name": "computer",
                "capabilities": [
                    "file_operation"
                ]
            }
        ],
        "file_operation"
    )


    assert device == "computer"



    route = router.route(
        "transfer_file",
        device
    )


    assert route["status"] == "routed"



    result = sync.sync(
        "transfer_file",
        "completed"
    )


    assert result["status"] == "synced"



    print(
        "Multi-Device Intelligence Layer PASS"
    )



if __name__ == "__main__":

    test_multi_device_intelligence()
