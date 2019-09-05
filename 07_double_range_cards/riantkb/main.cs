using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Threading;

class Program {
    static StreamWriter sw = new StreamWriter(Console.OpenStandardOutput()) { AutoFlush = false };
    static Scan sc = new Scan();
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
            int h, w;
            sc.Multi(out h, out w);
            var a = new int[h][];
            for (int i = 0; i < h; i++)
                a[i] = sc.IntArr;

            var imos = new int[h + 1][];
            for (int i = 0; i < h + 1; i++)
                imos[i] = new int[w + 1];

            int q = sc.Int;
            for (int i = 0; i < q; i++)
            {
                var b = sc.IntArr;
                {
                    int x1 = b[0] - 1;
                    int x2 = b[1];
                    int y1 = b[2] - 1;
                    int y2 = b[3];
                    ++imos[x1][y1];
                    --imos[x2][y1];
                    --imos[x1][y2];
                    ++imos[x2][y2];
                }
                {
                    int x1 = b[4] - 1;
                    int x2 = b[5];
                    int y1 = b[6] - 1;
                    int y2 = b[7];
                    ++imos[x1][y1];
                    --imos[x2][y1];
                    --imos[x1][y2];
                    ++imos[x2][y2];
                }
            }
            int ans = 0;
            for (int i = 0; i < h; i++)
            {
                for (int j = 0; j < w; j++)
                    imos[i][j + 1] += imos[i][j];

                for (int j = 0; j < w; j++)
                {
                    if (i > 0)
                        imos[i][j] += imos[i - 1][j];
                    if (imos[i][j] % 2 == 1)
                        ans += a[i][j];
                }
            }
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
