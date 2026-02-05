import numpy as np
import graph
import sys
import math
def main():

    # Le poids des arcs de ce graphe correspondent aux capacités
    g = example()

    # Le poids des arcs de ce graphe correspondent au flot
    flow = fordFulkerson(g, "s", "t")

    print(flow)
    
# Fonction créant un graphe sur lequel sera appliqué l'algorithme de Ford-Fulkerson
def example():
        
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)
    
    return g


# Fonction appliquant l'algorithme de Ford-Fulkerson à un graphe
# Les noms des sommets sources est puits sont fournis en entrée
def fordFulkerson(g, sName, tName):

    s = g.indexOf(sName)
    t = g.indexOf(tName)
    if s < 0 or t < 0:
        raise ValueError("Source or sink not found in graph nodes.")

    n = g.n
    cap = g.adjacency                       
    flow = graph.Graph(g.nodes)             
    f = flow.adjacency

    max_value = 0.0
    INF = math.inf

    while True:
        mark = [None] * n                   
        mark[s] = (+1, s)                   
        q = [s]

        while q and mark[t] is None:
            u = q.pop(0)

            for v in range(n):
                if mark[v] is None and cap[u][v] != 0 and f[u][v] < cap[u][v]:
                    mark[v] = (+1, u)
                    q.append(v)

            for v in range(n):
                if mark[v] is None and cap[v][u] != 0 and f[v][u] > 0:
                    mark[v] = (-1, u)
                    q.append(v)

        if mark[t] is None:
            S_star = {i for i in range(n) if mark[i] is not None}
            T_star = set(range(n)) - S_star
            return flow, max_value, S_star, T_star

        delta = INF
        v = t
        while v != s:
            sign, pred = mark[v]
            if sign == +1:
                residual = cap[pred][v] - f[pred][v]
            else:
                residual = f[v][pred]
            if residual < delta:
                delta = residual
            v = pred

        v = t
        while v != s:
            sign, pred = mark[v]
            if sign == +1:
                f[pred][v] += delta
            else:
                f[v][pred] -= delta
            v = pred

        max_value += delta

   
if __name__ == '__main__':
    main()
