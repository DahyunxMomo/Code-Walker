using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int primerNumero;

            int segundoNumero;

            int suma;

            primerNumero = 234;

            segundoNumero = 567;

            suma = primerNumero + segundoNumero;

            Console.WriteLine("La suma de {0} y {1} es {2}", primerNumero, segundoNumero, suma);

            Console.ReadKey();

        }
    }
}
