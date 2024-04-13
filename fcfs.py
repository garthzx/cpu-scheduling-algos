import operator
from statistics import mean
from gantt import Gantt
from table import Table
from process import Process
from eval import Eval

class FCFS:
    """
    FCFS Implementation with consideration for idle time.
    """

    def __init__(self, processes = []) -> None:
        self.processes = processes
        self.current_time = 0
        # Sorted by arrival time first, then process_id.
        self.sorted = sorted(
            self.processes, key=operator.attrgetter("at", "process_id")
        )
        self.gantt = Gantt()
        self.table = Table()
        self.eval = Eval()

    def solve(self):
        for current_process in self.sorted:
            current_process.bursted_by = current_process.bt
            self.current_time += current_process.bt
            self.update_params(current_process)
            self.gantt.add_process(current_process)

        self.gantt.draw()
        self.table.processes = sorted(self.sorted, key=lambda x: x.process_id)
        self.table.draw_table()
        
        self.eval.processes = self.processes
        self.eval.display_eval()
        
    def update_params(self, current_process: Process):
        current_process.et = self.current_time
        current_process.tt = current_process.et - current_process.at
        current_process.wt = current_process.tt - current_process.bt