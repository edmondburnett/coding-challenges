/*
AoC 2021 - Day 1
clang++ -std=c++11 day1.cpp -o day1 && ./day1
*/

#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream input_stream("day1_input.txt");
    std::string line;
    int value;
    int prev_value;
    int count = 0;

    while(std::getline(input_stream, line))
    {
        prev_value = value;
        value = std::stoi(line);

        if (prev_value > 1 && value > prev_value)
        {
            count++;
        }
    }
    std::cout << count << std::endl;
}