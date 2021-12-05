/*
AoC 2021 - Day 2
clang++ -std=c++11 day2.cpp -o day2 && ./day2
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

std::vector<std::string> split_string(std::string* line) {
    std::istringstream iss(*line);
    std::vector<std::string> split(std::istream_iterator<std::string>{iss}, std::istream_iterator<std::string>());
    return split;
}

int part1(std::ifstream* input_stream) {
    std::string line;
    int horiz = 0, depth = 0, amount; 

    while(std::getline(*input_stream, line))
    {
        std::vector<std::string> move = split_string(&line);
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

int part2(std::ifstream* input_stream) {
    std::string line;
    int horiz = 0, depth = 0, aim = 0, amount; 

    while(std::getline(*input_stream, line))
    {
        std::vector<std::string> move = split_string(&line);
        amount = std::stoi(move[1]);
    
        if (move[0] == "forward") {
            horiz += amount;
            depth = depth + (aim * amount);
        } else if (move[0] == "down") {
            aim += amount;
        } else if (move[0] == "up") {
            aim -= amount;
        }
    }
    return horiz * depth;
}

int main() {
    std::ifstream input_stream("day2_input.txt");

    int result1 = part1(&input_stream);
    std::cout << "Part 1 Result: " << result1 << std::endl;
    
    // reset the file position to the beginning
    input_stream.clear();
    input_stream.seekg(0);

    int result2 = part2(&input_stream);
    std::cout << "Part 2 Result: " << result2 << std::endl;
}
