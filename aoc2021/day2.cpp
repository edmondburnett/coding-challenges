/*
AoC 2021 - Day 2
clang++ -std=c++11 day2.cpp -o day2 && ./day2
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

std::ifstream input_stream("day2_input.txt");

int part1() {
    std::string move, line;
    int horiz = 0, depth = 0, amount; 

    while(std::getline(input_stream, line))
    {
        std::istringstream iss(line);
        std::vector<std::string> move(std::istream_iterator<std::string>{iss}, std::istream_iterator<std::string>());
        amount = std::stoi(move[1]);
        if (move[0] == "forward") {
            horiz += amount;
        } else if (move[0] == "down") {
            depth += amount;
        } else if (move[0] == "up") {
            depth -= amount;
        } 
    }
    return horiz * depth;
}

int part2() {

}

int main() {
    std::cout << part1() << std::endl;
}
