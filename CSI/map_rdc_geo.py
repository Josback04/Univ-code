import folium
from geopy.distance import geodesic
import heapq

# Coordonnées GPS des villes en RDC
coords_villes = {
    "Kinshasa": (-4.325, 15.322),
    "Matadi": (-5.815, 13.450),
    "Kikwit": (-5.040, 18.817),
    "Mbandaka": (0.048, 18.260),
    "Kananga": (-5.897, 22.417),
    "Mbuji-Mayi": (-6.151, 23.600),
    "Lubumbashi": (-11.660, 27.479),
    "Kolwezi": (-10.722, 25.472),
    "Likasi": (-10.983, 26.733),
    "Kalemie": (-5.947, 29.194),
    "Uvira": (-3.395, 29.137),
    "Bukavu": (-2.509, 28.860),
    "Goma": (-1.661, 29.232),
    "Beni": (0.491, 29.473),
    "Butembo": (0.130, 29.283),
    "Kisangani": (0.515, 25.191),
    "Isiro": (2.773, 27.616),
    "Buta": (2.801, 24.750),
    "Gemena": (3.250, 19.766),
    "Boende": (-0.281, 20.880),
}

# 
graph_RDC = {}

for ville1 in coords_villes:
    graph_RDC[ville1] = {}
    
    # Calcul des distances avec toutes les autres villes
    distances = [(ville2, geodesic(coords_villes[ville1], coords_villes[ville2]).kilometers)
                 for ville2 in coords_villes if ville1 != ville2]
    
    distances = sorted(distances, key=lambda x: x[1])[:3]

    # Ajouter les connexions optimisées au graphe
    for ville2, dist in distances:
        graph_RDC[ville1][ville2] = round(dist)

# 🔍 Algorithme Best-First Search
def bestFirstSearch(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start, []))  # (coût, ville_actuelle, chemin)

    while queue:
        cost, current_node, path = heapq.heappop(queue)
        path = path + [current_node]

        if current_node == end:
            return path, cost

        for neighbor, dist in graph[current_node].items():
            if neighbor not in path:
                heapq.heappush(queue, (dist, neighbor, path))

    return None, float('inf')

etat_initial = "Kinshasa"
etat_but = "Lubumbashi"

chemin, cout = bestFirstSearch(graph_RDC, etat_initial, etat_but)

if chemin:
    print(f'Meilleur chemin de {etat_initial} à {etat_but} : {chemin}')
    print(f'Distance totale : {cout} Km')
else:
    print(f'Aucun chemin trouvé entre {etat_initial} et {etat_but}')

# Création de la carte interactive
carte = folium.Map(location=[-2.88, 23.65], zoom_start=5)  # RDC centrée

# Ajouter les villes sur la carte
for ville, coord in coords_villes.items():
    folium.Marker(location=coord, popup=ville, icon=folium.Icon(color="blue")).add_to(carte)

# 🔗 Ajouter les routes optimisées sur la carte
for ville, voisins in graph_RDC.items():
    for voisin, distance in voisins.items():
        folium.PolyLine([coords_villes[ville], coords_villes[voisin]],
                        color="gray", weight=2.5, opacity=0.8,
                        tooltip=f"{ville} ↔ {voisin} : {distance} km").add_to(carte)

if chemin:
    for i in range(len(chemin) - 1):
        ville_depart = chemin[i]
        ville_arrivee = chemin[i + 1]
        folium.PolyLine([coords_villes[ville_depart], coords_villes[ville_arrivee]],
                        color="red", weight=4, opacity=1,
                        tooltip=f"Trajet optimal : {ville_depart} ↔ {ville_arrivee}").add_to(carte)

carte.save("carte_RDC_2.html")
