import time

def bubble_sort(items):
    """Bubble Sort Algorithm"""
    for i in range(len(items)):
        for j in range(len(items)-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def quick_sort(items):
    """Quick Sort Algorithm"""
    if len(items) <= 1:
        return items
    else:
        pivot = items[0]
        less_than_pivot = [i for i in items[1:] if i <= pivot]
        greater_than_pivot = [i for i in items[1:] if i > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def heapify(items, n, i):
    """Helper function for Heap Sort"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and items[i] < items[left]:
        largest = left
    if right < n and items[largest] < items[right]:
        largest = right
    if largest != i:
        items[i], items[largest] = items[largest], items[i]
        heapify(items, n, largest)

def heap_sort(items):
    """Heap Sort Algorithm"""
    n = len(items)
    for i in range(n, -1, -1):
        heapify(items, n, i)
    for i in range(n-1, 0, -1):
        items[i], items[0] = items[0], items[i]
        heapify(items, i, 0)
    return items

def merge(left, right):
    """Helper function for Merge Sort"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(items):
    """Merge Sort Algorithm"""
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    return list(merge(merge_sort(left), merge_sort(right)))

def selection_sort(items):
    """Selection Sort Algorithm"""
    for i in range(len(items)):
        min_idx = i
        for j in range(i+1, len(items)):
            if items[min_idx] > items[j]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    return items

def sort_data(sort_type, data):
    """Main function to sort data"""
    start_time = time.time()
    if sort_type.lower() == "bubble":
        sorted_items = bubble_sort(data)
    elif sort_type.lower() == "quick":
        sorted_items = quick_sort(data)
    elif sort_type.lower() == "heap":
        sorted_items = heap_sort(data)
    elif sort_type.lower() == "merge":
        sorted_items = merge_sort(data)
    elif sort_type.lower() == "selection":
        sorted_items = selection_sort(data)
    end_time = time.time()
    return sorted_items, end_time - start_time

print("          ****** Sıralama Algoritmaları ******                 ")
while True:
    sort_type = input("Hangi sıralama algoritmasını kullanmak istersiniz? (bubble/quick/heap/merge/selection): ")
    if sort_type.lower() not in ["bubble", "quick", "heap", "merge", "selection"]:
        print("Geçersiz giriş. Lütfen 'bubble', 'quick', 'heap', 'merge' veya 'selection' girin.")
        continue
    else:
        while True:
            data_type = input("Giriş türünü seçin: (kelime/sayi): ")
            if data_type.lower() == "kelime":
                data = input("Kelimeleri virgülle ayırarak girin: ").split(',')
                data = [i.strip() for i in data]
                break
            elif data_type.lower() == "sayi":
                data = input("Sayıları virgülle ayırarak girin: ").split(',')
                data = [int(i.strip()) for i in data]
                break
            else:
                print("Geçersiz giriş. Lütfen 'kelime' veya 'sayi' girin.")
                continue
        sorted_data, duration = sort_data(sort_type, data)
        print("Sıralanmış veri: ", sorted_data)
        print("--- %s seconds ---" % duration)
        break
