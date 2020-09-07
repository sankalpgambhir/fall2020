#include <iostream>
#include <chrono>
#include <vector>

std::vector<int> checks{1}; // add an empty check to account for initial setup delay
const char * test_string = "01Game Over"; // arbitrary string to look for

int main(){

    char c = (char) 0;
    int pos_test = 0; // position in test string during traversal
    int count = 0; // number of test strings seen

    // construct the checks vector as
    // 1, 2, 3, 4, 5,
    // 10, 20, 30, 40, 50, ....
    // 10000, 20000, 30000, 40000, 50000
    int i = 1;
    for(int j = 1; j < 6; j++){
        checks.emplace_back(i*j);

        if(j == 5 && i < 10000){
            j = 0;
            i *= 10;
        }
    }

    
    auto curr_time = std::chrono::high_resolution_clock::now();
    auto last_time = curr_time;

    while(!checks.empty()){
        if(count == checks[0]){
            // log a hit
            curr_time = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double, std::nano> time_taken = curr_time - last_time;
            last_time = curr_time;
            std::cout   << "Count " << count 
                        << " : Time " << time_taken.count() 
                        << " ns" << std::endl;

            // remove this check
            checks.erase(checks.begin());
            // reset
            count = 0;
        }
        

        // have we found the entire string?
        if(test_string[pos_test] == (char) 0){
            count++;
            pos_test = 0;
            continue;
        }

        // get the next character
        c = std::cin.get();

        if(c == test_string[pos_test]){
            pos_test++;
        }

    }

    return 0;
}