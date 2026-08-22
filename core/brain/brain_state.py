from enum import Enum


class BrainState(Enum):

    IDLE = "idle"

    ANALYZING = "analyzing"

    PLANNING = "planning"

    EXECUTING = "executing"

    COMPLETED = "completed"

    FAILED = "failed"
