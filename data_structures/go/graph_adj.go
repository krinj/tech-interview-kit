package ds

import "fmt"

type EdgeAdj struct {
	VertexFrom string
	VertexTo   string
}

type GraphAdj struct {
	vertices map[string]bool
	edges    []EdgeAdj
}

func NewGraphAdj() GraphAdj {
	graph := GraphAdj{
		vertices: make(map[string]bool, 0),
		edges:    make([]EdgeAdj, 0),
	}
	return graph
}

func (g *GraphAdj) AddVertex(x string) {
	g.vertices[x] = true
}

func (g *GraphAdj) RemoveVertex(x string) {
	if _, ok := g.vertices[x]; ok {
		delete(g.vertices, x)

		// Rebuild edges.
		new_edges := make([]EdgeAdj, 0, len(g.edges))
		for i := len(g.edges) - 1; i >= 0; i-- {
			edge := g.edges[i]
			if edge.VertexFrom != x && edge.VertexTo != x {
				new_edges = append(new_edges, edge)
			}
		}
		g.edges = new_edges
	}
}

func (g *GraphAdj) AddEdge(x string, y string) {
	g.vertices[x] = true
	g.vertices[y] = true

	// If the edge already exists.
	for _, edge := range g.edges {
		if edge.VertexFrom == x && edge.VertexTo == y {
			return
		}
	}

	// Add the edge.
	edge := EdgeAdj{VertexFrom: x, VertexTo: y}
	g.edges = append(g.edges, edge)
}

func (g *GraphAdj) RemoveEdge(x string, y string) {
	for i, edge := range g.edges {
		if edge.VertexFrom == x && edge.VertexTo == y {
			g.edges = append(g.edges[:i], g.edges[i+1:]...)
			break
		}
	}
}

func (g *GraphAdj) VertexCount() int {
	return len(g.vertices)
}

func (g *GraphAdj) EdgesCount() int {
	return len(g.edges)
}

func (g *GraphAdj) Display() {

	if g.VertexCount() == 0 {
		fmt.Println("--- No Vertices ---")
	} else {
		fmt.Printf("Vertices: [")
		i := 0
		for k := range g.vertices {
			fmt.Printf("%v", k)
			if i < len(g.vertices)-1 {
				fmt.Printf(", ")
			}
			i++
		}
		fmt.Println("]")
	}

	if g.EdgesCount() == 0 {
		fmt.Println("--- No Edges ---")
	} else {
		for _, edge := range g.edges {
			fmt.Printf("%v -> %v\n", edge.VertexFrom, edge.VertexTo)
		}
	}
}
