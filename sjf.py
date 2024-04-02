import operator as op
from process import Process
from table import Table
from gantt import Gantt


class SJF:
    def __init__(self, processes: list = []) -> None:
        self.processes = processes
        self.current_time = 0
        self.processes_in_cpu = []
        # self.sorted = sorted(self.processes, key=op.attrgetter("bt", "at"))
        self.copy = self.processes.copy()
        self.table = Table()
        self.gantt = Gantt()

    def solve(self):
        self.set_first_processes()
        # self.show_processes_in_cpu()
        print()

        while self.processes_in_cpu:
            # self.show_processes_in_cpu()

            processes_sorted_in_cpu = sorted(
                self.processes_in_cpu, key=op.attrgetter("bt", "at", "process_id")
            )

            process = processes_sorted_in_cpu[0]

            self.current_time += process.bt

            # update params
            original = self.find_by_id(process.process_id)
            original.bursted_by = process.bt
            original.et = self.current_time
            original.tt = original.et - original.at
            original.wt = original.tt - original.bt

            self.remove_process(process)
            self.update_cpu_processes()

            self.gantt.add_process(process)

        self.gantt.draw()
        self.table.processes = self.processes
        self.table.draw_table()

        print(f"\nAverage Turnaround Time: {self.att()}")
        print(f"Average Waiting Time: {self.awt()}")

    def remove_process(self, process):
        for p in self.copy:
            if p.process_id == process.process_id:
                self.copy.remove(p)

        for p in self.processes_in_cpu:
            if p.process_id == process.process_id:
                self.processes_in_cpu.remove(p)

    def set_first_processes(self):
        while not self.processes_in_cpu:
            for p in self.copy:
                if p.at <= self.current_time:
                    self.processes_in_cpu.append(p)
                    self.copy.remove(p)

            if not self.processes_in_cpu:
                self.current_time += 1

    def update_cpu_processes(self):
        for p in self.copy:
            if p.at <= self.current_time and not self.exists(p):
                self.processes_in_cpu.append(p)

    def exists(self, process):
        for p in self.processes_in_cpu:
            if p.process_id == process.process_id:
                return True
        return False

    def find_by_id(self, id):
        for p in self.processes:
            if p.process_id == id:
                return p
        return None

    def show_processes_in_cpu(self):
        for p in self.processes_in_cpu:
            print(f"P{p.process_id}, AT:{p.at}, BT:{p.bt}")

    def att(self):
        return round(sum([p.tt for p in self.processes]) / len(self.processes), 2)

    def awt(self):
        return round(sum([p.wt for p in self.processes]) / len(self.processes), 2)
