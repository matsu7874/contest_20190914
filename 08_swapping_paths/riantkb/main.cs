using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Threading;

class Program {
    static StreamWriter sw = new StreamWriter(Console.OpenStandardOutput()) { AutoFlush = false };
    static Scan sc = new Scan();
    const int M = 1000000007;
    static void Prt(string a) => sw.WriteLine(a);
    static void Prt<T>(IEnumerable<T> a) => Prt(string.Join(" ", a));
    static void Prt(params object[] a) => Prt(string.Join(" ", a));

    static void Main(string[] args)
    {
        var solver = new Solver();
        // var t = new Thread(solver.solve, 1 << 26); // 64 MB
        // t.Start();
        // t.Join();
        solver.solve();
        sw.Flush();
    }


    class Solver {
        public void solve() {
            int n, m, a, b;
            sc.Multi(out n, out m);
            sc.Multi(out a, out b);
            --a;
            --b;
            if (Math.Abs(a - b) > n - 1) {
                Prt(0);
                return;
            }
            if (Math.Min(a, b) > n) {
                int d = Math.Min(a, b) - n;
                a -= d;
                b -= d;
                m -= d;
            }
            if (m > Math.Max(a, b) + n) {
                m = Math.Max(a, b) + n;
            }
            var dp1 = new long[m];
            var dp2 = new long[m];
            dp1[a] = 1;
            dp2[b] = 1;
            for (int i = 0; i < n / 2; i++)
            {
                var nex1 = new long[m];
                var nex2 = new long[m];
                for (int j = 0; j < m; j++)
                {
                    nex1[j] = (nex1[j] + dp1[j]) % M;
                    nex2[j] = (nex2[j] + dp2[j]) % M;
                    if (j > 0) {
                        nex1[j] = (nex1[j] + dp1[j - 1]) % M;
                        nex2[j] = (nex2[j] + dp2[j - 1]) % M;
                    }
                    if (j < m - 1) {
                        nex1[j] = (nex1[j] + dp1[j + 1]) % M;
                        nex2[j] = (nex2[j] + dp2[j + 1]) % M;
                    }
                }
                dp1 = nex1;
                dp2 = nex2;
            }
            long ans = 0;
            for (int i = 0; i < m; i++)
                ans = (ans + dp1[i] * dp2[i]) % M;

            ans = ans * ans % M;
            for (int i = 0; i < m; i++)
                ans = (ans + M - dp1[i] * dp1[i] % M * dp2[i] % M * dp2[i] % M) % M;

            Prt(ans);

        } // end Solver.solve

    }
}

class Scan {
    StreamReader sr;
    public Scan() { sr = new StreamReader(Console.OpenStandardInput()); }
    public Scan(string path) { sr = new StreamReader(path); }
    public int Int => int.Parse(Str);
    public long Long => long.Parse(Str);
    public double Double => double.Parse(Str);
    public string Str => sr.ReadLine().Trim();
    public int[] IntArr => StrArr.Select(int.Parse).ToArray();
    public long[] LongArr => StrArr.Select(long.Parse).ToArray();
    public double[] DoubleArr => StrArr.Select(double.Parse).ToArray();
    public string[] StrArr => Str.Split(new[]{' '}, StringSplitOptions.RemoveEmptyEntries);
    bool eq<T, U>() => typeof(T).Equals(typeof(U));
    T ct<T, U>(U a) => (T)Convert.ChangeType(a, typeof(T));
    T cv<T>(string s) => eq<T, int>()    ? ct<T, int>(int.Parse(s))
                       : eq<T, long>()   ? ct<T, long>(long.Parse(s))
                       : eq<T, double>() ? ct<T, double>(double.Parse(s))
                       : eq<T, char>()   ? ct<T, char>(s[0])
                                         : ct<T, string>(s);
    public void Multi<T>(out T a) => a = cv<T>(Str);
    public void Multi<T, U>(out T a, out U b)
    { var ar = StrArr; a = cv<T>(ar[0]); b = cv<U>(ar[1]); }
    public void Multi<T, U, V>(out T a, out U b, out V c)
    { var ar = StrArr; a = cv<T>(ar[0]); b = cv<U>(ar[1]); c = cv<V>(ar[2]); }
}
