from collections import deque
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip()
                line = line.split(',')
                n = int(line[0])
                m = int(line[1])
            
                people = xrange(n)
                people_cycle = ModifiableCycle(people)
                killed_list = []
            
                i = 1
                while people_cycle.has_next():
                    person = next(people_cycle)
                    if i % m == 0:
                        killed_list.append(person)
                        people_cycle.delete_prev()
                    i+=1
            
                print ' '.join(map(str, killed_list))


class ModifiableCycle(object):
    def __init__(self, items=()):
        self.deque = deque(items)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.deque:
            raise StopIteration
        item = self.deque.popleft()
        self.deque.append(item)
        return item
    
    next = __next__

    def has_next(self):
        return self.deque
        
    def delete_prev(self):
        self.deque.pop()


if __name__ == '__main__':
    main(sys.argv[1])
