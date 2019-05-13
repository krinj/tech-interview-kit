#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <iostream>
#include <string>
#include "graph_adj.hpp"

using namespace std;

TEST_CASE("GraphAdj Works", "[GraphAdj]") {
    GraphAdj<string> graph;
    
    graph.Display();

    graph.AddVertex("A");
	graph.AddVertex("B");
	graph.AddVertex("C");

    graph.Display();

	graph.AddEdge("C", "B");
	graph.AddEdge("B", "C");
	graph.AddEdge("A", "D");
	graph.AddEdge("A", "E");
	graph.AddEdge("A", "G");

	graph.RemoveEdge("A", "D");
	graph.RemoveVertex("E");

    graph.Display();

    cout << "V. Count: " << graph.VertexCount() << endl;
    cout << "Alles Gut!" << endl;
}