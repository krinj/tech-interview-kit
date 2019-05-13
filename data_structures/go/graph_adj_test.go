package ds

import (
	"testing"
)

func TestGraphAdj(t *testing.T) {
	graph := NewGraphAdj()
	graph.Display()

	graph.AddVertex("A")
	graph.AddVertex("B")
	graph.AddVertex("C")

	graph.AddEdge("C", "B")
	graph.AddEdge("B", "C")
	graph.AddEdge("A", "D")
	graph.AddEdge("A", "E")
	graph.AddEdge("A", "G")

	graph.RemoveEdge("A", "D")
	graph.RemoveVertex("E")

	graph.Display()
}
