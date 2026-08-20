class BaseAgent:

    def __init__(self, name, capability):
        self.name = name
        self.capability = capability


    def execute(self, task):
        raise NotImplementedError
