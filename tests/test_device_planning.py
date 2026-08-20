from core.planner.device_planner import DevicePlanner



planner = DevicePlanner()



print("Device Planner Ready")



result = planner.create_plan(

    {
        "goal":
        "帮我拍一张照片"
    }

)



print(result)

