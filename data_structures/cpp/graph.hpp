#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;
#define G Graph<T>
typedef unordered_map<string, float> f_map_t;

template<class T>
class Graph {
    
    bool directed_;
    float default_weight_;
    int number_of_edges_;

    void EnsureVertex(string key);
    void AddEdgeHelper(string key_from, string key_to, float weight);
    void RemoveEdgeHelper(string key_from, string key_to);

public:

    struct Vertex {
        string   key;
        T        data;
        f_map_t  edges;
    };

    unordered_map<string, Vertex*> vertex_map;

    // Core
    Graph(bool directed=true, float default_weight=1);

    // Vertex
    void AddVertex(string key);
    void AddVertexData(string key, T data);
    Vertex* GetVertex(string key);
    T GetData(string key);
    void RemoveVertex(string key);
    int VertexCount();

    // Edges
    void AddEdge(string key_from, string key_to, float weight=1);
    void RemoveEdge(string key_from, string key_to);
    float GetEdgeWeight(string key_from, string key_to);
    int EdgeCount();

    // Adjacency
    bool IsAdjacent(string key_from, string key_to);
    f_map_t GetAdjacent(string key);
    vector<string> GetAdjacentKeys(string key);

    // Misc
    void Display();

};

template<class T>
G::Graph(bool directed, float default_weight) {
    directed_ = directed;
    default_weight_ = default_weight;
    number_of_edges_ = 0;
}

template<class T>
void G::AddVertex(string key) {
    T default_data;
    AddVertexData(key, default_data);
}

template<class T>
void G::AddVertexData(string key, T data) {
    if (vertex_map.find(key) == vertex_map.end()) {
        auto vertex = new Vertex();
        vertex->key = key;
        vertex->data = data;
        vertex_map[key] = vertex;
    } else {
        auto vertex = vertex_map[key];
        vertex->data = data;
    }
}

template<class T>
typename G::Vertex* G::GetVertex(string key) {
    if (vertex_map.find(key) == vertex_map.end()) {
        return NULL;
    } else {
        return vertex_map[key];
    }
}

template<class T>
T G::GetData(string key) {
    return vertex_map[key]->data;
}

template<class T>
void G::RemoveVertex(string key) {
    auto vertex = vertex_map[key];

    // Disconnect any edges connected to this.
    for (auto& pair : vertex_map) {
        auto adj_vertex = pair.second;
        if (adj_vertex->edges.find(key) != adj_vertex->edges.end()) {
            RemoveEdge(pair.first, key);
        }
    }

    // Disconnect the edges.
    number_of_edges_ -= vertex->edges.size();
    vertex_map.erase(key);
}

template<class T>
int G::VertexCount() {
    return vertex_map.size();
}

template<class T>
void G::EnsureVertex(string key) {
    if (vertex_map.find(key) == vertex_map.end()) {
        AddVertex(key);
    }
}

template<class T>
void G::AddEdgeHelper(string key_from, string key_to, float weight) {
    auto vertex_from = vertex_map[key_from];
    vertex_from->edges[key_to] = weight;
}

template<class T>
void G::AddEdge(string key_from, string key_to, float weight) {
    EnsureVertex(key_from);
    EnsureVertex(key_to);
    AddEdgeHelper(key_from, key_to, weight);
    if (!directed_) {
        AddEdgeHelper(key_to, key_from, weight);
    }
    number_of_edges_++;
}

template<class T>
void G::RemoveEdgeHelper(string key_from, string key_to) {
    auto vertex_from = vertex_map[key_from];
    vertex_from->edges.erase(key_to);
}

template<class T>
void G::RemoveEdge(string key_from, string key_to) {
    RemoveEdgeHelper(key_from, key_to);
    if (!directed_) {
        RemoveEdgeHelper(key_to, key_from);
    }
    number_of_edges_--;
}

template<class T>
float G::GetEdgeWeight(string key_from, string key_to) {
    auto vertex = vertex_map[key_from];
    if (vertex->edges.find(key_to) == vertex->edges.end()) {
        throw "No edge exists between these two nodes.";
    } else {
        return vertex->edges[key_to];
    }
}

template<class T>
int G::EdgeCount() {
    return number_of_edges_;
}

template<class T>
bool G::IsAdjacent(string key_from, string key_to) {
    auto vertex = vertex_map[key_from];
    if (vertex->edges.find(key_to) == vertex->edges.end()) {
        return false;
    } else {
        return true;
    }
}

template<class T>
f_map_t G::GetAdjacent(string key) {
    return vertex_map[key]->edges;
}

template<class T>
vector<string> G::GetAdjacentKeys(string key) {
    vector<string> results;
    auto vertex = vertex_map[key];
    for (auto& x : vertex->edges) {
        results.push_back(x.first);
    }
    return results;
}

template<class T>
void G::Display() {
    cout << endl << "--- GRAPH ---" << endl;
    cout << endl << "--- VERTS: " << VertexCount() << " ---" << endl;

    if (VertexCount() > 0) {
        int i = 0;
        for (auto& pair : vertex_map) {
            cout << pair.first;
            if (i < vertex_map.size() - 1) {
                cout << " ";
            }
            i++;
        }
        cout << endl;
    }

    cout << endl << "--- EDGES: " << EdgeCount() << " ---" << endl;
    if (EdgeCount() > 0) {
        unordered_map<string, string> seen_map;
        for (auto& v_pair : vertex_map) {

            auto k = v_pair.first;
            auto v = v_pair.second;

            for (auto& e_pair : v->edges) {
                
                auto k2 = e_pair.first;
                auto w = e_pair.second;

                if (seen_map.find(k) != seen_map.end() && seen_map[k] == k2) {
                    continue;
                }

                seen_map[k2] = k;
                if (!directed_) {
                    cout << k << " <--" << w << "--> " << k2 << endl;
                } else {
                    cout << k << " ---" << w << "--> " << k2 << endl;
                }
            }
        }
        cout << endl;
    }
}