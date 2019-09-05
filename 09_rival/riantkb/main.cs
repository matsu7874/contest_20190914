using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Threading;

using static util;

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
            int n = sc.Int;
            var p = new int[n];
            var l = new int[n];
            var r = new int[n];
            var idx = new int[n];
            for (int i = 0; i < n; i++)
            {
                idx[i] = i;
                sc.Multi(out p[i], out l[i], out r[i]);
            }
            var cmp = compress(p, l, r);
            p = p.Select(x => cmp[x]).ToArray();
            l = l.Select(x => cmp[x]).ToArray();
            r = r.Select(x => cmp[x]).ToArray();

            Array.Sort(idx, (i, j) => p[i].CompareTo(p[j]));
            var ql = new PriorityQueue<int>((i, j) => l[j].CompareTo(l[i]));
            var qr = new PriorityQueue<int>((i, j) => r[j].CompareTo(r[i]));
            for (int i = 0; i < n; i++)
                ql.Push(i);

            var bit = new BIT(cmp.Count);
            long ans = 0;
            foreach (var i in idx)
            {
                while (ql.Count > 0 && l[ql.Top] <= p[i]) {
                    int x = ql.Pop();
                    bit.add(p[x], 1);
                    qr.Push(x);
                }
                while (qr.Count > 0 && r[qr.Top] < p[i]) {
                    int x = qr.Pop();
                    bit.add(p[x], -1);
                }
                ans += bit.sum(l[i], r[i] + 1);
            }
            for (int i = 0; i < n; i++)
                if (l[i] <= p[i] && p[i] <= r[i]) --ans;

            Assert(ans % 2 == 0);
            Prt(ans / 2);

        } // end Solver.solve

    }
}

static class util {
    public static void Assert(bool cond) { if (!cond) throw new Exception(); }
    public static Dictionary<T, int> compress<T>(this IEnumerable<T> a)
        => a.Distinct().OrderBy(v => v).Select((v, i) => new { v, i }).ToDictionary(p => p.v, p => p.i);
    public static Dictionary<T, int> compress<T>(params IEnumerable<T>[] a) => compress(a.Aggregate(Enumerable.Union));
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

// the greatest element pops
class PriorityQueue<T> {
    List<T> buf;
    public bool rev = false;
    Func<int, int, int> cmp;
    public PriorityQueue() {
        buf = new List<T>();
        cmp = (i, j) => Comparer<T>.Default.Compare(buf[i], buf[j]) * (rev ? -1 : 1);
    }
    public PriorityQueue(Func<T, T, int> cmp) {
        buf = new List<T>();
        this.cmp = (i, j) => cmp(buf[i], buf[j]);
    }
    void swap(int i, int j) { var t = buf[i]; buf[i] = buf[j]; buf[j] = t; }
    public void Push(T elem) {
        int n = buf.Count;
        buf.Add(elem);
        while (n > 0) {
            int i = (n - 1) >> 1;
            if (cmp(n, i) > 0) swap(i, n);
            n = i;
        }
    }
    public T Pop() {
        T ret = buf[0];
        int n = buf.Count - 1;
        buf[0] = buf[n];
        buf.RemoveAt(n);
        for (int i = 0, j; (j = (i << 1) + 1) < n; i = j) {
            if (j != n - 1 && cmp(j, j + 1) < 0) ++j;
            if (cmp(i, j) < 0) swap(i, j);
        }
        return ret;
    }
    public T Top => buf[0];
    public int Count => buf.Count;
}
class BIT {
    int n;
    long[] bit;
    public BIT(int n) { this.n = n; bit = new long[n]; }
    public void add(int j, long w) { for (int i = j; i < n; i |= i + 1) bit[i] += w; }
    public long at(int j) => sum(j, j + 1);
    // [0, j)
    public long sum(int j) {
        long ret = 0;
        for (int i = j - 1; i >= 0; i = (i & i + 1) - 1) ret += bit[i];
        return ret;
    }
    // [j, k)
    public long sum(int j, int k) => sum(k) - sum(j);
}
