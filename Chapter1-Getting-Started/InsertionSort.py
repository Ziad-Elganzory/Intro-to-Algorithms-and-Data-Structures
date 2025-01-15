#Algorithm
arr = [5,2,4,6,1,3]

def AscendingInsertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr

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