graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

def generate_edges(graph):
  edges = []
  for node in graph:
    for neighbour in graph[node]:
       edges.append((node, neighbour))
  return edges

def find_isolated_nodes(graph):
  isolated = []
  for node in graph:
    if not graph[node]:
      isolated=isolated+[node]
  return isolated

def vertex_degree(graph,vertex):
  adj_vertices=graph[vertex]
  degree = len(adj_vertices) + adj_vertices.count(vertex)
  return degree

def graph_degree(graph):
  degree_tot=0
  for vertex in graph:
    degree_tot=degree_tot+vertex_degree(graph,vertex)
  return degree_tot

def initq():
  return []

def enq(val):
  q.append(val)

def deq():
  u=q[0]
  q.remove(q[0])
  return u

graph1 = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F','D'],
             'F': ['C']
        }

graph = {'A': ['B', 'C'],
             'B': ['A','C'],
             'C': ['A',"B"]
        }

graphw = {'A': [['B',2], ['C',4]],
             'B': [['A',2],['C',1]],
             'C': [['A',4],["B"]]
          }

graphw1 = {'A': [['B',2], ['C',3],["D",2]],
           'B': [['A',2],['D',1]],
           'C': [['A',3],["D",4]],
           "D": [["A",2],["B",1],["C",4]]
          }

def BFS(graph, start, end):
  temp_path = [start]	
  enq(temp_path)
  while q != []:
    tmp_path = deq()
    last_node = tmp_path[len(tmp_path)-1]
    print(tmp_path)
    if last_node == end:
      print ("VALID_PATH : ", tmp_path)
    for link_node in graph[last_node]:
      if link_node not in tmp_path:
        new_path = []
        new_path = tmp_path + [link_node]
        enq(new_path)

def inits():
  return []

def push(val):
  s.append(val)

def pop():
  u=s[len(s)-1]
  s.remove(s[len(s)-1])
  return u

def DFS(graph,start,end):
  temp_path = [start]	
  push(temp_path)
  while s != []:
    tmp_path = pop()
    last_node = tmp_path[len(tmp_path)-1]
    print(tmp_path)
    if last_node == end:
      print("VALID_PATH : ", tmp_path)
    for link_node in graph[last_node]:
      if link_node not in tmp_path:
        new_path = []
        new_path = tmp_path + [link_node]
        push(new_path)

def DFSR(tmp_path):
  last_node=tmp_path[len(tmp_path)-1]
  for link_node in graph[last_node]:
    if link_node not in tmp_path:
      new_path=tmp_path+[link_node]
      aux=DFSR(new_path)
      print(aux)
      return [last_node]+aux 
  return [last_node]

def add_vertex(graph,vertex):
  if vertex not in graph:
    graph[vertex] = []
  return graph

def add_edge(graph,edge):
  (vertex1, vertex2) = tuple(edge)
  if vertex1 in graph:
    graph[vertex1].append(vertex2)
  else:
    graph[vertex1] = [vertex2]
  return graph

def generate_edges_weight(graph):
  edges_weight = {}
  for node in graph:
    for neighbour in graph[node]:
       edges_weight[(node, neighbour[0])]=neighbour[1]
  return edges_weight

def generate_graph(graphw):
  graph = {}
  for node in graphw:
    aux=[]
    for neighbour in graphw[node]:
       aux=aux+[neighbour[0]]
    graph[node]=aux
  return graph

def min_edge(tree,fringe,edges_weight):
  min=10000
  for t in tree:
    for f in fringe:
      if (t,f) in edges_weight.keys():
        if edges_weight[(t,f)]<min:
          min=edges_weight[(t,f)];(tmin,fmin)=(t,f)
  return (tmin,fmin)

def prim(graphw,start):
  min=100000
  graph=generate_graph(graphw)
  edges_weight=generate_edges_weight(graphw)
  tree=[start];fringe=graph[start]
  mintree=[]
  while fringe:
    (t,f)=min_edge(tree,fringe,edges_weight)
    mintree.append((t,f))
    tree.append(f)
    fringe.remove(f)
    for a in graph[f]:
      if (a not in fringe) and (a not in tree):
        fringe.append(a)
  return mintree
def dijkstra(graph,start,end):
  D={};P={}
  for node in graph.keys():
    D[node]=100
    P[node]=""
  D[start]=0 
  unseen_nodes=graph.keys()
  while len(unseen_nodes)>0:
    shortest=None
    node=""
    for temp_node in unseen_nodes:
      if shortest==None:
        shortest=D[temp_node]
        node=temp_node
      elif D[temp_node]<shortest:
        shortest=D[temp_node]
        node=temp_node
    unseen_nodes.remove(node)
    for child_node,child_value in graph[node].items():
      if D[node]+child_value<D[child_node]:
        D[child_node]=D[node]+child_value
        P[child_node]=node 
  path=[]
  node=end
  while not(node==start):
    if path.count(node)==0:
      path.insert(0,node)
      node=P[node]
    else:
      break
  path.insert(0,start)
  return path

graphd = { "A":{"B":4,"C":3,"D":7},
            "B":{"D":1,"F":4},
            "C":{"D":3,"E":5},
            "D":{"E":2,"F":2,"G":7},
            "E":{"G":2},
            "F":{"G":4},
            "G":{},
        }

def fleury(graph,start):
  nc=start
  lr=[];sr=[];sr.append(0);sp=0
  lr.append(start)
  while graph!={}:
    if graph[nc]==[]:
      del graph[nc]
      nc=sr[sp];sp=sp-1
      lr.append(nc)
    sr.append(0)
    sp=sp+1
    sr[sp]=nc
    nca=nc
    if graph[nc][0] not in graph:
      graph[nc].remove(graph[nc][0])
    nc=graph[nc][0]
    lr.append(nc)
    graph[nca].remove(nc)
    graph[nc].remove(nca)
    if graph[nca]==[]:
      del graph[nca]
      sp=sp-1
  return lr
  
graphe = {"a" : ["u","b"],
          "b" : ["a", "u"],
          "u" : ["a", "b", "d", "c"],
          "c" : ["d","u"],
          "d" : ["c","e","u","f"],
          "e" : ["f", "d"],
          "f" : ["e","d"]
        }


  
           


