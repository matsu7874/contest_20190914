#include <bits/stdc++.h>
#include "testlib.h"

using namespace std;

const int MIN_N = 2;
const int MAX_N = 100000;
const long MIN_L = 0;
const long MAX_L = 1000000000;
const long MIN_P = 0;
const long MAX_P = 1000000000;
const long MIN_R = 0;
const long MAX_R = 1000000000;

signed main(int argc, char* argv[]) {
  registerValidation(argc, argv);

  int n = inf.readInt(MIN_N, MAX_N, "N");
  inf.readEoln();

  for (int i = 0; i < n; i++) {
    inf.readInt(MIN_P, MAX_P, "P");
    inf.readSpace();
    long l = inf.readInt(MIN_L, MAX_L, "L");
    inf.readSpace();
    inf.readInt(l, MAX_R, "R");
    inf.readEoln();
  }
  inf.readEof();
  return 0;
}