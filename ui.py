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
            algorithm = self.prompt_algorithm()
            processes = self.prompt_processes(algorithm)

            for p in processes:
                print(f"{p.process_id},{p.at},{p.bt}")

            quantum = 0
            if algorithm == Algorithm.RR.value:
                quantum = int(input("Quantum: "))
            
                        

    def prompt_processes(self, algorithm):
        num_processes = int(input("Number of processes: "))
        processes = []
        for i in range(num_processes):
            if algorithm in [
                Algorithm.FCFS.value,
                Algorithm.SJF.value,
                Algorithm.SRTF.value,
            ]:
                print(
                    "Enter process Arrival time and Burst time respectively by space-separated values."
                )
                process_attrs = str(input(f"P{i+1}: ")).strip().split(sep=" ")
                processes.append(
                    Process(i + 1, at=process_attrs[0], bt=process_attrs[1])
                )

            elif algorithm == Algorithm.PRIORITY.value:
                print(
                    "Enter process Priority and Burst time respectively by space-separated values."
                )
                process_attrs = str(input(f"P{i+1}")).strip().split(sep=" ")
                processes.append(
                    Process(i + 1, at=process_attrs[0], bt=process_attrs[1])
                )

            elif algorithm == Algorithm.RR.value:
                print("Enter process burst time.")
                process_attrs = str(input(f"P{i+1}")).strip().split(sep=" ")
                processes.append(
                    Process(i + 1, at=process_attrs[0], bt=process_attrs[1])
                )

        return processes

    def prompt_algorithm(self):
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
