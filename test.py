import heapq

heap = [1, 3, 5, 7, 9, 2]
heapq.heapify(heap)  # Chuyển danh sách thành min-heap
print(heap)  # Output: [1, 3, 2, 7, 9, 5]