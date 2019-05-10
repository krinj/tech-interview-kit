#include <bits/stdc++.h>

using namespace std;

int main() {

    // Hash Map
    unordered_map<string, int> map;

    map["hello"] = 10;
    cout << map["hello"] << endl;
    cout << map.size() << endl;

    map["world"] = 2;
    cout << map.size() << endl;

    map.clear();
    cout << map.size() << endl;

    // Hash Set
    unordered_set<string> test_set;
    cout << "Set Size: " << test_set.size() << endl;

    test_set.insert("hello");
    cout << "Set Size: " << test_set.size() << endl;

    auto is_in_set = test_set.find("hello") != test_set.end();
    cout << "Hello in Set: " << is_in_set << endl;

    test_set.erase("hello");
    is_in_set = test_set.find("hello") != test_set.end();
    cout << "Hello in Set: " << is_in_set << endl;
    
    return 0;
}