/*
AoC 2021 - Day 3
clang++ -std=c++11 day3.cpp -o day3 && ./day3
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>


int part1(std::ifstream* input) {
    const int b = 12;
    std::vector<std::bitset<b>> binaries;
    std::string line;

    while(std::getline(*input, line))
    {
        binaries.push_back(std::bitset<b>(line));
    }

    std::bitset<b> gamma, epsilon;
    for(int i = b-1; i >= 0; i--)
    {
        int count[2] {0,0};
		for(std::bitset<b> binary : binaries)
		{
			count[binary[i]]++;
		}
		gamma[i] = count[0] > count[1] ? 0 : 1;
    }
    epsilon = std::bitset<b>(gamma).flip();

    return gamma.to_ulong()*epsilon.to_ulong();
}

int main() {
    std::ifstream input("day3_input.txt");

    int result1 = part1(&input);
    std::cout << result1 << std::endl;
}