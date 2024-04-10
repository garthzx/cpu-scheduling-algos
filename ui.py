"""
    Main terminal program. Dito natin ilagay yung user interface na kung saan mag-iinput yung user ng processes. Dapat daw
    user input yung processes: how many processes --> input arrival time --> input burst time
"""

from fcfs import FCFS
from priority import Priority
from rr import RR
from sjf import SJF
from process import Process
from algorithm import Algorithm


class UI:

    def __init__(self) -> None:
        self.fcfs = FCFS()
        self.priority = Priority()
        self.rr = RR()
        self.sjf = SJF()
        pass

    def run(self):
        isRunning = True

        while isRunning:
            algorithm = self._prompt_algorithm()
            processes = self._prompt_processes(algorithm)

            # for p in processes:
            #     print(f"{p.process_id},{p.at},{p.bt}")

            # TODO
            quantum = 0
            if algorithm == Algorithm.RR.value:
                quantum = int(input("Quantum: "))

            self._solve(algorithm, processes, quantum=quantum)

    def _solve(self, algorithm, processes, quantum=0):
        if algorithm == Algorithm.FCFS.value:
            self.fcfs = FCFS(processes)
            self.fcfs.solve()
        elif algorithm == Algorithm.PRIORITY.value:
            self.priority = Priority(processes)
            self.priority.solve()
        elif algorithm == Algorithm.SJF.value:
            SJF(processes).solve()
        elif algorithm == Algorithm.RR.value:
            RR(processes=processes, quantum=quantum).solve()
        pass

    def _prompt_processes(self, algorithm):
        num_processes = int(input("Number of processes: "))
        processes = []
        for i in range(num_processes):
            if algorithm in [
                Algorithm.FCFS.value,
                Algorithm.SJF.value,
                Algorithm.SRTF.value,
            ]:
                process_attrs = str(input(f"P{i+1} [AT BT]: ")).strip().split(sep=" ")
                process_attrs = list(map(int, process_attrs))
                processes.append(
                    Process(i + 1, at=process_attrs[0], bt=process_attrs[1])
                )

            elif algorithm == Algorithm.PRIORITY.value:
                process_attrs = (
                    str(input(f"P{i+1} [Priority BT]:")).strip().split(sep=" ")
                )
                process_attrs = list(map(int, process_attrs))
                processes.append(
                    Process(i + 1, priority=process_attrs[0], bt=process_attrs[1])
                )

            elif algorithm == Algorithm.RR.value:
                process_attrs = str(input(f"P{i+1} [BT]:")).strip().split(sep=" ")
                process_attrs = list(map(int, process_attrs))
                processes.append(
                    Process(i + 1, bt=process_attrs[0])
                )

        return processes

    def _prompt_algorithm(self):
        valid = False
        while not valid:
            print(
                "[1] First Come First Serve\n[2] Shortest Job First\n[3] Shortest Remaining Time First\n[4] Priority\n[5] Round Robin\nSelect algorithm >> ",
                end="",
            )
            choice = int(input())
            if choice > 0 and choice < 6:
                valid = True

        return choice
