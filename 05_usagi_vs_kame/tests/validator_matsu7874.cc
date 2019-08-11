#include <bits/stdc++.h>
#include "testlib.h"

using namespace std;

signed main(int argc, char* argv[]) {
  registerValidation(argc, argv);
  int n = inf.readInt(1, 100000, "N");
  inf.readEoln();
  long long maxab = 1000000000;
  vector<long long> a = inf.readLongs(n, 1, maxab, "a");
  inf.readEoln();
  vector<long long> b = inf.readLongs(n, 1, maxab, "b");
  inf.readEoln();

  long long maxq = 100000000000000;
  int q = inf.readInt(1, 100000, "Q");
  inf.readEoln();
  vector<long long> qs = inf.readLongs(q, 0, maxq, "qs");
  for (int i = 0; i < q - 1; i++) {
    assert(qs[i] < qs[i + 1]);
  }
  inf.readEoln();

  inf.readEof();
  return 0;
}
