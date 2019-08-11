#include <bits/stdc++.h>
#include "testlib.h"

using namespace std;

signed main(int argc, char* argv[]) {
  registerValidation(argc, argv);
  long long n = inf.readInt(1, 100000, "N");
  inf.readEoln();

  string s = inf.readWord("[A-Z]{" + to_string(n) + "}");
  inf.readEoln();

  int q = inf.readInt(1, 100000, "Q");
  inf.readEoln();

  long long maxq = (n * (n + 1)) / 2;
  vector<long long> qs = inf.readLongs(q, 1, maxq, "qs");
  inf.readEoln();
  inf.readEof();

  return 0;
}
