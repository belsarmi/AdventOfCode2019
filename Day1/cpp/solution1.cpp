//reading this source code
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

//using namespace std;

int main(int argc, char *argv[]) {
    std::vector<int> data;
    std::string line;
    std::string::size_type sz;
    std::ifstream myfile ("../Day1Input.txt");
    if (myfile.is_open()){
	while (std::getline (myfile, line) ) {
	    data.push_back(std::stoi(line,&sz));
	}
	myfile.close();
    }
    else std::cout << "Unable to open file!";
    int mysum = 0;
    for(auto i: data){
	mysum += i/3-2;
    }

    std::cout << mysum << "\n";
    return 0;
}
