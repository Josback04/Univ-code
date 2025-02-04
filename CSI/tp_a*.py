import networkx as nx
import matplotlib.pyplot as plt

# Graph complet des distances entre 20 villes de la RDC (approximatives en km)
graph_RDC = {
    'Kinshasa': {'Matadi': 350, 'Kikwit': 525, 'Mbandaka': 650, 'Kananga': 950, 'Mbuji-Mayi': 1100, 'Lubumbashi': 2200, 'Kolwezi': 2100, 'Likasi': 2050, 'Kalemie': 1900, 'Uvira': 2000, 'Bukavu': 2100, 'Goma': 2200, 'Beni': 2250, 'Butembo': 2300, 'Kisangani': 1750, 'Isiro': 2000, 'Buta': 1650, 'Gemena': 1050, 'Boende': 750},
    'Matadi': {'Kinshasa': 350, 'Kikwit': 875, 'Mbandaka': 1000, 'Kananga': 1300, 'Mbuji-Mayi': 1450, 'Lubumbashi': 2600, 'Kolwezi': 2500, 'Likasi': 2450, 'Kalemie': 2300, 'Uvira': 2400, 'Bukavu': 2500, 'Goma': 2600, 'Beni': 2650, 'Butembo': 2700, 'Kisangani': 2150, 'Isiro': 2400, 'Buta': 2050, 'Gemena': 1450, 'Boende': 1150},
    'Kikwit': {'Kinshasa': 525, 'Matadi': 875, 'Mbandaka': 750, 'Kananga': 780, 'Mbuji-Mayi': 950, 'Lubumbashi': 2000, 'Kolwezi': 1900, 'Likasi': 1850, 'Kalemie': 1700, 'Uvira': 1800, 'Bukavu': 1900, 'Goma': 2000, 'Beni': 2050, 'Butembo': 2100, 'Kisangani': 1550, 'Isiro': 1800, 'Buta': 1450, 'Gemena': 950, 'Boende': 700},
    'Mbandaka': {'Kinshasa': 650, 'Matadi': 1000, 'Kikwit': 750, 'Kananga': 900, 'Mbuji-Mayi': 1100, 'Lubumbashi': 2100, 'Kolwezi': 2000, 'Likasi': 1950, 'Kalemie': 1800, 'Uvira': 1900, 'Bukavu': 2000, 'Goma': 2100, 'Beni': 2150, 'Butembo': 2200, 'Kisangani': 1600, 'Isiro': 1850, 'Buta': 1500, 'Gemena': 800, 'Boende': 500},
    'Kananga': {'Kinshasa': 950, 'Matadi': 1300, 'Kikwit': 780, 'Mbandaka': 900, 'Mbuji-Mayi': 180, 'Lubumbashi': 1200, 'Kolwezi': 1100, 'Likasi': 1050, 'Kalemie': 900, 'Uvira': 1000, 'Bukavu': 1100, 'Goma': 1200, 'Beni': 1250, 'Butembo': 1300, 'Kisangani': 850, 'Isiro': 1100, 'Buta': 750, 'Gemena': 650, 'Boende': 600},
    'Mbuji-Mayi': {'Kinshasa': 1100, 'Matadi': 1450, 'Kikwit': 950, 'Mbandaka': 1100, 'Kananga': 180, 'Lubumbashi': 900, 'Kolwezi': 800, 'Likasi': 750, 'Kalemie': 700, 'Uvira': 800, 'Bukavu': 900, 'Goma': 1000, 'Beni': 1050, 'Butembo': 1100, 'Kisangani': 650, 'Isiro': 900, 'Buta': 550, 'Gemena': 800, 'Boende': 700},
    'Lubumbashi': {'Kinshasa': 2200, 'Matadi': 2600, 'Kikwit': 2000, 'Mbandaka': 2100, 'Kananga': 1200, 'Mbuji-Mayi': 900, 'Kolwezi': 320, 'Likasi': 150, 'Kalemie': 1100, 'Uvira': 1200, 'Bukavu': 1300, 'Goma': 1400, 'Beni': 1450, 'Butembo': 1500, 'Kisangani': 1050, 'Isiro': 1300, 'Buta': 1150, 'Gemena': 1700, 'Boende': 1600},
    'Kolwezi': {'Kinshasa': 2100, 'Matadi': 2500, 'Kikwit': 1900, 'Mbandaka': 2000, 'Kananga': 1100, 'Mbuji-Mayi': 800, 'Lubumbashi': 320, 'Likasi': 120, 'Kalemie': 1000, 'Uvira': 1100, 'Bukavu': 1200, 'Goma': 1300, 'Beni': 1350, 'Butembo': 1400, 'Kisangani': 950, 'Isiro': 1200, 'Buta': 1050, 'Gemena': 1600, 'Boende': 1500},
    'Likasi': {'Kinshasa': 2050, 'Matadi': 2450, 'Kikwit': 1850, 'Mbandaka': 1950, 'Kananga': 1050, 'Mbuji-Mayi': 750, 'Lubumbashi': 150, 'Kolwezi': 120, 'Kalemie': 950, 'Uvira': 1050, 'Bukavu': 1150, 'Goma': 1250, 'Beni': 1300, 'Butembo': 1350, 'Kisangani': 900, 'Isiro': 1150, 'Buta': 1000, 'Gemena': 1550, 'Boende': 1450},
'Boende': {'Kinshasa': 750, 'Mbandaka': 500, 'Gemena': 900, 'Buta': 950, 'Isiro': 1100, 'Kisangani': 1200, 'Kananga': 600, 'Mbuji-Mayi': 700},
    'Gemena': {'Kinshasa': 1050, 'Boende': 900, 'Buta': 800, 'Isiro': 950, 'Kisangani': 1150, 'Mbandaka': 800},
    'Buta': {'Kinshasa': 1650, 'Boende': 950, 'Gemena': 800, 'Isiro': 500, 'Kisangani': 650},
    'Isiro': {'Kinshasa': 2000, 'Boende': 1100, 'Gemena': 950, 'Buta': 500, 'Kisangani': 550, 'Butembo': 850, 'Beni': 950},
    'Kisangani': {'Kinshasa': 1750, 'Boende': 1200, 'Gemena': 1150, 'Buta': 650, 'Isiro': 550, 'Butembo': 750, 'Beni': 850, 'Goma': 1300},
    'Butembo': {'Kinshasa': 2300, 'Isiro': 850, 'Kisangani': 750, 'Beni': 55, 'Goma': 350},
    'Beni': {'Kinshasa': 2250, 'Isiro': 950, 'Kisangani': 850, 'Butembo': 55, 'Goma': 350, 'Bukavu': 500},
    'Goma': {'Kinshasa': 2200, 'Kisangani': 1300, 'Butembo': 350, 'Beni': 350, 'Bukavu': 220, 'Uvira': 250},
    'Bukavu': {'Kinshasa': 2100, 'Beni': 500, 'Goma': 220, 'Uvira': 120, 'Kalemie': 600},
    'Uvira': {'Kinshasa': 2000, 'Goma': 250, 'Bukavu': 120, 'Kalemie': 260, 'Lubumbashi': 1200},
    'Kalemie': {'Kinshasa': 1900, 'Bukavu': 600, 'Uvira': 260, 'Lubumbashi': 1100, 'Likasi': 950, 'Kolwezi': 1000},

}



