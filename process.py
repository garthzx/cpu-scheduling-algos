class Process:
    """
    Class to define a process.
    """

    def __init__(self, process_id, at=0, bt=-1, priority=-1) -> None:
        self.process_id = process_id
        self.at = at
        self.bt = bt
        self.et = -1
        self.tt = -1
        self.wt = -1

        # only use for priority scheduling algorithm
        self.priority = priority

        self.bursted_by = 0
