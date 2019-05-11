#include <iostream>
#include <stack>

using namespace std;

#define PRINT(x, y) cout << x << ": " << y << endl;

int main() {

    stack<int> s;

    PRINT("Is Empty", s.empty());

    s.push(5);
    s.push(15);
    s.push(25);
    s.push(30);

    PRINT("Is Empty", s.empty());

    PRINT("Top", s.top());

    s.pop();
    s.pop();
    s.pop();

    PRINT("Top", s.top());
    PRINT("Size", s.size());

    return 0;
}