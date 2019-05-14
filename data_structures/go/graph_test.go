package ds

import (
	"testing"

	"gotest.tools/assert"
)

func KeyExistsInList(key string, arr []string) bool {
	for _, k := range arr {
		if k == key {
			return true
		}
	}
	return false
}

func TestGraphAdd(t *testing.T) {
	g := NewDirectedGraph()

	assert.Equal(t, 0, g.VertexCount())
	assert.Equal(t, true, g.GetVertex("A") == nil)

	g.AddVertexData("A", 155)
	assert.Equal(t, 1, g.VertexCount())
	assert.Equal(t, 155, g.GetVertex("A").Data)
}

func TestGraphDirected(t *testing.T) {
	g := NewUndirectedGraph()
	g.AddEdge("A", "B")
	g.AddEdge("A", "C")
	assert.Equal(t, 3, g.VertexCount())
	assert.Equal(t, 2, g.EdgeCount())
	assert.Equal(t, true, g.IsAdjacent("A", "B"))
	assert.Equal(t, true, g.IsAdjacent("B", "A"))
	assert.Equal(t, true, g.IsAdjacent("A", "C"))
	assert.Equal(t, true, g.IsAdjacent("C", "A"))
	assert.Equal(t, false, g.IsAdjacent("C", "B"))

	g.RemoveEdge("B", "A")
	assert.Equal(t, 1, g.EdgeCount())
}

func TestGraphAdjacency(t *testing.T) {

	g := NewUndirectedGraph()
	g.AddEdge("A", "B")
	g.AddEdge("B", "C")
	g.AddEdge("A", "D")
	g.AddEdge("D", "E")
	g.AddVertex("X")

	neighbors := g.GetAdjacentKeys("A")
	assert.Equal(t, 2, len(neighbors))
	assert.Equal(t, true, KeyExistsInList("D", neighbors))
	assert.Equal(t, true, KeyExistsInList("B", neighbors))

	neighbors = g.GetAdjacentKeys("D")
	assert.Equal(t, 2, len(neighbors))
	assert.Equal(t, true, KeyExistsInList("E", neighbors))
	assert.Equal(t, true, KeyExistsInList("A", neighbors))

	neighbors = g.GetAdjacentKeys("X")
	assert.Equal(t, 0, len(neighbors))

	assert.Equal(t, true, g.IsAdjacent("A", "B"))
	assert.Equal(t, true, g.IsAdjacent("B", "C"))
	assert.Equal(t, false, g.IsAdjacent("A", "C"))

}

func TestGraphEdges(t *testing.T) {
	g := NewDirectedGraph()
	g.AddEdge("A", "B")
	g.AddEdge("B", "C")
	g.AddEdge("A", "C")

	assert.Equal(t, 3, g.VertexCount())
	assert.Equal(t, 3, g.EdgeCount())

	g.RemoveVertex("B")
	assert.Equal(t, 2, g.VertexCount())
	assert.Equal(t, 1, g.EdgeCount())
}

func TestGraphDisplay(t *testing.T) {
	g := NewUndirectedGraph()
	g.AddEdge("A", "B")
	g.AddEdge("B", "C")
	g.AddEdge("A", "D")
	g.AddEdge("D", "E")
	g.AddVertex("X")
	g.Display()
}

func TestGraphEdgeWeight(t *testing.T) {
	g := NewUndirectedGraph()
	g.AddEdgeWithWeight("A", "B", 5)
	g.AddEdgeWithWeight("B", "C", 12)

	assert.Equal(t, 5.0, g.GetEdgeWeight("B", "A"))
	assert.Equal(t, 12.0, g.GetEdgeWeight("B", "C"))
}
