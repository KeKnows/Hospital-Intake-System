# emergency_queue.py

class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency  # 1 is most urgent, 10 least urgent

class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if self.data:
            return self.data[0]
        return None

    def remove_min(self):
        if not self.data:
            return None
        min_patient = self.data[0]
        last_patient = self.data.pop()
        if self.data:
            self.data[0] = last_patient
            self.heapify_down(0)
        return min_patient

