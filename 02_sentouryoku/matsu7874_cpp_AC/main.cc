#include <bits/stdc++.h>

using namespace std;

string s;

int main() {
  cin >> s;
  long a[10], b[9], total = 1;
  for (int i = 0; i < s.length(); i++) {
    a[i] = int(s[i]) - int('A') + 1;
  }
  for (int i = 0; i < s.length() - 1; i++) {
    total *= a[i] + a[i + 1];
  }
  cout << total << endl;
  return 0;
}
