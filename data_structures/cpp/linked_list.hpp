#include <iostream>
using namespace std;

template<class T>
class LinkedList{

    int _size;
    T popLastNode();
    
    public:

    ~LinkedList<T>();

    class Node {
        public:
        Node *next;
        Node *prev;
        T val;
    };

    int size();
    Node *head;
    Node *tail;
    void addHead(T);
    void addTail(T);
    T popHead();
    T popTail();
    T peekHead();
    T peekTail();
    void display();
    
};

template<class T>
int LinkedList<T>::size() {
    return _size;
}

template<class T>
LinkedList<T>::~LinkedList<T>() {
    auto node = head;
    while (node != nullptr) {
        auto oldNode = node;
        node = node->next;
        delete oldNode; 
    }
}

template<class T>
void LinkedList<T>::addHead(T item) {
    

    Node *node = new Node();
    node->val = item;

    if (size() == 0) {
        head = node;
        tail = node;
    } else {
        node->next = head;
        head->prev = node;
        head = node;
    }
    _size ++;
}

template<class T>
void LinkedList<T>::addTail(T item) {
    Node *node = new Node();
    node->val = item;

    if (size() == 0) {
        head = node;
        tail = node;
    } else {
        node->prev = tail;
        tail->next = node;
        tail = node;
    }
    _size ++;
}

template<class T>
T LinkedList<T>::popLastNode() {
    auto x = head->val;
    delete head;
    head = nullptr;
    tail = nullptr;
    return x;
}

template<class T>
T LinkedList<T>::popHead() {
    _size --;

    if (_size == 0) {
        return popLastNode();
    }

    auto oldNode = head;
    auto x = oldNode->val;
    head = oldNode->next;
    head->prev = nullptr;
    oldNode->next = nullptr;
    delete oldNode;

    return x;
}

template<class T>
T LinkedList<T>::popTail() {
    _size --;

    if (_size == 0) {
        return popLastNode();
    }

    auto oldNode = tail;
    auto x = oldNode->val;
    tail = oldNode->prev;
    tail->next = nullptr;
    oldNode->prev = nullptr;
    delete oldNode;

    return x;
}

template<class T>
T LinkedList<T>::peekHead() {
    return head->val;
}

template<class T>
T LinkedList<T>::peekTail() {
    return tail->val;
}

template<class T>
void LinkedList<T>::display() {
    cout << "[";
    auto node = head;
    while (node != nullptr) {
        cout << node->val;
        node = node->next;
        if (node != nullptr) {
            cout << " -> ";
        }
    }
    cout << "]" << endl;
}