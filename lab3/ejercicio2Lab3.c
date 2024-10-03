#include <stdio.h>
#include <sys/time.h>

// Función recursiva para calcular Fibonacci
unsigned long long fibonacci(int n) {
    if (n <= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    unsigned long long result;
    struct timeval start, end;

    // Solicitar el valor de n
    printf("Ingrese el valor de n: ");
    scanf("%d", &n);

    // Medir el tiempo de inicio con gettimeofday
    gettimeofday(&start, NULL);

    // Calcular el número de Fibonacci
    result = fibonacci(n);

    // Medir el tiempo de fin con gettimeofday
    gettimeofday(&end, NULL);

    // Calcular el tiempo en microsegundos
    long seconds = (end.tv_sec - start.tv_sec);
    long micros = ((seconds * 1000000) + end.tv_usec) - (start.tv_usec);

    // Imprimir el resultado y el tiempo de ejecución
    printf("Fibonacci(%d) = %llu\n", n, result);
    printf("Tiempo de ejecución: %ld microsegundos\n", micros);

    return 0;
}
