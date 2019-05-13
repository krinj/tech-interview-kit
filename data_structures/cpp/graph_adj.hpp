#include <vector>
#include <unordered_set>

using namespace std;

template <class T>
class GraphAdj {

    struct EdgeAdj {
        T vertexFrom;
        T vertexTo;
    };

    vector<EdgeAdj> edges_;
    unordered_set<T> vertices_;

public:

    ~GraphAdj();

    void AddVertex(T x);
    void RemoveVertex(T x);

    void AddEdge(T x, T y);
    void RemoveEdge(T x, T y);

    void Display();

    int VertexCount();
    int EdgesCount();

};

template <class T>
GraphAdj<T>::~GraphAdj() {

}

template <class T>
void GraphAdj<T>::AddVertex(T x) {
    vertices_.insert(x);
}

template <class T>
void GraphAdj<T>::RemoveVertex(T x) {
    vertices_.erase(x);

    for (int i = edges_.size() - 1; i >= 0; i--) {
        auto edge = edges_[i];
        if (edge.vertexFrom == x || edge.vertexTo == x) {
            edges_.erase(edges_.begin() + i);
        }
    }
}

template <class T>
void GraphAdj<T>::AddEdge(T x, T y) {

    // Check if edge isn't already in the vector.
    for (int i = 0; i < edges_.size(); i++) {
        auto edge = edges_[i];
        if (edge.vertexFrom == x && edge.vertexTo == y) {
            return;
        }
    }

    EdgeAdj edge;
    edge.vertexFrom = x;
    edge.vertexTo = y;

    AddVertex(x);
    AddVertex(y);
    edges_.push_back(edge);
}

template <class T>
void GraphAdj<T>::RemoveEdge(T x, T y) {
    for (int i = edges_.size() - 1; i >= 0; i--) {
        auto edge = edges_[i];
        if (edge.vertexFrom == x && edge.vertexTo == y) {
            edges_.erase(edges_.begin() + i);
            return;
        }
    }
}

template <class T>
void GraphAdj<T>::Display() {
    if (VertexCount() == 0) {
        cout << "--- No Vertices ---" << endl;
    } else {
        cout << "Vertices: [";
        int i = 0;
        for (auto x : vertices_ ) {
            cout << x;
            if (i < VertexCount() - 1) {
                cout << ", ";
            }
            i ++;
        }
        cout << "]" << endl;
    }

    if (EdgesCount() == 0) {
        cout << "--- No Edges ---" << endl;
    } else {
        for (auto edge : edges_) {
            cout << edge.vertexFrom << " -> " << edge.vertexTo << endl;
        }
    }
}

template <class T>
int GraphAdj<T>::VertexCount() {
    return vertices_.size();
}

template <class T>
int GraphAdj<T>::EdgesCount() {
    return edges_.size();
}