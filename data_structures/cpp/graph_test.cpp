#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <iostream>
#include <string>
#include "graph.hpp"

bool KeyExistsInVector(string key, vector<string>& arr) {
    for (auto x : arr) {
        if (x == key) {
            return true;
        }
    }
    return false;
}

TEST_CASE("Can Add Nodes", "[Graph]") {
    auto g = new Graph<int>(true);
    REQUIRE(g->VertexCount() == 0);
    REQUIRE(g->GetVertex("A") == NULL);
    g->AddVertexData("A", 155);
    REQUIRE(g->VertexCount() == 1);
    REQUIRE(g->GetData("A") == 155);
    REQUIRE(g->GetVertex("A")->data == 155);
    delete g;
}

TEST_CASE("Directed Graph", "[Graph]") {
    auto g = new Graph<int>(false);
    g->AddEdge("A", "B");
    g->AddEdge("A", "C");
    REQUIRE(g->VertexCount() == 3);
    REQUIRE(g->EdgeCount() == 2);
    REQUIRE(g->IsAdjacent("A", "B"));
    REQUIRE(g->IsAdjacent("B", "A"));
    REQUIRE(g->IsAdjacent("A", "C"));
    REQUIRE(g->IsAdjacent("C", "A"));
    REQUIRE_FALSE(g->IsAdjacent("C", "B"));

    g->RemoveEdge("B", "A");
    REQUIRE(g->EdgeCount() == 1);
}

TEST_CASE("Test Graph Adjacency", "[Graph]") {

    auto g = new Graph<int>(false);
    g->AddEdge("A", "B");
	g->AddEdge("B", "C");
	g->AddEdge("A", "D");
	g->AddEdge("D", "E");
	g->AddVertex("X");

    auto neighbors = g->GetAdjacentKeys("A");
    REQUIRE(neighbors.size() == 2);
    REQUIRE(KeyExistsInVector("B", neighbors));
    REQUIRE(KeyExistsInVector("D", neighbors));

    neighbors = g->GetAdjacentKeys("D");
    REQUIRE(neighbors.size() == 2);
    REQUIRE(KeyExistsInVector("E", neighbors));
    REQUIRE(KeyExistsInVector("A", neighbors));

    neighbors = g->GetAdjacentKeys("X");
    REQUIRE(neighbors.size() == 0);

    REQUIRE(g->IsAdjacent("A", "B"));
    REQUIRE(g->IsAdjacent("B", "C"));
    REQUIRE_FALSE(g->IsAdjacent("A", "C"));
}

TEST_CASE("Test Graph Edges", "[Graph]") {
    auto g = new Graph<int>();
    g->AddEdge("A", "B");
	g->AddEdge("B", "C");
	g->AddEdge("A", "C");

    REQUIRE(g->VertexCount() == 3);
    REQUIRE(g->EdgeCount() == 3);

    g->RemoveVertex("B");
    REQUIRE(g->VertexCount() == 2);
    REQUIRE(g->EdgeCount() == 1);
}

TEST_CASE("Test Graph Display", "[Graph]") {
    auto g = new Graph<int>(false);
    g->AddEdge("A", "B");
    g->AddEdge("B", "C");
	g->AddEdge("A", "D");
	g->AddEdge("D", "E");
	g->AddVertex("X");
	g->Display();
}

TEST_CASE("Test Edge Weight", "[Graph]") {
    auto g = new Graph<int>(false);
    g->AddEdge("A", "B", 5);
    g->AddEdge("B", "C", 12);

    REQUIRE(g->GetEdgeWeight("B", "A") == 5);
    REQUIRE(g->GetEdgeWeight("B", "C") == 12);
}