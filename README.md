using System;

public class Program
{
    // бинарное возведение в степень
    static int bp(int a, int n, int mod)
    {
        int res = 1;
        while (n > 0)
        {
            if (n % 2 == 1) res = res * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return res;
    }

    // находит обратный элемент как a^(p-2)
    static int inv(int x, int mod)
    {
        return bp(x, mod - 2, mod);
    }


    static void Solve(int n, int m)
    {
        long s = 1;
        for (int i = 2; i <= n; i++)
        {
            s += (long)inv(i, m);
        }
        Console.WriteLine($"== {s}");
    }

    static void Solve_(long n, long m)
    {
        long sm = 1;
        var r = new long[n + 1];
        r[1] = 1;

        for (int i = 2; i < n + 1; i++)
        {
            //Console.WriteLine($"{i} : {m % i} : {r[m % i]}");
            long d = (m - (m / i) * r[m % i] % m) % m;
            r[i] = d;
            sm += d;
        }
        Console.WriteLine(sm);
    }

    public static int Main()
    {
        var watch = System.Diagnostics.Stopwatch.StartNew();
        Solve(100_000_000, 999_999_937);
        //Solve(3, 5);
        watch.Stop();
        var elapsedMs = watch.ElapsedMilliseconds / 1000;
        Console.WriteLine("Done!  " + elapsedMs);
        string s = Console.ReadLine();
        int r = int.Parse(s);

        return 0;
    }
}

