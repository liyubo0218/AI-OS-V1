from device.agents.iphone_agent import IPhoneAgent

from device.agents.mac_agent import MacAgent

from device.agents.car_agent import CarAgent



agents = {


"iphone_001":
IPhoneAgent(),


"mac_001":
MacAgent(),


"car_001":
CarAgent()

}



print("Multi Device Execution Ready")



print(

    agents["iphone_001"].execute(
        "capture"
    )

)



print(

    agents["mac_001"].execute(
        "open_file"
    )

)



print(

    agents["car_001"].execute(
        "navigate_company"
    )

)

