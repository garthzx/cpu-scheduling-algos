import operator
from statistics import mean
from gantt import Gantt
from table import Table
from eval import Eval

class Priority:
    def __init__(self, processes: list = []) -> None:
        self.processes = processes
        self.current_time = 0
        # Sorted by priority first, then process_id.
        self.sorted = sorted(
            self.processes, key=operator.attrgetter("priority", "process_id")
        )
        self.gantt = Gantt()
        self.table = Table()
        self.eval = Eval()

    def solve(self):
        for current_process in self.sorted:

            self.current_time += current_process.bt
            self.update_params(current_process)
            self.gantt.add_process(current_process)

            current_process.bursted_by = current_process.bt

        self.gantt.draw()
        self.table.processes = sorted(self.sorted, key=lambda x: x.process_id)
        self.table.draw_table(isPriority=True)

        self.eval.processes = self.sorted
        self.eval.display_eval()

    def update_params(self, current_process):
        current_process.et = self.current_time
        current_process.tt = current_process.et - current_process.at
        current_process.wt = current_process.tt - current_process.bt
