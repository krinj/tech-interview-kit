#include <functional>

using namespace std;

template<class K, class V>
class HashMap {

    struct Node {
        K key;
        V val;
        bool occupied;
        Node * next;
    };
    Node** storage_;
    int size_;
    int capacity_;
    int limit_;
    void Resize(int new_size);
    hash<K> hash_func_;
    int SetInternal_(K key, V value, Node** storage, int capacity);
    void DeleteNodes_();
    
public:

    HashMap();
    ~HashMap();
    void Set(K key, V value);
    V Get(K key);
    int Size();
    int Capacity();
    int GetHashIndex(K key, int capacity_target);
    void Display();

};

template<class K, class V>
HashMap<K, V>::HashMap() {
    size_ = 0;
    capacity_ = 0;
    limit_ = 0;
    Resize(8);
}

template<class K, class V>
HashMap<K, V>::~HashMap() {
    DeleteNodes_();
    delete storage_;
}

template<class K, class V>
void HashMap<K, V>::DeleteNodes_() {
    for (int i = 0; i < capacity_; i++) {
        auto node = storage_[i];
        while (node->occupied) {
            auto delete_node = node;
            node = node->next;
            delete delete_node;
        }
    }
}


template<class K, class V>
void HashMap<K, V>::Resize(int new_size) {
    // Create an array with new size, of Node pointers.
    Node** new_storage = (Node**)calloc(new_size, sizeof(Node *));
    for (int i = 0; i < new_size; i++) {
        new_storage[i] = new Node();
    }

    // Move all nodes over from the previous storage.
    for (int i = 0; i < capacity_; i++) {
        auto old_node = storage_[i];
        while (old_node->occupied) {
            SetInternal_(old_node->key, old_node->val, new_storage, new_size);
            old_node = old_node->next;
        }
    }

    // Clear the old nodes.
    DeleteNodes_();

    // Set the new limit and storage.
    limit_ = new_size;
    capacity_ = new_size;
    storage_ = new_storage;
}

template<class K, class V>
int HashMap<K, V>::GetHashIndex(K key, int target_capacity) {
    auto hash_index = hash_func_(key) % target_capacity;
    return hash_index;
}

template<class K, class V>
int HashMap<K, V>::SetInternal_(K key, V value, Node** storage, int capacity) {
    int index = GetHashIndex(key, capacity);
    auto node = storage[index];

    while (node->occupied && node->key != key) {
        node = node->next;
    }

    node->val = value;
    node->key = key;

    if (!node->occupied) {
        node->occupied = true;
        auto new_node = new Node();
        new_node->occupied = false;
        node->next = new_node;
        return 1;
    } else {
        return 0;
    }
}

template<class K, class V>
void HashMap<K, V>::Set(K key, V value) {
    int index = GetHashIndex(key, capacity_);
    auto node = storage_[index];
    size_ += SetInternal_(key, value, storage_, capacity_);

    if (size_ >= limit_) {
        Resize(capacity_ * 2);
    }
}

template<class K, class V>
V HashMap<K, V>::Get(K key) {
    int index = GetHashIndex(key, capacity_);
    auto node = storage_[index];
    while (node->key != key) {

        node = node->next;
        if (!node->occupied) {
            throw "No key in this dictionary!";
        }
    }
    return node->val;
}

template<class K, class V>
int HashMap<K, V>::Size() {
    return size_;
}

template<class K, class V>
int HashMap<K, V>::Capacity() {
    return capacity_;
}

template<class K, class V>
void HashMap<K, V>::Display() {
    for (int i = 0; i < capacity_; i++) {
        auto node = storage_[i];
        cout << i << ": " << "[";
        while (node->occupied) {
            cout << node->key << "(" << node->val << ")";
            node = node->next;
            if (node->occupied) {
                cout << " -> ";
            }
        }
        cout << "]" << endl;
    }
    cout << endl;
    cout << "Size: " << size_ << endl;
    cout << "Capacity: " << capacity_ << endl;
    cout << "Limit: " << limit_ << endl;
}