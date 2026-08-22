from core.runtime.registry import RuntimeRegistry
from core.runtime.state import RuntimeState


class RuntimeCore:

    def __init__(
        self,
        registry=None,
        state=None
    ):
        self.registry = registry or RuntimeRegistry()
        self.state = state or RuntimeState()


    def register(
        self,
        name,
        module
    ):
        return self.registry.register(
            name,
            module
        )


    def run(
        self,
        module_name,
        task
    ):
        self.state.set_state(
            RuntimeState.RUNNING
        )

        module = self.registry.get(
            module_name
        )

        if module is None:
            self.state.set_state(
                RuntimeState.FAILED
            )

            return {
                "status": "failed",
                "state": self.state.get_state(),
                "module": module_name,
                "task": task,
                "error": "module not registered"
            }

        try:
            result = self._execute_module(
                module,
                task
            )

            self.state.set_state(
                RuntimeState.COMPLETED
            )

            return {
                "status": "completed",
                "state": self.state.get_state(),
                "module": module_name,
                "task": task,
                "result": result
            }

        except Exception as error:
            self.state.set_state(
                RuntimeState.FAILED
            )

            return {
                "status": "failed",
                "state": self.state.get_state(),
                "module": module_name,
                "task": task,
                "error": str(error)
            }


    def execute(
        self,
        module_name,
        task
    ):
        return self.run(
            module_name,
            task
        )


    def get_state(self):
        return self.state.get_state()


    def _execute_module(
        self,
        module,
        task
    ):
        if isinstance(module, type):
            module = module()

        if hasattr(module, "execute"):
            return module.execute(
                task
            )

        if callable(module):
            return module(
                task
            )

        raise TypeError(
            "module must be callable or expose execute"
        )
