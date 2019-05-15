package ds

import "fmt"

type Vertex struct {
	Key   string
	Data  interface{}
	Edges map[string]float64
}

type Graph struct {
	Directed      bool
	DefaultWeight float64
	vertexMap     map[string]*Vertex
	numberOfEdges int
}

func NewGraph(directed bool) *Graph {
	graph := Graph{
		Directed:      directed,
		DefaultWeight: 1,
		vertexMap:     make(map[string]*Vertex, 0),
	}
	return &graph
}

func NewUndirectedGraph() *Graph {
	graph := NewGraph(false)
	return graph
}

func NewDirectedGraph() *Graph {
	graph := NewGraph(true)
	return graph
}

func (g *Graph) AddVertex(key string) {
	g.AddVertexData(key, nil)
}

func (g *Graph) AddVertexData(key string, data interface{}) {
	if v, ok := g.vertexMap[key]; ok {
		v.Data = data
	} else {
		vertex := Vertex{Key: key, Data: data, Edges: make(map[string]float64, 0)}
		g.vertexMap[key] = &vertex
	}
}

func (g *Graph) GetVertex(key string) *Vertex {
	// TODO: Handle Errors.
	return g.vertexMap[key]
}

func (g *Graph) GetData(key string) interface{} {
	// TODO: Handle Errors.
	return g.vertexMap[key].Data
}

func (g *Graph) RemoveVertex(key string) {

	// Reduce edges count.
	g.numberOfEdges -= len(g.vertexMap[key].Edges)
	delete(g.vertexMap, key)

	// Remove all associated edges.
	for _, v := range g.vertexMap {
		if _, ok := v.Edges[key]; ok {
			delete(v.Edges, key)
			g.numberOfEdges--
		}
	}
}

func (g *Graph) ensureVertex(key string) {
	if _, ok := g.vertexMap[key]; !ok {
		g.AddVertex(key)
	}
}

func (g *Graph) addEdgeWithWeightActual(keyFrom string, keyTo string, weight float64, reverse bool) {

	g.ensureVertex(keyFrom)
	g.ensureVertex(keyTo)

	vertex := g.vertexMap[keyFrom]

	// Increment Edge Count.
	if _, ok := vertex.Edges[keyTo]; !ok {
		g.numberOfEdges++
	}

	// Set the Edge.
	vertex.Edges[keyTo] = weight

	// If not directed, also add/modify the mirror.
	if reverse {
		g.addEdgeWithWeightActual(keyTo, keyFrom, weight, false)
	}
}

func (g *Graph) AddEdgeWithWeight(keyFrom string, keyTo string, weight float64) {
	g.addEdgeWithWeightActual(keyFrom, keyTo, weight, !g.Directed)
}

func (g *Graph) AddEdge(keyFrom string, keyTo string) {
	g.AddEdgeWithWeight(keyFrom, keyTo, g.DefaultWeight)
}

func (g *Graph) removeEdgePrivate(keyFrom string, keyTo string, reverse bool) {
	vertex := g.vertexMap[keyFrom]

	if _, ok := vertex.Edges[keyTo]; ok {
		delete(vertex.Edges, keyTo)
		g.numberOfEdges--
	}

	// If not directed, also add/modify the mirror.
	if reverse {
		g.removeEdgePrivate(keyTo, keyFrom, false)
	}
}

func (g *Graph) RemoveEdge(keyFrom string, keyTo string) {
	g.removeEdgePrivate(keyFrom, keyTo, !g.Directed)
}

func (g *Graph) IsAdjacent(keyFrom string, keyTo string) bool {
	vertex := g.vertexMap[keyFrom]
	if _, ok := vertex.Edges[keyTo]; ok {
		return true
	}
	return false
}

func (g *Graph) GetEdgeWeight(keyFrom string, keyTo string) float64 {
	vertex := g.vertexMap[keyFrom]
	if w, ok := vertex.Edges[keyTo]; ok {
		return w
	}
	return 0
}

func (g *Graph) GetAdjacent(key string) map[string]float64 {
	vertex := g.vertexMap[key]
	return vertex.Edges
}

func (g *Graph) GetAdjacentKeys(key string) []string {
	vertex := g.vertexMap[key]
	keyList := make([]string, 0)

	for k, _ := range vertex.Edges {
		keyList = append(keyList, k)
	}
	return keyList
}

func (g *Graph) VertexCount() int {
	return len(g.vertexMap)
}

func (g *Graph) EdgeCount() int {
	if g.Directed {
		return g.numberOfEdges
	} else {
		return g.numberOfEdges / 2
	}
}

func (g *Graph) Display() {
	fmt.Println("\n--- GRAPH ---")
	fmt.Printf("\n--- VERTS: %v ---\n", g.VertexCount())

	if g.VertexCount() > 0 {
		i := 0
		for k, _ := range g.vertexMap {
			fmt.Printf("%v", k)
			if i < len(g.vertexMap)-1 {
				fmt.Print(" ")
			}
		}
		fmt.Print("\n")
	}

	fmt.Printf("\n--- EDGES: %v ---\n", g.EdgeCount())
	if g.EdgeCount() > 0 {
		seenMap := make(map[string]string, 0)
		for k, v := range g.vertexMap {
			for k2, w := range v.Edges {

				if linkedKey, ok := seenMap[k]; ok && linkedKey == k2 {
					continue
				}

				seenMap[k2] = k

				if !g.Directed {
					fmt.Printf("%v <--%v--> %v\n", k, w, k2)
				} else {
					fmt.Printf("%v ---%v--> %v\n", k, w, k2)
				}
			}
		}
		fmt.Print("\n")
	}
}
