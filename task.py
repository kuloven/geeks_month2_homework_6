def selection_sort(nom):

    n = len(nom)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nom[j] < nom[min_idx]:
                min_idx = j
        nom[i], nom[min_idx] = nom[min_idx], nom[i]

    return nom

def binary_search(target, nom):
    left = 0
    right = len(nom) - 1

    while left <= right:
        mid = (left + right) // 2

        if nom[mid] == target:
            print(f"Элемент {target} найден в позиции {mid}.")
            return

        elif nom[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    print(f"Элемент {target} не найден в списке.")

unsorted_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

target = 11
binary_search(target, sorted_list)
