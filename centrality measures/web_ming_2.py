import networkx as nx
import matplotlib.pyplot as plt
import csv
G=nx.Graph()
with open('./quakers_nodelist.csv', 'r') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader][1:]
node_names = [n[0] for n in nodes]
with open('./quakers_edgelist.csv', 'r') as edgecsv:
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader][1:]
G.add_nodes_from(node_names)
G.add_edges_from(edges)
print(nx.info(G))
v=nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx(G,pos=v,with_labels=False,node_size = 20)
density = nx.density(G)
bet=nx.betweenness_centrality(G)
deg=nx.degree_centrality(G)
clos=nx.closeness_centrality(G)
##
print("Network density:\n\n", density)
print("\n\nNetwork betweenness:",sorted(bet.items(),key= lambda x:x[1],reverse=True))
print("\n\nNetwork degree:",sorted(deg.items(),key= lambda x:x[1],reverse=True))
print("\n\nNetwork closeness:",sorted(clos.items(),key= lambda x:x[1],reverse=True))
