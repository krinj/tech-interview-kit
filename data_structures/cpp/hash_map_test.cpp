#include <bits/stdc++.h>
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "hash_map.hpp"

using namespace std;

TEST_CASE("Can insert items into hash map.", "[HashMap]") {
    HashMap<string, int> hash_map;
    hash_map.Set("A", 1);
    hash_map.Set("B", 2);
    hash_map.Set("C", 3);
    hash_map.Set("A", 5);
    REQUIRE(hash_map.Size() == 3);
}

TEST_CASE("Hash map resizes when capacity limit is reached.", "[HashMap]") {
    HashMap<string, int> hash_map;
    int original_capacity = hash_map.Capacity();
    hash_map.Set("A", 1);
    hash_map.Set("B", 2);
    hash_map.Set("C", 3);
    hash_map.Set("D", 4);
    hash_map.Set("E", 5);
    hash_map.Set("F", 6);
    hash_map.Set("G", 7);
    hash_map.Set("H", 8);
    hash_map.Set("I", 9);
    REQUIRE(hash_map.Capacity() > original_capacity);
}

TEST_CASE("Can get items from hash map.", "[HashMap]") {
    HashMap<string, int> hash_map;
    hash_map.Set("A", 1);
    hash_map.Set("B", 5);
    hash_map.Set("C", 10);
    hash_map.Set("A", 9);

    hash_map.Set("D", 5);
    hash_map.Set("E", 5);
    hash_map.Set("F", 5);
    hash_map.Set("G", 5);
    hash_map.Set("H", 5);

    REQUIRE(hash_map.Get("A") == 9);
    REQUIRE(hash_map.Get("B") == 5);
    REQUIRE(hash_map.Get("C") == 10);
    hash_map.Display();
}

TEST_CASE("Can display a hash map.", "[HashMap]") {
    HashMap<string, int> hash_map;
    hash_map.Set("A", 1);
    hash_map.Set("B", 5);
    hash_map.Set("C", 10);
    hash_map.Set("A", 9);
    hash_map.Display();
}

