import math
from collections import deque, defaultdict

def load_priorities_paths(filepath):
    page_ordering_rules = []
    with open(filepath) as reader:
        lines = reader.readlines()

    path_start = False
    paths = []

    for line in lines:
        if (line == '\n'):
            path_start = True
        if path_start == False:
            line = (line.strip())
            line_split = line.split("|")
            page_ordering_rules.append(line_split)
        else:
            if line != '\n':
                paths.append(line.strip().split(","))

    return page_ordering_rules, paths


def get_graph_dict(page_ordering_rules):
    graph = {}
    for rule in page_ordering_rules:
        node = rule[0]
        node_to = rule[1]
        if node not in graph:
            graph[node] = []
        if node_to not in graph:
            graph[node_to] = []
        graph[node].append(node_to)
        # else:
        #     graph[node].append(node_to)
    return graph

def traverse_path(graph, path):
    for n in range(len(path) - 1):
        node = path[n]
        node_to = path[n+1]
        if node not in graph or node_to not in graph[node]:
            return False
    return True

def topological_sort(graph, path):
    partial_graph = {node: graph[node] for node in path}
    in_degree = {node: 0 for node in partial_graph} # initialse a in-degree map for each node in the path to be sorted
    for node in partial_graph: # for each neighbors of each node in the subgraph
        for node_to in partial_graph[node]: 
            if node_to in path:  
                in_degree[node_to] += 1 # incoming edge + 1 degree
    
    zero_degree = deque([node for node in path if in_degree[node] == 0])

    sorted = []
    while zero_degree:
        current_node = zero_degree.popleft()
        sorted.append(current_node)

        for node_to in partial_graph[current_node]: # minus one degree for each node_to of the current node 
            if node_to in path:
                in_degree[node_to] -= 1
                if in_degree[node_to] == 0:
                    zero_degree.append(node_to)

    return sorted


if __name__ == "__main__":
    sum_1 = 0
    sum_2 = 0
    page_ordering_rules, paths = load_priorities_paths('input-dec5.txt')
    graph = get_graph_dict(page_ordering_rules)
    path1 = [75,97,47,61,53]
    path1_str = [str(item) for item in path1]
    for path in paths:
        if traverse_path(graph, path):
            middle = path[int(len(path) / 2)]
            sum_1 += int(middle)
        else:
            resorted = topological_sort(graph, path)
            m = resorted[int(len(resorted) / 2)]
            sum_2 += int(m)
    print(sum_2)
            
    # for node, node_to in graph.items():
    #     print(node, ":", node_to)
    # sum = 0
    # for path in paths:
    #     if traverse_path(graph, path):
    #         m = path[int(len(path) / 2)]
    #         sum += int(m)

    # print(sum)
    # graph = get_graph_dict(page_ordering_rules)
    # print(graph)
    # can = traverse_path(graph, path1_str)
    # print(can)