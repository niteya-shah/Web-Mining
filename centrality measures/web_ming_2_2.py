import networkx as nx
import matplotlib.pyplot as plt
import csv
from itertools import combinations

G=nx.DiGraph()
with open('./dh11_nodes.csv', 'r') as csvread:
    nodereader = csv.reader(csvread)
    nodenames = [n[0] for n in nodereader][1:]
len(nodenames)
with open('./dh11_edges.csv', 'r') as csvread:
    nodereader = csv.reader(csvread)
    nodedges = [tuple(n[0:2]) for n in nodereader][1:]
##
G.add_nodes_from(nodenames)
G.add_edges_from(nodedges)
v=nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx(G,pos=v,with_labels=False,node_size = 20)
##
degree_prestige = dict((vertex,len(G.in_edges(vertex))/(len(nodenames)-1)) for vertex in G.nodes())
##
num_nodes=len(nodenames)
proximity_prestige=list()
for i in nx.all_pairs_shortest_path_length(G):
    proximity_prestige.append([i[0],((len(list(i[1].values()))-1)**2)/(0.0001+sum(list(i[1].values()))*num_nodes)])
##
rank_prestige=nx.pagerank(G,alpha=1)
##
co_citation=[]
bibliography_coupling=[]
for i in combinations(G.nodes(),2):
    w=set(G.neighbors(i[0])).intersection(set(G.neighbors(i[1])))
    if len(w)>0:
        bibliography_coupling.append([i[0],i[1],[w]])

for i in G.nodes():
    w=list(combinations(G.neighbors(i),2))
    if len(w)>0:
        co_citation.append([i,w])
##
pr = nx.pagerank(G, alpha=0.85)
##
prs=sorted(pr.items(),key=lambda x:x[1],reverse=True)
dp=sorted(degree_prestige.items(),key=lambda x:x[1],reverse=True)
pp=sorted(proximity_prestige,key=lambda x:x[1],reverse=True)
rp=sorted(rank_prestige.items(),key=lambda x:x[1],reverse=True)
##
print("RageRank")
print(prs[0:10])
print("degree prestige")
print(dp[0:10])
print("proximity prestige")
print(pp[0:10])
print("Rank prestige")
print(rp[0:10])
print("bibliography_coupling")
print(bibliography_coupling,end=" ")
print("Co-citation")
print(co_citation,end=" ")
