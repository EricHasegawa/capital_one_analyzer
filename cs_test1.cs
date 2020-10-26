/*
 * Program to create a thread in C#
 */
using System;
using System.Threading;

class ThreadEx
{
    public void MyThreadFun()
    {
        int i = 0;
        for (i = 1; i<=4; i++)
        {
            Console.WriteLine("Thread Executed");
        }
    }
}
class Program
{
    public static void Main()
    {
        ThreadEx T = new ThreadEx();
        Thread t1 = new Thread(new ThreadStart(T.MyThreadFun));
        t1.Start();
    }
}