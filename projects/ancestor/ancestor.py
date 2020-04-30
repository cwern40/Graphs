class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def get_ancestors(ancestors, child):
    child_ancestors = []
    # for each letter in word
    for i in range(len(ancestors)):
        if ancestors[i][1] == child:
            child_ancestors.append(ancestors[i][0])
    return child_ancestors

def earliest_ancestor(ancestors, starting_node):
    plan_to_visit = Queue()
    current_path = [starting_node]
    plan_to_visit.enqueue(current_path)
    visited_vertices = set()
    previous_path = []

    while plan_to_visit.size() > 0:
        current_path = plan_to_visit.dequeue()

        if current_path[-1] not in visited_vertices:

            visited_vertices.add(current_path[-1])

            if len(current_path) > len(previous_path):
                    previous_path = current_path

            for neighbor in get_ancestors(ancestors, current_path[-1]):
                new_path = current_path[:]
                new_path.append(neighbor)
                plan_to_visit.enqueue(new_path)
    
    if len(current_path) > 1:
        if len(current_path) == len(previous_path) and current_path[-1] != previous_path[-1]:
            if previous_path[-1] < current_path[-1]:
                return previous_path[-1]
        return current_path[-1]
    else: 
        return -1