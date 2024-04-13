from tabulate import tabulate

class Table:
    def __init__(self, processes : list = []):
        self.processes = processes
        
    def add_process(self, process):
        self.processes.append(process)
    
    def draw_table(self, isPriority=False):
        print("\nTABLE:\n")
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