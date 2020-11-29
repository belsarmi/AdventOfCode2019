//reading this source code
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

//using namespace std;
#define CAL(x) (x/3-2)

int calculate(std::vector<int> data){
    int mysum = 0;
    bool i_res = false;
    for(auto i:data){
	int res = CAL(i);
	mysum  += res;
	while (!i_res){
	    if (CAL(res) >= 0){
		res = CAL(res);
		mysum += res;
	    }else{
		i_res = true;
	    }
	}
	i_res = false;
    }
    return mysum;
}
std::vector<int> readfile_create_data(){

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

    return data;
}
int main(int argc, char *argv[]) {
    std::vector<int> data = readfile_create_data(); 
    std::cout << calculate(data) << "\n";
    return 0;
}
