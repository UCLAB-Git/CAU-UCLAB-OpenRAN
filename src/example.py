import random
import time

class Cell:
    def __init__(self, cell_id, capacity):
        self.cell_id = cell_id
        self.capacity = capacity
        self.current_load = 0.0

    def add_traffic(self, amount):
        self.current_load += amount

    def remove_traffic(self, amount):
        self.current_load = max(self.current_load - amount, 0)

    def get_utilization(self):
        return (self.current_load / self.capacity) * 100.0

def steer_traffic(cells, threshold=80.0):
    """
    A basic traffic steering logic:
    1. If a cell's utilization > threshold, move 20% of its load to the cell with the most available capacity.
    2. Print out the steering action for logging.
    """
    for cell in cells:
        usage = cell.get_utilization()
        if usage > threshold:
            overloaded_amount = cell.current_load * 0.2
            # Find the cell with the largest available capacity
            target_cell = max(cells, key=lambda c: c.capacity - c.current_load)
            if target_cell is not cell:
                cell.remove_traffic(overloaded_amount)
                target_cell.add_traffic(overloaded_amount)
                print(f"[STEER] {cell.cell_id} → {target_cell.cell_id} | amount={overloaded_amount:.2f}")

def main():
    cells = [
        Cell("Cell_A", capacity=1000),
        Cell("Cell_B", capacity=800),
        Cell("Cell_C", capacity=1200)
    ]

    for cycle in range(1, 6):
        print(f"=== Cycle {cycle} ===")
        # Simulate random traffic increase
        for cell in cells:
            additional_traffic = random.uniform(50, 200)
            cell.add_traffic(additional_traffic)

        # Attempt to steer traffic if any cell is overloaded
        steer_traffic(cells, threshold=80.0)

        # Print utilization for monitoring
        for cell in cells:
            print(f"{cell.cell_id} Load={cell.current_load:.2f}, Util={cell.get_utilization():.2f}%")
        print("-" * 40)
        time.sleep(1)

if __name__ == "__main__":
    main()
