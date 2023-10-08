import networkx as nx
import matplotlib.pyplot as plt

def add_a(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)
    if not di:
        G.add_edge(v, u, weight=w)

if __name__ == '__main__':
    G = nx.DiGraph()

    add_a(G, "Q0", "Q1", "A")
    add_a(G, "Q1", "Q2", "A")
    add_a(G, "Q2", "Q3", "B")
    add_a(G, "Q3", "Q6", "B")
    add_a(G, "Q3", "Q4", "B")
    add_a(G, "Q4", "Q5", "B")
    add_a(G, "Q5", "Q7", "B")
    add_a(G, "Q5", "Q8", "A")
    add_a(G, "Q8", "Q9", "B")
    add_a(G, "Q9", "Q10", "B")
    add_a(G, "Q9", "Q11", "A")
    add_a(G, "Q11", "Q12", "B")
    add_a(G, "Q12", "Q13", "B")

    for node in ["Q6", "Q7", "Q10", "Q13"]:
        G.nodes[node]['is_accept'] = True

    pos = {
        "Q0": (1, 0),
        "Q1": (1, 1),
        "Q2": (2, 2),
        "Q3": (3, 1),
        "Q4": (5, 1),
        "Q5": (5, 0),
        "Q6": (3, 0),
        "Q7": (5, -1),
        "Q8": (8, 0),
        "Q9": (8, -1),
        "Q10": (8, -2),
        "Q11": (11, -1),
        "Q12": (14, -1),
        "Q13": (14, -2),
    }

    node_colors = ['green' if G.nodes[node].get('is_accept') else 'purple' for node in G.nodes]

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, node_color=node_colors, with_labels=True, node_size=500, font_size=10)
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("Grafo con Networkx")
    plt.show()
