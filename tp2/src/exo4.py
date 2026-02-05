import numpy as np
import graph
import fordFulkerson


base_nodes = ["s", "a", "g", "e", "b", "c", "h", "f", "d", "t"]
base_arcs = [
    ("s", "a"),
    ("s", "g"),
    ("s", "e"),
    ("a", "b"),
    ("a", "c"),
    ("g", "b"),
    ("g", "c"),
    ("e", "c"),
    ("e", "h"),
    ("c", "b"),
    ("c", "f"),
    ("h", "c"),
    ("b", "d"),
    ("d", "t"),
    ("f", "t"),
    ("h", "t"),
]


def build_arc_disjoint_graph():
    g = graph.Graph(np.array(base_nodes))
    for u, v in base_arcs:
        g.addArc(u, v, 1)
    return g


def build_vertex_disjoint_graph():
    nodes = ["s", "t"]
    for v in base_nodes:
        if v in ("s", "t"):
            continue
        nodes.append(f"{v}_in")
        nodes.append(f"{v}_out")

    g = graph.Graph(np.array(nodes))

    for v in base_nodes:
        if v in ("s", "t"):
            continue
        g.addArc(f"{v}_in", f"{v}_out", 1)

    for u, v in base_arcs:
        src = u if u in ("s", "t") else f"{u}_out"
        dst = v if v in ("s", "t") else f"{v}_in"
        g.addArc(src, dst, 1)

    return g


def run(name, g, s="s", t="t"):
    flow, max_value, s_star, t_star = fordFulkerson.fordFulkerson(g, s, t)
    print(name)
    print("Max flow:", max_value)
    print("Flow graph:")
    print(flow)
    print("S*:", [g.nodes[i] for i in sorted(s_star)])
    print("T*:", [g.nodes[i] for i in sorted(t_star)])
    print()


run("Arc-disjoint (unit capacities on arcs)", build_arc_disjoint_graph())
run("Vertex-disjoint (node splitting with unit capacities)", build_vertex_disjoint_graph())
