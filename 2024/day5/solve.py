import re
import collections

def topological_sort(graph):
    indegree = {node: 0 for  node in graph}
    
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            indegree[neighbour] +=1
        
    queue = collections.deque([node for node in graph if indegree[node] == 0])

    arr=[]
    while queue:
        node = queue.popleft()
        arr.append(node)
        for neighbour in graph[node]:
            indegree[neighbour] -=1
            if not indegree[neighbour]:
                queue.append(neighbour)
    
    return arr

def main():
    print("\n--- Day 4: Print Queue ---")
    with open("input.txt","r") as f:
        text=f.read()
        print("Input read")

    rules, updates = text.split('\n\n')
    rules = [[int(x),int(y)] for x,y in re.findall(r'(?P<pg1>\d+)\|(?P<pg2>\d+)',rules)]
    updates=[[int(page) for page in update.split(',')] for update in updates.splitlines()]

    """     Only Part 1
    
    correct_page_sum=0

    for update in updates:
        for x,y in rules:
            if x in update and y in update and update.index(x)>update.index(y):
                break
        else:
            correct_page_sum += update[len(update)//2]

    """

    #Both Parts together

    correct_page_sum=0
    corrected_page_sum=0

    #Dictionary containing set of all pages that must come after the key page
    after = collections.defaultdict(set)
    for x,y in rules:
        after[x].add(y)

    for update in updates:
        for x,y in rules:
            if x in update and y in update and update.index(x)>update.index(y):
                
                graph = {}
                for page in update:
                    graph[page] = [k for k in update if k in after[page]]      #list-implementation
                    #graph[page] = after[page].intersection(set(update))       #set-implementation
                corrected_update = topological_sort(graph)
                corrected_page_sum += corrected_update[len(corrected_update)//2]
                
                break
        else:
            correct_page_sum += update[len(update)//2]
    
    print(f"\n--- Part One ---\n Sum of middle page numbers of correctly-ordered updates: {correct_page_sum}")

    print(f"\n--- Part Two --- \nSum of middle page numbers of corrected incorrectly-ordered updates: {corrected_page_sum}\n")

if __name__ == '__main__':
    main()
