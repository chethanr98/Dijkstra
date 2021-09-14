import sys

def buildGraph(arr):
    graph = {}
    max_row = len(arr)
    max_col = len(arr[0])
    for ind_row,row in enumerate(arr):
        for ind_col,col in enumerate(arr):
            cell_name = str(ind_row) + str(ind_col)
            cell_value = col
            sub_graph = get_weights(arr,ind_row,ind_col,max_row,max_col,cell_value)
            graph[cell_name] = sub_graph
    return graph

def get_weights(arr,ind_row,ind_col,max_row,max_col,cell_value):
    weights = {}
    behind_col_ind = max(0,ind_col-1)
    front_col_ind = min(max_col-1,ind_col+1)
    above_row_ind = max(0,ind_row-1)
    below_row_ind = min(max_row-1,ind_row+1)
    if(behind_col_ind != ind_col):
        weights[str(ind_row)+str(behind_col_ind)] = NAND(cell_value,arr[ind_row][behind_col_ind])
    if(front_col_ind != ind_col):
        weights[str(ind_row)+str(front_col_ind)] = NAND(cell_value,arr[ind_row][front_col_ind])
    if(above_row_ind != ind_row):
        weights[str(above_row_ind)+str(ind_col)] = NAND(cell_value,arr[above_row_ind][ind_col])
    if(below_row_ind != ind_row):
        weights[str(below_row_ind)+str(ind_col)] = NAND(cell_value,arr[below_row_ind][ind_col])
    return weights
    
def NAND(a,b):
    if int(not (a and b)) == 1:
        return float("inf")
    else:
        return 1

def Dijkstra(graph,src):
    Q = []
    dist = {}
    prev = {}
    dist[src] = 0
    u = src
    for v in graph:
        if v != src:
            dist[v] = 1000
            prev[v] = -1
        Q.append(v)
    #print(dist)
    #print(prev)
    #print(Q)
    while len(Q) != 0:
        min = 1001
        for i in Q:
            if min > dist[i]:
                min = dist[i]
                u = i
        #print(u)
        Q.remove(u)
        
        for v in graph[u]:
            if (v in Q) & (graph[u][v] == 1):
                #print(v)
                alt = dist[u]+1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    return dist,prev

def find_path(src,dest,dist,prev):
    path = []
    node = dest
    path.append(node)
    while node != src:
        node = prev[node]
        path.append(node)
    path.reverse()
    return path


map = [[1,1,1,1,1],[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1],[0,0,1,0,0]]
graph = buildGraph(map)
print("The graph is represented by the list:")
print(graph)
print("Enter the source:")
source = raw_input()
if map[int(source[0])][int(source[1])] == 0:
    print("Not a valid source node")
    sys.exit()
#source = '42'
print("Enter the destination:")
destination = raw_input()
if map[int(destination[0])][int(destination[1])] == 0:
    print("Not a valid destination node")
    sys.exit()
#destination = '10'
distance,previous = Dijkstra(graph,source)
print("Distance calculated by the Dijkstra algorithm from source node to various nodes:")
print(distance)
print("Previous node to every node in the shortest path:")
print(previous)
path = find_path(source,destination,distance,previous)
print("The shortest path from source to destination:")
print(path)
