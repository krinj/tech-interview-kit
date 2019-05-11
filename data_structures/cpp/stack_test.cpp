#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "stack.hpp"
#include <iostream>

using namespace std;


TEST_CASE("Stack Works Completely", "[Stack]") {
    cout << "Hello World" << endl;

    Stack<int> stack;

    REQUIRE(stack.IsEmpty() == true);

    stack.Push(2);
    stack.Push(5);
    stack.Push(12);
    stack.Push(40);

    REQUIRE(stack.IsEmpty() == false);
    REQUIRE(stack.Size() == 4);

    REQUIRE(stack.Peek() == 40);
    REQUIRE(stack.Pop() == 40);
    REQUIRE(stack.Pop() == 12);

    REQUIRE(stack.Size() == 2);
    REQUIRE(stack.Peek() == 5);
    REQUIRE(stack.Pop() == 5);
    REQUIRE(stack.Pop() == 2);

    REQUIRE(stack.IsEmpty() == true);

    stack.Push(12);
    stack.Push(40);
}