#include <bits/stdc++.h>

using namespace std;

int n;
long p[100000], l[100000], r[100000];
bool is_rival(int a, int b) { return (l[a] <= p[b]) && (p[b] <= r[a]); }

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> p[i] >> l[i] >> r[i];
  }
  long cnt = 0;
  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      if (is_rival(i, j) && is_rival(j, i)) {
        cnt += 1;
      }
    }
  }
  cout << cnt << endl;
  return 0;
}
