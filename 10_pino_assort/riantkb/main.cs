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
            int n, k;
            sc.Multi(out n, out k);
            var a = new List<int>[3];
            for (int i = 0; i < 3; i++)
                a[i] = new List<int>();

            int z = 0;
            for (int i = 0; i < n; i++)
            {
                var b = sc.IntArr.Select(x => x - 1).ToArray();
                if (b.Count(x => x > 0) == 0) ++z;
                else {
                    for (int j = 0; j < 3; j++)
                        if (b[j] > 0)
                            a[j].Add(b[j]);
                }
            }
            for (int i = 0; i < 3; i++)
                a[i].Sort();

            int[] pino = { 10, 7, 7 };
            long ng = 0, ok = M;
            while (ng < ok - 1) {
                long m = (ng + ok) / 2;
                int c = z;
                for (int i = 0; i < 3; i++)
                {
                    long p = pino[i] * m - k;
                    if (p < 0) c = -M;
                    foreach (var item in a[i])
                    {
                        if (p >= item) {
                            p -= item;
                            ++c;
                        }
                    }
                }
                if (c >= k) ok = m;
                else ng = m;
            }
            Prt(ok);

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
