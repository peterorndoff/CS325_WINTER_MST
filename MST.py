
# Name: Peter Orndoff
# Description: Prims Algorithm implementation. With a lot help from Explorations code LOL help.
# Date: May 6th 2023

def Prims(G):
    INF = 9999999
    # number of vertices in graph
    V = len(G)
    selected = []
    for i in range(len(G)):
        selected.append(0)
    no_edge = 0
    selected[0] = True
    tuples = []
    # print for edge and weight
    while (no_edge < V - 1):
        # For every vertex in the set S, find the all adjacent vertices
        minimum = INF
        x = 0
        y = 0
        for i in range(V): # For the amount of vertices in graph
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):
                        # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j

        tuples.append((x, y, G[x][y])) # Append Tuples to list
        selected[y] = True # Set selected to True for visited Vertices
        no_edge += 1 # increment while loop

    return tuples # Returns the amount of tuples