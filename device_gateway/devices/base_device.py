class BaseDevice:

    def __init__(
        self,
        name,
        capabilities
    ):

        self.name = name

        self.capabilities = capabilities


    def execute(
        self,
        command
    ):

        raise NotImplementedError
