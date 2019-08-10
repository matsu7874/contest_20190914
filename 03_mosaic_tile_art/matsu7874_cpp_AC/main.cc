#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
  cin >> n;
  long mod = 1000000007;
  long total = n;
  for (int i = 1; i < n; i++) {
    total *= i;
    total %= mod;
  }
  cout << total << endl;
  return 0;
}
