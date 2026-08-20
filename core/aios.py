from logging.logger import AIOSLogger


class AIOS:


    def __init__(
        self,
        brain,
        task_router,
        memory,
        settings=None,
        logger=None,
        runtime=None
    ):

        self.brain = brain

        self.task_router = task_router

        self.memory = memory

        self.settings = settings

        self.logger = logger or AIOSLogger()

        self.runtime = runtime



    def run(
        self,
        user_input
    ):


        if self.runtime:

            self.runtime.start()

            self.runtime.update_task(
                user_input
            )



        self.logger.info(
            "AI-OS Started"
        )



        if self.settings:

            self.logger.info(
                f"Version {self.settings.version}"
            )


            self.logger.info(
                f"Environment {self.settings.environment}"
            )



        self.logger.info(
            "Brain Understanding"
        )


        understanding = self.brain.understand(

            {
                "user_input":
                user_input
            }

        )



        self.logger.info(
            "Task Executing"
        )


        result = self.task_router.execute(

            understanding

        )



        self.memory.save(

            "task",

            user_input

        )



        self.logger.info(
            "Memory Saved"
        )


        self.logger.info(
            "Task Completed"
        )



        return {

            "status":
            "completed",

            "understanding":
            understanding,

            "result":
            result,

            "runtime":
            self.runtime.get_status()
            if self.runtime
            else None

        }
