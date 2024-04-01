
class Process:
    """
        Class to define a process.
    """

    def __init__(self, process_id, at, bt) -> None:
        self.process_id = process_id
        self.at = at
        self.bt = bt
        self.et = -1
        self.tt = -1
        self.wt = -1
        