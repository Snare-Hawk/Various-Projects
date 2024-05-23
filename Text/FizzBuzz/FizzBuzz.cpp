/* Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”. */

#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 101; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            if (i % 3 == 0)
                cout << "Fizz";
            if (i % 5 == 0)
                cout << "Buzz";
        } else
            cout << i;
        cout << "\n";
    }
}