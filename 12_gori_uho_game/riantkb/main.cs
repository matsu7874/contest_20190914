using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Threading;

using P = pair<int, int>;

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
        int n;
        P[] p;
        int[] c;
        int[][] memo;
        bool dfs(int now, int bit, int k) {
            if (memo[now][bit] != 0) return memo[now][bit] == 1;
            bool win = false;
            for (int i = 0; i < n; i++)
            {
                if (((bit >> i) & 1) == 1 && Math.Abs(p[now].v1 - p[i].v1) + Math.Abs(p[now].v2 - p[i].v2) == c[k])
                    win |= !dfs(i, bit ^ (1 << i), k + 1);
            }
            memo[now][bit] = win ? 1 : -1;
            return win;
        }
        public void solve() {
            n = sc.Int;
            int m = 5;
            var s = new string[m];
            int k = 0;
            p = new P[n + 1];
            for (int i = 0; i < m; i++)
            {
                s[i] = sc.Str;
                for (int j = 0; j < m; j++)
                {
                    if (s[i][j] == 'G')
                        p[n] = new P(i, j);
                    else if (s[i][j] == 'B')
                        p[k++] = new P(i, j);
                }
            }
            c = sc.IntArr;
            memo = new int[n + 1][];
            for (int i = 0; i < n + 1; i++)
                memo[i] = new int[1 << n];

            Prt(dfs(n, (1 << n) - 1, 0) ? "gori" : "uho");

        } // end Solver.solve

    }
}

class pair<T, U> : IComparable<pair<T, U>> {
    public T v1;
    public U v2;
    public pair() : this(default(T), default(U)) {}
    public pair(T v1, U v2) { this.v1 = v1; this.v2 = v2; }
    public int CompareTo(pair<T, U> a) {
        int c = Comparer<T>.Default.Compare(v1, a.v1);
        return c != 0 ? c : Comparer<U>.Default.Compare(v2, a.v2);
    }
    public override string ToString() => v1 + " " + v2;
    public void Deconstruct(out T a, out U b) { a = v1; b = v2; }
}

class Scan {
    StreamReader sr;
    public Scan() { sr = new StreamReader(Console.OpenStandardInput()); }
    public Scan(string path) { sr = new StreamReader(path); }
    public int Int => int.Parse(Str);
    public long Long => long.Parse(Str);
    public double Double => double.Parse(Str);
    public string Str => sr.ReadLine().Trim();
    public pair<T, U> Pair<T, U>() {
        T a; U b;
        Multi(out a, out b);
        return new pair<T, U>(a, b);
    }
    public P P => Pair<int, int>();
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
