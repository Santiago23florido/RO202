import numpy as np
import graph
import fordFulkerson


def graph_left():
    g = graph.Graph(np.array(["s", "1", "2", "3", "4", "t"]))
    g.addArc("s", "1", 16)
    g.addArc("s", "2", 13)
    g.addArc("1", "2", 10)
    g.addArc("2", "1", 4)
    g.addArc("1", "3", 12)
    g.addArc("3", "2", 9)
    g.addArc("2", "4", 14)
    g.addArc("4", "3", 7)
    g.addArc("3", "t", 20)
    g.addArc("4", "t", 4)
    return g


def graph_right():
    g = graph.Graph(np.array(["s", "A", "C", "E", "B", "D", "F", "t"]))
    g.addArc("s", "A", 10)
    g.addArc("s", "C", 12)
    g.addArc("s", "E", 15)
    g.addArc("A", "B", 9)
    g.addArc("A", "C", 4)
    g.addArc("A", "D", 15)
    g.addArc("C", "B", 2)
    g.addArc("C", "D", 8)
    g.addArc("C", "E", 4)
    g.addArc("E", "F", 16)
    g.addArc("D", "B", 15)
    g.addArc("D", "F", 15)
    g.addArc("F", "C", 6)
    g.addArc("B", "t", 10)
    g.addArc("D", "t", 10)
    g.addArc("F", "t", 10)
    return g


def run(name, g):
    flow, max_value, s_star, t_star = fordFulkerson.fordFulkerson(g, "s", "t")
    print(name)
    print("Max flow:", max_value)
    print("Flow graph:")
    print(flow)
    print("S*:", [g.nodes[i] for i in sorted(s_star)])
    print("T*:", [g.nodes[i] for i in sorted(t_star)])
    print()


run("Graph 1", graph_left())
run("Graph 2", graph_right())
