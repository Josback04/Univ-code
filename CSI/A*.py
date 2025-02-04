graph_USA={
    'Los_Angeles' : {
        'Chicago' : 2500,
        'Houston' : 700,
        'New_York_City' :800
    }, 
    'Chicago' : {
        'Houston' : 400,
        'New_York_City' :300,
        'Los_Angeles':700,
        'Miami':2200
    },
    'Houston':{
        'New_York_City':1200,
        'Chicago':400,
        'Los_Angeles':700,
        'Miami':600
    },
    'New_York_City':{
        'Los_Angeles':800,
        'Chicago':300,
        'Houston':1200
    },
    'Miami':{
        'Chicago':2200,
        'Houston':600
    }
}

def bestFirstSearch(graph, start, end):
    villes=[]
    current_node=start
    chemin=[start]
    cout=0

    while current_node  is not end:
        villes.append(current_node)
        neighbors=graph[current_node]

        min_cout=float('inf')
        next_node= None
        for neighbor, dist in neighbors.items():
            if neighbor not in villes and dist < min_cout:
                min_cout=dist
                next_node=neighbor

        if next_node is None:
            return None, float('inf')

        cout += min_cout
        chemin.append(next_node)
        current_node=next_node
    return chemin, cout 

Etat_initial = 'Houston'
Etat_but= 'Los_Angeles'


chm, cost = bestFirstSearch(graph_USA, Etat_initial, Etat_but)

if chm:
    print('Chemin pour quitter ', Etat_initial, 'à ', Etat_but, ':', chm)
    print('Cout du chemin : ', cost, 'Km')

else:
    print('Il n\'y a pas de chemin possible entre ', Etat_initial, 'et ', Etat_but)