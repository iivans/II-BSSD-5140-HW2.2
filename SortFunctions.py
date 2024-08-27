def partition(A, low, high, compare):
    # Choose the pivot
    pivot = A[high]
    i = low - 1
    
    # Traverse A[low..high] and move all smaller elements to the left side
    for j in range(low, high):
        if not compare(A[j], pivot):
            i += 1
            A[i], A[j] = A[j], A[i]
    
    # Move pivot after smaller elements and return its position
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

# The iterative QuickSort function implementation
def quick_sort(A, compare):
    # Stack for storing start and end index
    stack = [(0, len(A) - 1)]
    
    # Main loop to pop and push items until stack is empty
    while stack:
        start, end = stack.pop()
        
        if start >= end:
            continue
        
        # Partition process
        pivot_index = partition(A, start, end, compare)
        
        # Push left and right subarrays into the stack
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

def selection_sort(A, compare):
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if compare(A[j], A[min_idx]):
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

def binary_search_sub(A, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if A[mid] == x:
            return mid

        # If x is greater, ignore the left half
        elif A[mid] < x:
            l = mid + 1

        # If x is smaller, ignore the right half
        else:
            r = mid - 1

    # If we reach here, the element was not present
    # Return the position where x would be inserted
    return l

# Function to print an array (for debugging)
def print_array(A):
    for i in A:
        print(i, end=" ")
    print()

# Driver code for testing
if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    print("Original array:", A)
    quick_sort(A, lambda x, y: x > y)  # You can switch to selection_sort to test that function
    print("Sorted array:", A)