# Algorithme Best-First Search
def bestFirstSearch(graph, start, end):
    visited = []
    current_node = start
    path = [start]
    total_cost = 0

    while current_node != end:
        visited.append(current_node)
        neighbors = graph[current_node]

        min_cost = float('inf')
        next_node = None
        for neighbor, dist in neighbors.items():
            if neighbor not in visited and dist < min_cost:
                min_cost = dist
                next_node = neighbor

        if next_node is None:
            return None, float('inf')

        total_cost += min_cost
        path.append(next_node)
        current_node = next_node

    return path, total_cost

# Points de départ et d'arrivée
etat_initial = 'Kinshasa'
etat_but = 'Lubumbashi'

# Exécution de la recherche
chemin, cout = bestFirstSearch(graph_RDC, etat_initial, etat_but)

if chemin:
    print(f'Chemin de {etat_initial} à {etat_but} :', chemin)
    print(f'Coût total du chemin : {cout} Km')
else:
    print(f'Il n\'y a pas de chemin possible entre {etat_initial} et {etat_but}')

# Tracer la carte avec les villes et connexions
G = nx.Graph()
for ville, voisins in graph_RDC.items():
    for voisin, distance in voisins.items():
        G.add_edge(ville, voisin, weight=distance)

pos = nx.spring_layout(G, seed=42)  # Disposition des villes
plt.figure(figsize=(14, 10))

nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=8, edge_color="gray")
edge_labels = {(u, v): f"{d} km" for u, v, d in G.edges(data="weight")}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

plt.title("Carte des Villes et Distances en RDC (Graph Complet)")
plt.show()
