import folium
import heapq

# 📍 Distances entre les villes de la RDC (exemple simplifié)
graph_RDC = {
    "Kinshasa": {"Matadi": 350, "Kikwit": 525, "Mbandaka": 650, "Kananga": 950},
    "Matadi": {"Kinshasa": 350, "Kikwit": 800, "Boma": 120},
    "Kikwit": {"Kinshasa": 525, "Matadi": 800, "Kananga": 780, "Tshikapa": 400},
    "Mbandaka": {"Kinshasa": 650, "Boende": 500, "Gemena": 710},
    "Kananga": {"Kikwit": 780, "Mbuji-Mayi": 180, "Lubumbashi": 1200, "Tshikapa": 300},
    "Mbuji-Mayi": {"Kananga": 180, "Lubumbashi": 900, "Tshikapa": 250},
    "Lubumbashi": {"Mbuji-Mayi": 900, "Kolwezi": 320, "Likasi": 150, "Kasumbalesa": 200},
    "Kolwezi": {"Lubumbashi": 320, "Likasi": 120, "Kamina": 180},
    "Likasi": {"Lubumbashi": 150, "Kolwezi": 120, "Kalemie": 450, "Kamina": 100},
    "Kalemie": {"Likasi": 450, "Uvira": 260, "Kindu": 300},
    "Uvira": {"Kalemie": 260, "Bukavu": 120, "Kindu": 400},
    "Bukavu": {"Uvira": 120, "Goma": 220, "Kindu": 350},
    "Goma": {"Bukavu": 220, "Beni": 350, "Rutshuru": 80},
    "Beni": {"Goma": 350, "Butembo": 55, "Rutshuru": 120},
    "Butembo": {"Beni": 55, "Kisangani": 640, "Bunia": 200},
    "Kisangani": {"Butembo": 640, "Isiro": 515, "Bunia": 300, "Kindu": 400},
    "Isiro": {"Kisangani": 515, "Buta": 350, "Watsa": 150},
    "Buta": {"Isiro": 350, "Gemena": 430, "Bumba": 200},
    "Gemena": {"Buta": 430, "Mbandaka": 710, "Bumba": 250},
    "Boende": {"Mbandaka": 500, "Basankusu": 300},
    "Boma": {"Matadi": 120, "Muanda": 80, "Kinshasa":70},
    "Tshikapa": {"Kikwit": 400, "Kananga": 300, "Mbuji-Mayi": 250},
    "Kasumbalesa": {"Lubumbashi": 200, "Ndola": 150},  # Ndola est en Zambie
    "Kamina": {"Kolwezi": 180, "Likasi": 100, "Kabalo": 200},
    "Kindu": {"Kalemie": 300, "Uvira": 400, "Bukavu": 350, "Kisangani": 400},
    "Rutshuru": {"Goma": 80, "Beni": 120},
    "Bunia": {"Butembo": 200, "Kisangani": 300},
    "Watsa": {"Isiro": 150, "Dungu": 120},
    "Bumba": {"Buta": 200, "Gemena": 250},
    "Basankusu": {"Boende": 300, "Lisala": 200},
    "Muanda": {"Boma": 80},
    "Ndola": {"Kasumbalesa": 150},  # Ndola est en Zambie
    "Kabalo": {"Kamina": 200, "Kongolo": 150},
    "Dungu": {"Watsa": 120, "Doruma": 100},
    "Lisala": {"Basankusu": 200, "Mbandaka": 300},
    "Kongolo": {"Kabalo": 150, "Kalemie": 200},
    "Doruma": {"Dungu": 100},
}

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

# 🎯 Points de départ et d'arrivée
etat_initial = "Kinshasa"
etat_but = "Lubumbashi"

# 🚀 Exécution de l'algorithme
chemin, cout = bestFirstSearch(graph_RDC, etat_initial, etat_but)

# 🔥 Affichage du résultat
if chemin:
    print(f'✅ Meilleur chemin de {etat_initial} à {etat_but} : {chemin}')
    print(f'🔢 Distance totale : {cout} Km')
else:
    print(f'❌ Aucun chemin trouvé entre {etat_initial} et {etat_but}')

# 📌 Création de la carte interactive
carte = folium.Map(location=[-2.88, 23.65], zoom_start=5)  # RDC centrée

# 🔵 Ajouter les villes sur la carte avec des positions approximatives
coords_villes = {
    "Kinshasa": (-4.3, 15.3),
    "Matadi": (-5.8, 13.4),
    "Kikwit": (-5.0, 18.8),
    "Mbandaka": (0.0, 18.2),
    "Kananga": (-5.8, 22.4),
    "Mbuji-Mayi": (-6.1, 23.6),
    "Lubumbashi": (-11.6, 27.4),
    "Kolwezi": (-10.7, 25.4),
    "Likasi": (-10.9, 26.7),
    "Kalemie": (-5.9, 29.1),
    "Uvira": (-3.3, 29.1),
    "Bukavu": (-2.5, 28.8),
    "Goma": (-1.6, 29.2),
    "Beni": (0.4, 29.4),
    "Butembo": (0.1, 29.2),
    "Kisangani": (0.5, 25.1),
    "Isiro": (2.7, 27.6),
    "Buta": (2.8, 24.7),
    "Gemena": (3.2, 19.7),
    "Boende": (-0.2, 20.8),
    "Boma": (-5.8, 13.0), 
    "Tshikapa": (-6.4, 20.8),  
    "Kasumbalesa": (-12.0, 27.8),  
    "Kamina": (-8.7, 25.0),  
    "Kindu": (-2.9, 25.9),  
    "Rutshuru": (-1.2, 29.4),  
    "Bunia": (1.5, 30.2),  
    "Watsa": (3.0, 29.5),  
    "Bumba": (2.2, 22.5),  
    "Basankusu": (1.2, 19.8),  
    "Muanda": (-5.9, 12.4),  
    "Ndola": (-12.9, 28.6),  
    "Kabalo": (-6.1, 26.9),  
    "Dungu": (3.6, 28.9),  
    "Lisala": (2.1, 21.5),  
    "Kongolo": (-5.4, 27.0),  
    "Doruma": (4.0, 29.0),  
}

for ville, coord in coords_villes.items():
    folium.Marker(location=coord, popup=ville, icon=folium.Icon(color="blue")).add_to(carte)

# 🔗 Ajouter les routes optimisées sur la carte
for ville, voisins in graph_RDC.items():
    for voisin, distance in voisins.items():
        folium.PolyLine([coords_villes[ville], coords_villes[voisin]],
                        color="gray", weight=2.5, opacity=0.8,
                        tooltip=f"{ville} ↔ {voisin} : {distance} km").add_to(carte)

# 🛣️ Tracer le chemin optimal trouvé par Best-First Search en rouge
if chemin:
    for i in range(len(chemin) - 1):
        ville_depart = chemin[i]
        ville_arrivee = chemin[i + 1]
        folium.PolyLine([coords_villes[ville_depart], coords_villes[ville_arrivee]],
                        color="red", weight=4, opacity=1,
                        tooltip=f"Trajet optimal : {ville_depart} ↔ {ville_arrivee}").add_to(carte)

# 📌 Sauvegarde et affichage de la carte
carte.save("carte_RDC_3.html")