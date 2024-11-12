//Merge Sort vs. Quick Sort Here, the divide-and-conquer sorting algorithms—Merge Sort and Quick Sort—are implemented and compared on the same dataset. This experiment enables students to analyze sorting efficiency and understand the practical differences between stable sorting in Merge Sort and in-place partitioning in Quick Sort.
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to merge two subarrays for Merge Sort
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int leftArr[n1], rightArr[n2];

    // Copy data to temp arrays
    for (int i = 0; i < n1; i++)
        leftArr[i] = arr[left + i];
    for (int i = 0; i < n2; i++)
        rightArr[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }

    // Copy remaining elements of leftArr[]
    while (i < n1) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }

    // Copy remaining elements of rightArr[]
    while (j < n2) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

// Function to implement Merge Sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Function to partition the array for Quick Sort
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return (i + 1);
}

// Function to implement Quick Sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to copy array elements
void copyArray(int source[], int destination[], int n) {
    for (int i = 0; i < n; i++) {
        destination[i] = source[i];
    }
}

int main() {
    // Hard-coded array for testing
    int arr1[] = {23, 45, 16, 37, 3, 99, 22, 14, 78, 50};
    int n = sizeof(arr1) / sizeof(arr1[0]);
    int arr2[n];

    // Copy arr1 to arr2 to ensure both sorting algorithms use the same data
    copyArray(arr1, arr2, n);

    // Measure time for Merge Sort
    clock_t start_merge = clock();
    mergeSort(arr1, 0, n - 1);
    clock_t end_merge = clock();
    double time_merge = (double)(end_merge - start_merge) / CLOCKS_PER_SEC;
    printf("Time taken by Merge Sort: %.6f seconds\n", time_merge);

    // Measure time for Quick Sort
    clock_t start_quick = clock();
    quickSort(arr2, 0, n - 1);
    clock_t end_quick = clock();
    double time_quick = (double)(end_quick - start_quick) / CLOCKS_PER_SEC;
    printf("Time taken by Quick Sort: %.6f seconds\n", time_quick);

    // Print sorted arrays for verification
    printf("Sorted array using Merge Sort: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");

    printf("Sorted array using Quick Sort: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr2[i]);
    }
    printf("\n");

    return 0;
}
