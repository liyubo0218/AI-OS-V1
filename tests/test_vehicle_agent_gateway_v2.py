from core.application.vehicle_agent.vehicle_agent_gateway import VehicleAgentGateway


def test_vehicle_agent_gateway_v2():

    gateway = VehicleAgentGateway()


    request = gateway.create_request(
        "打开空调"
    )

    assert request["input"] == "打开空调"
    assert request["source"] == "vehicle_agent"


    capability = gateway.provide_capability()

    assert "climate_control" in capability["capability"]


    permission = gateway.provide_permission()

    assert permission["permission"]["climate_control"] is True


    response = gateway.handle_response(
        {
            "status": "completed",
            "result": "空调已开启"
        }
    )


    assert response["status"] == "completed"
    assert response["result"] == "空调已开启"


    print(
        "Vehicle Agent Gateway V2 PASS"
    )


if __name__ == "__main__":
    test_vehicle_agent_gateway_v2()
