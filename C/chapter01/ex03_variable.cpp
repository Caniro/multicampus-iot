#include <iostream>
#include <string>

int main(int argc, char const *argv[])
{
    using namespace std;

    int i;

    i = 1000;
    // int i = 1000;
    // int i{ 1000 }
    cout << i << endl;
    string s{ "hello" }; // string s = "hello"와 동일
    cout << s << endl;
}
