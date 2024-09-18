#include <stdio.h>

int removerDuplicados(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    int j = 0;  // Este puntero rastrea el lugar donde debemos insertar el siguiente número único.

    for (int i = 1; i < numsSize; i++) {
        // Si encontramos un valor diferente del último único registrado, lo movemos a la posición j+1
        if (nums[i] != nums[j]) {
            j++;
            nums[j] = nums[i];
        }
    }

    // j es el índice del último valor único, así que el número total de únicos es j + 1.
    return j + 1;
}

int main() {
    int nums[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int k = removerDuplicados(nums, numsSize);

    printf("El número de elementos únicos es: %d\n", k);
    printf("El arreglo modificado es: ");
    for (int i = 0; i < k; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");

    return 0;
}
