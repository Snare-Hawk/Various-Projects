#include <iostream>
using namespace std;

int main() {
    string input;
    cout << "Please input a word to be reversed: ";
    cin >> input;
    
    for (int i = input.size() - 1; i > -1; i--)
        cout << input[i];
}