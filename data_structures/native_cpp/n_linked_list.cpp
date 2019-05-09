#include <list>
#include <iostream>

using namespace std;

#define PRINT(x) cout << x << endl;

int main () {

    list<int> linkedList;

    linkedList.push_back(5);
    linkedList.push_back(6);
    linkedList.push_back(7);
    PRINT(linkedList.size());

    linkedList.push_front(7);
    linkedList.push_front(1);
    linkedList.push_front(0);
    PRINT(linkedList.size());
    
    PRINT(linkedList.front()); linkedList.pop_front();
    PRINT(linkedList.back()); linkedList.pop_back();
    PRINT(linkedList.front()); linkedList.pop_front();
    PRINT(linkedList.back()); linkedList.pop_back();
    PRINT(linkedList.front()); linkedList.pop_front();
    PRINT(linkedList.back()); linkedList.pop_back();
    
    return 0;
}