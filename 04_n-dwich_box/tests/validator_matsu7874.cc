#include <bits/stdc++.h>
#include "testlib.h"

using namespace std;

signed main(int argc, char* argv[]) {
  registerValidation(argc, argv);
  string s = inf.readWord();
  assert(1 <= s.length() && s.length() <= 1000);
  regex ndwich("[\#\|]{1,1000}");
  assert(regex_match(s, ndwich));
  regex db("\#\#");
  assert(!regex_search(s, db));
  inf.readEoln();

  inf.readEof();
  return 0;
}
