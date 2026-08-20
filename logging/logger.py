from datetime import datetime


class AIOSLogger:


    def __init__(
        self,
        level="INFO"
    ):

        self.level = level



    def _log(
        self,
        level,
        message
    ):

        time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )


        print(
            f"{time} [{level}] {message}"
        )



    def info(
        self,
        message
    ):

        self._log(

            "INFO",

            message

        )



    def error(
        self,
        message
    ):

        self._log(

            "ERROR",

            message

        )



    def debug(
        self,
        message
    ):

        self._log(

            "DEBUG",

            message

        )
