from core.aios import AIOS

from config.settings import AIOSSettings

from logging.logger import AIOSLogger

from runtime.manager import RuntimeManager



class DemoBrain:


    def understand(
        self,
        context
    ):

        return {

            "goal":
            context["user_input"],

            "status":
            "understood"

        }



class DemoRouter:


    def execute(
        self,
        task
    ):

        return {

            "status":
            "completed",

            "message":
            "AI-OS任务完成"

        }



class DemoMemory:


    def save(
        self,
        t,
        c
    ):

        pass



def start():


    settings = AIOSSettings()

    logger = AIOSLogger()

    runtime = RuntimeManager()



    aios = AIOS(

        DemoBrain(),

        DemoRouter(),

        DemoMemory(),

        settings,

        logger,

        runtime

    )



    print(
        "===== AI-OS V1.0 Started ====="
    )



    result = aios.run(

        "测试AI-OS启动"

    )



    print(result)



if __name__ == "__main__":

    start()

