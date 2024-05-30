import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("User", pos=(0, 1))
G.add_node("Input", pos=(0, 0.7))
G.add_node("API Calls", pos=(0, 0.4))
G.add_node("Data Processing", pos=(0, 0.1))
G.add_node("Machine Learning", pos=(0, -0.2))
G.add_node("Output", pos=(0, -0.5))
G.add_node("User Data", pos=(0, 0.7))

# Add edges
G.add_edge("User", "Input")
G.add_edge("Input", "API Calls")
G.add_edge("API Calls", "Data Processing")
G.add_edge("Data Processing", "Machine Learning")
G.add_edge("Machine Learning", "Output")
G.add_edge("User Data", "Data Processing")

# Get node positions
pos = nx.get_node_attributes(G, 'pos')

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='skyblue')

# Draw edges
nx.draw_networkx_edges(G, pos, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Set plot title
plt.title("High-Level Design Diagram")

# Remove axes
plt.axis('off')

# Show plot
plt.show()
