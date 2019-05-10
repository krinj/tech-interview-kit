#include <bits/stdc++.h>
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "linked_list.hpp"

using namespace std;

TEST_CASE("Can add items to LL.", "[LinkedList]") {
    LinkedList<int> ll;
    ll.addHead(1);
    ll.addHead(3);
    ll.addHead(5);
    REQUIRE(ll.size() == 3);

    ll.addTail(2);
    ll.addTail(4);
    ll.addTail(6);
    REQUIRE(ll.size() == 6);
}

TEST_CASE("Can pop items from LL.", "[LinkedList]") {
    LinkedList<int> ll;
    ll.addTail(1);
    ll.addTail(3);
    ll.addTail(5);

    REQUIRE(ll.popHead() == 1);
    REQUIRE(ll.popTail() == 5);
    REQUIRE(ll.popHead() == 3);
    REQUIRE(ll.size() == 0);
}

TEST_CASE("We can display items.", "[LinkedList]") {
    LinkedList<int> ll;
    ll.addTail(1);
    ll.addTail(3);
    ll.addTail(5);
    ll.addHead(4);
    ll.addHead(2);
    ll.addHead(6);
    ll.display();
}