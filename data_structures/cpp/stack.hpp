using namespace std;

template<class T>
class Stack {

    struct StackNode {
        T val;
        StackNode* next;
    };

    int size_;
    StackNode* tail_;

    public:
        Stack();
        ~Stack();
        void Push(T item);
        T Pop();
        T Peek();
        int Size();
        bool IsEmpty();
};

template<class T>
Stack<T>::Stack() {
    size_ = 0;
    tail_ = nullptr;
}

template<class T>
Stack<T>::~Stack() {
    while (tail_ != nullptr) {
        Pop();
    }
}

template<class T>
void Stack<T>::Push(T item) {
    auto node = new StackNode();
    node->val = item;
    
    if (tail_ != nullptr) {
        node->next = tail_;
    }

    tail_ = node;
    size_ ++;
}

template<class T>
T Stack<T>::Pop() {
    if (tail_ == nullptr) {
        throw "Cannot Pop Empty Stack!";
    } else {
        auto prev = tail_;
        T val = prev->val;
        tail_ = prev->next;
        delete prev;
        size_ --;
        return val;
    }
}

template<class T>
T Stack<T>::Peek() {
    if (tail_ == nullptr) {
        throw "Cannot Peek Empty Stack!";
    } else {
        return tail_->val;
    }
}

template<class T>
int Stack<T>::Size() {
    return size_;
}

template<class T>
bool Stack<T>::IsEmpty() {
    return Size() == 0;
}