from chatgpt_bridge.task_adapter import ChatGPTTaskAdapter



adapter = ChatGPTTaskAdapter()



print("ChatGPT Device Bridge Ready")



print(

    adapter.convert(

        "帮我拍一张照片"

    )

)

