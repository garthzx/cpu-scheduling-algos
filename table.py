from tabulate import tabulate

class Table:
    def __init__(self, processes : list = []):
        self.processes = processes
        
    def add_process(self, process):
        self.processes.append(process)
    
    def draw_table(self, isPriority=False):
        print("\nTABLE:\n")
        # print("| P\t| AT\t| BT\t| ET\t| TT\t| WT\t|")
        data = []
        
        if isPriority:
            for p in self.processes:
                data.append([f"P{p.process_id}", p.priority, p.bt, p.et, p.tt, p.wt])
            headers = ["P", "Priority", "BT", "ET", "TT", "WT"]
        
        else:
            for p in self.processes:
                data.append([f"P{p.process_id}", p.at, p.bt, p.et, p.tt, p.wt])    
            headers = ["P", "AT", "BT", "ET", "TT", "WT"]
        
        table = tabulate(data, headers=headers, tablefmt="grid")    
        print(table)
        # for p in self.processes:
        #     print(f"| P{p.process_id}\t| {p.at}\t| {p.bt}\t| {p.et}\t| {p.tt}\t| {p.wt}\t|")