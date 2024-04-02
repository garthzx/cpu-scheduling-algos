class EndTime:
    def __init__(self, et) -> None:
        pass

class Gantt:
    def __init__(self, processes : list = []):
        self.processes = processes
        pass        
        
    def add_process(self, process):
        self.processes.append(process)
    
    def draw(self):
        print("\nGANTT CHART:\n")
        self.draw_horizontal()
        self.draw_strips()
        self.draw_horizontal()
        self.draw_time()
            
    def draw_strips(self):
        for process in self.processes:
            
            print("|", end="")
            print(process.bursted_by * " ", end="")
            print(f"P{process.process_id}", end="")
            print(process.bursted_by * " ", end="") 
            
            # Add | for last process
            if self.processes[len(self.processes)-1] == process:
                print("|")
            
        # print("|", end="")   
    
    def draw_horizontal(self):
        print("+", end="")
        
        horizontals = sum(p.bursted_by for p in self.processes) * 2
        horizontals += len(self.processes) * 2
        horizontals += len(self.processes) + 1
        horizontals -= 2 
        
        print("-" * horizontals, end="")
        print("+")
        
    def draw_time(self):
        
        print("0", end="")
        for process in self.processes:
            spaces = ""
            spaces += "  "
            spaces += (" " * (process.bursted_by * 2))
            
            if len(str(process.et)) > 1:
                spaces = spaces[:-len(str(process.et)) + 1]
            
            spaces += str(process.et)
            print(spaces, end="")
        print()            
            
        