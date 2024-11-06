#include <bits/stdc++.h>
#include <chrono> // Para medir el tiempo de ejecución
using namespace std;

struct Item {
    int profit, weight;
    Item(int profit, int weight) : profit(profit), weight(weight) {}
};

static bool cmp(struct Item a, struct Item b) {
    double r1 = (double)a.profit / (double)a.weight;
    double r2 = (double)b.profit / (double)b.weight;
    return r1 > r2;
}

double fractionalKnapsack(int W, struct Item arr[], int N) {
    sort(arr, arr + N, cmp);
    double finalvalue = 0.0;
    for (int i = 0; i < N; i++) {
        if (arr[i].weight <= W) {
            W -= arr[i].weight;
            finalvalue += arr[i].profit;
        } else {
            finalvalue += arr[i].profit * ((double)W / (double)arr[i].weight);
            break;
        }
    }
    return finalvalue;
}

int main() {
    Item arr[] = { 
        { 100, 10 }, { 280, 40 }, { 120, 20 }, { 120, 24 }, { 100, 36 },
        { 150, 30 }, { 180, 50 }, { 40, 10 }, { 60, 20 }, { 90, 35 },
        { 200, 25 }, { 300, 29 }, { 90, 24 }, { 40, 5 }, { 30, 6 },
        { 10, 4 }, { 70, 20 }, { 80, 10 }, { 50, 15 }, { 110, 22 }
    };
    int N = sizeof(arr) / sizeof(arr[0]);

    int weights[] = { 50, 80 };
    for (int W : weights) {
        auto start = chrono::high_resolution_clock::now();
        double maxProfit = fractionalKnapsack(W, arr, N);
        
        auto end = chrono::high_resolution_clock::now();
        chrono::duration<double> duration = end - start;
        cout << "Para W = " << W << ", máximo beneficio = " << maxProfit 
             << ", tiempo de ejecución = " << duration.count() << " segundos" << endl;
    }
    return 0;
}
