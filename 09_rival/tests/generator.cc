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
  registerGen(argc, argv, 1);
  struct Testcase {
    int n;
    vector<long> p, l, r;
  };
  const int n_sample_case = 3;
  Testcase sample[n_sample_case] = {
      {3, {3, 2, 1}, {1, 1, 3}, {4, 2, 4}},
      {3, {3, 2, 1}, {1, 1, 3}, {4, 2, 4}},
      {3, {3, 2, 1}, {1, 1, 3}, {4, 2, 4}},
  };
  // 00_sample
  for (int t = 0; t < n_sample_case; t++) {
    ofstream of(format("00_sample_%02d.in", t + 1).c_str());

    int n = sample[t].n;
    of << n << endl;
    for (int i = 0; i < n; i++) {
      long p = sample[t].p[i];
      long l = sample[t].l[i];
      long r = sample[t].r[i];
      of << p << " " << l << " " << r << endl;
    }
    of.close();
  }
  // 01_ramdom_small
  const int MAX_N_SMALL = 10;
  const long MAX_P_SMALL = 10;
  const long MAX_L_SMALL = 10;
  const long MAX_R_SMALL = 10;

  for (int t = 0; t < 20; t++) {
    ofstream of(format("01_random_small_%02d.in", t + 1).c_str());
    int n = rnd.next(MIN_N, MAX_N_SMALL);
    of << n << endl;
    for (int i = 0; i < n; i++) {
      long p = rnd.next(MIN_P, MAX_P_SMALL);
      long l = rnd.next(MIN_L, MAX_L_SMALL);
      long r = rnd.next(l, MAX_R_SMALL);
      of << p << " " << l << " " << r << endl;
    }
    of.close();
  }
  // 02_random_large
  for (int t = 0; t < 5; t++) {
    ofstream of(format("02_random_large_%02d.in", t + 1).c_str());
    int n = rnd.next(MAX_N / 2, MAX_N);
    of << n << endl;
    for (int i = 0; i < n; i++) {
      long p = rnd.next(MIN_P, MAX_P);
      long l = rnd.next(MIN_L, MAX_L);
      long r = rnd.next(l, MAX_R);
      of << p << " " << l << " " << r << endl;
    }
    of.close();
  }
  return 0;
}
