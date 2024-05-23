#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 101; i++) {
        if (i % 3 == 0)
            cout << "Fizz";
        if (i % 5 == 0)
            cout << "Buzz";
    }
}