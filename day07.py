import re
from collections import deque

import networkx as nx
from networkx import NetworkXNoPath

lines = [line.strip() for line in open("input/07.txt")]

G = nx.DiGraph()
for line in lines:
    container = re.findall(r'([a-z ]*) bags contain', line)[0]
    bags = re.findall(r'(\d+) ([a-z ]*) bag[s]?[,.]?', line[len(container) + 13:])
    for num, bag in bags:
        num = int(num)
        G.add_edge(container, bag, weight=num)

# Part A
target = "shiny gold"
paths = []
for source in G.nodes:
    if source == target:
        continue
    try:
        path = list(nx.all_shortest_paths(G, source=source, target=target))
        paths.append(path)
    except NetworkXNoPath:
        continue
print(len(paths))

# Part B
q = deque([(target, 1)])
bag_count = 0
while q:
    curr, count = q.popleft()
    bag_count += count
    for _, bag in G.out_edges([curr]):
        q.append((bag, count * G.edges[curr, bag]["weight"]))
print(bag_count - 1)
