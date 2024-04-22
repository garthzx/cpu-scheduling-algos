from colorama import Fore


class Eval:
    def __init__(self, processes=[]) -> None:
        self.processes = processes

    def att(self):
        return round(sum([p.tt for p in self.processes]) / len(self.processes), 2)

    def awt(self):
        return round(sum([p.wt for p in self.processes]) / len(self.processes), 2)

    def cpu_utilization(self):
        sum_bt = sum([p.bt for p in self.processes])
        total_end_time = sorted(self.processes, key=lambda x: x.et)[-1].et
        # print(f"total_end_time: {total_end_time}")
        return round((sum_bt / total_end_time) * 100, 2)

    def display_eval(self):
        print(f"\n{Fore.CYAN}CPU Utilization:{Fore.WHITE} {self.cpu_utilization()}%")
        print(f"{Fore.CYAN}Average Turnaround Time:{Fore.WHITE} {self.att()}")
        print(f"{Fore.CYAN}Average Waiting Time:{Fore.WHITE} {self.awt()}")
