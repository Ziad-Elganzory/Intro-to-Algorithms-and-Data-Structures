#Algorithm
arr = [5,2,4,6,1,3]

def AscendingInsertionSort(arr):
    for j in range(1,len(arr)): # ----------------> c1 * n | c1 * n
        key = arr[j]         # ----------------> c2 * (n-1) | c2 * (n-1)
        i = j - 1           # ----------------> c3 * (n-1) | c3 * (n-1)
        while i >= 0 and arr[i] > key: # ----------------> c4 * (n-1) | c4 * ((n-1) * n)/2
            arr[i+1] = arr[i] # ----------------> 0 | c5 * ((n-1) * n)/2
            i = i - 1        # ----------------> 0 | c6 * ((n-1) * n)/2
        arr[i+1] = key     # ----------------> c7 * (n-1) | c7 * (n-1)
    return arr # ----------------> 0 | c8

# Best Case T(n) = c1 * n + c2 * (n-1) + c3 * (n-1) + c4 * (n-1) + 0 + 0 + c7 * (n-1) + 0 = an + b
# Worst Case T(n) = c1 * n + c2 * (n-1) + c3 * (n-1) + c4 * ((n-1) * n)/2 + c5 * ((n-1) * n)/2 + c6 * ((n-1) * n)/2 + c7 * (n-1) + c8 = an^2 + bn + c
# Best Case O(n) | Worst Case O(n^2)

print(AscendingInsertionSort(arr))


#Exercise 2.1-1
# Initial Array: [31, 41, 59, 26, 41, 58]
# After First Iteration: [31, 41, 59, 26, 41, 58]
# After Second Iteration: [31, 41, 59, 26, 41, 58]
# After Third Iteration: [26, 31, 41, 59, 41, 58]
# After Fourth Iteration: [26, 31, 41, 41, 59, 58]
# After Fifth Iteration: [26, 31, 41, 41, 58, 59]

# Exercise 2.1-2
def DecendingInsertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr

print(DecendingInsertionSort(arr))


# Exercise 2.1-3

def linearSearch(arr,v):
    for i in range(len(arr)):
        if v == arr[i]:
            return i

arrSearch = [5,2,4,1,3,6]

print(linearSearch(arrSearch,6))

# Initialization: Before the loop starts, the subarray A[1...0] does not contain #.
# Maintenance: During each iteration, the subarray A[1...i-1] does not contain #.
# Termination: When the loop ends, either the element # is found and returned, or NIL is returned, confirming that # does not appear in the sequence.


# Exercise 2.1-4
def add_binary_integers(A, B):
    # Initialize the result array C with size max(len(A),len(B)) + 1 (for carry)
    n = max(len(A),len(B))
    C = [0] * (n + 1)
    
    # Initialize carry to 0
    carry = 0
    
    # Loop through each bit from right to left (starting from least significant bit)
    for i in range(n):
        digitA = A[i] if i < len(A) else 0
        digitB = B[i] if i < len(B) else 0
        # Calculate sum of corresponding bits from A and B, and the carry
        sum_bits = digitA + digitB + carry
        
        # The current bit is the sum modulo 2
        C[i] = sum_bits % 2
        
        # Update carry for the next step
        carry = sum_bits // 2
    
    # After the loop, the most significant bit (C[n]) will hold the final carry
    C[n] = carry
    
    return C

# Example usage:
A = [1,1, 0, 1, 1]  # Binary number 1011
B = [1, 1, 0, 1]  # Binary number 1101

result = add_binary_integers(A, B)
print(f"Sum of A and B: {result}")

# Initialization: Initially, no bits have been added, so the invariant holds trivially.
# Maintenance: At each step, the algorithm correctly updates the sum and carry, maintaining the invariant.
# Termination: When the loop terminates, the sum of all bits in CC is correct, and the carry has been placed in the final position. Thus, the invariant ensures the correctness of the result

# Exercise 2.2-1

#T(n) = n^3/1000 - 100n^2 - 100n + 3
#T(n) = O(n^3)

# Exercise 2.2-2

# Selection Sort
def SelectionSort(arr):
    for i in range(len(arr)): #------------------> c1 * n
        minIndex = i #---------------------------> c2 * n-1
        for j in range(i+1,len(arr)): #----------> c3 * (n-1) n / 2
            if arr[j] < arr[minIndex]: #---------> c4 * (n-1) n / 2
                minIndex = j            #--------> c5 * (n-1) n / 2
        arr[i], arr[minIndex] = arr[minIndex], arr[i] #-> c6 (n-1)
    return arr

    # Loop Invariant: At the start of each iteration of the outer loop, the subarray A[1...i-1] contains the i-1 smallest elements in sorted order.
    # The algorithm needs to run for only the first n-1 elements because after placing the first n-1 smallest elements in their correct positions, the nth element will naturally be in its correct position.

    # Best-case and Worst-case running times:
    # Best-case: O(n^2) - The best case still involves comparing each element with every other element.
    # Worst-case: O(n^2) - The worst case involves the same number of comparisons and swaps as the best case.

    # Exercise 2.2-3 Average-case and worst-case analysis of linear search

    # In the average case, the element being searched for is equally likely to be any element in the array.
    # Therefore, on average, we need to check half of the elements in the array.
    # If the array has n elements, we need to check n/2 elements on average.

    # In the worst case, the element being searched for is either the last element in the array or not present at all.
    # Therefore, we need to check all n elements in the array.

    # Average-case running time: O(n)
    # Worst-case running time: O(n)

    # Justification:
    # In the average case, the number of comparisons is (n + 1) / 2, which is O(n).
    # In the worst case, the number of comparisons is n, which is also O(n).

    # Exercise 2.2-4
    # To modify almost any algorithm to have a good best-case running time, we can add a check at the beginning of the algorithm to see if the input is already in the desired state. If it is, we can return immediately without performing any further operations. This way, the best-case running time will be O(1).

    # For example, in the case of the Insertion Sort algorithm, we can add a check to see if the array is already sorted before proceeding with the sorting process.

    def OptimizedInsertionSort(arr):
        # Check if the array is already sorted
        is_sorted = True
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                is_sorted = False
                break
        
        # If the array is already sorted, return it immediately
        if is_sorted:
            return arr
        
        # Otherwise, proceed with the regular Insertion Sort algorithm
        for j in range(1, len(arr)):
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i = i - 1
            arr[i + 1] = key
        
        return arr

    # Example usage:
    arr = [1, 2, 3, 4, 5]
    print(OptimizedInsertionSort(arr))  # Output: [1, 2, 3, 4, 5]

    arr = [5, 2, 4, 6, 1, 3]
    print(OptimizedInsertionSort(arr))  # Output: [1, 2, 3, 4, 5, 6]