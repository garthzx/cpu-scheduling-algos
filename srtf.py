from gantt import Gantt
from eval import Eval
from table import Table
import copy
from operator import attrgetter
from process import Process

class SRTF:
    def __init__(self, processes = []) -> None:
        self.processes = processes
        self.current_time = 0
        self.copy = copy.deepcopy(processes)
        self.pool = copy.deepcopy(sorted(processes, key=attrgetter("at", "process_id")))
        self.ready_queue = []
        self.gantt_timeline = []
        self.gantt = Gantt()
        self.table = Table()
    
    
    def solve(self):

        next = self.get_next_from_pool()
        self.ready_queue.append(next)
        
        while self.has_processes_in_queue():
            print("Processes in pool")
            for p in self.pool:
                print(f"\tProcess {p.process_id}, {p.at}, {p.bt}")

            print("Processes in queue")
            for p in self.ready_queue:
                print(f"\tProcess {p.process_id}, {p.at}, {p.bt}")
            
            selected_process = self.get_lowest_bt_from_queue()
            print(f"Selected process: P{selected_process.process_id}, {selected_process.at}, {selected_process.bt}")

            if len(self.pool) != 0:
                peek = self.peek_from_pool()

            # Timer interrupt: Another process enters while another is being executed ("bursted")
            bursted_by = selected_process.bt
            if peek and peek.at <= (selected_process.bt + self.current_time):
                print(f"Peeked process {peek.process_id}, {peek.at}, {peek.bt}")
                next = self.get_next_from_pool()
                if next:
                    bursted_by =  abs(self.current_time - next.at)
                    print(f"Appending process {next.process_id}, {next.at}, {next.bt}")
                    self.ready_queue.append(next)

            # else:
            #     bursted_by = selected_process.bt

            print(f"Bursted by: {bursted_by}")
            self.current_time += bursted_by
            selected_process.bt -= bursted_by
            
            if selected_process.bt <= 0:
                self.remove_from_queue(selected_process)
                print(f"Removing process {selected_process.process_id}, {selected_process.at}, {selected_process.bt}")
            
            self.append_to_gantt(selected_process, bursted_by)
            self.update_params_process(selected_process.process_id, bursted_by)
            
            print("---------------------------------------")
        
        self.gantt.processes = self.gantt_timeline
        self.gantt.draw()
    
    def peek_from_pool(self):
        return self.pool[0]
    
    def remove_from_queue(self, process):
        process_in_queue = self.find_process_by_id(self.ready_queue, process.process_id)
        self.ready_queue.remove(process_in_queue)
                
    def update_params_process(self, process_id, bursted_by):
        process = self.find_process_by_id(self.processes, process_id)
        process.et = self.current_time
        process.tt = process.et - process.at
        process.wt = process.tt - process.tt
    
    def append_to_gantt(self, process, bursted_by):
        gantt_process = Process(process.process_id)
        gantt_process.bursted_by = bursted_by
        gantt_process.et = self.current_time
        
        self.gantt_timeline.append(gantt_process)
        
    
    def get_lowest_bt_from_queue(self):
        return min(self.ready_queue, key=attrgetter("bt"))

    
    def find_process_by_id(self, processes, id):
        for p in processes:
            if p.process_id == id:
                return p
        return None
        
    def has_processes_in_queue(self):
        return len(self.ready_queue) > 0
    
    def get_next_from_pool(self):
        if len(self.pool) == 0:
            return None
        return self.pool.pop(0)
    
    