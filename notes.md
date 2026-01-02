##The Core Big-O Types

1️⃣ O(1) — Constant Time

arr = [10, 20, 30]
print(arr[0])
>3 elements or 1 million elements → same time
>Access by index, dictionary lookup
📌 Best possible performance


2️⃣ O(n) — Linear Time

Time grows proportionally with input size.
def print_all(arr):
    for x in arr:
        print(x)
If array size doubles → time doubles
One loop → usually O(n)
📌 Most common and acceptable


3️⃣ O(n²) — Quadratic Time
Nested loops → danger zone 🚨
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
n = 100 → 10,000 operations
n = 1,000 → 1,000,000 operations
📌 Works only for small input sizes


4️⃣ O(log n) — Logarithmic Time

Input reduces by half each step.
# Binary Search idea
Every step cuts problem size
Very fast even for huge data
📌 Gold standard for efficiency

🔍 QUICK TRICK TO IDENTIFY TIME COMPLEXITY
| Code Pattern      | Time     |
| ----------------- | -------- |
| No loop           | O(1)     |
| One loop          | O(n)     |
| Two nested loops  | O(n²)    |
| Loop halves input | O(log n) |
| Loop + hash map   | O(n)     |

🧠 SPACE COMPLEXITY
Extra memory used.
def copy(arr):
    new = []
    for x in arr:
        new.append(x)
Time: O(n)
Space: O(n) ❗ (new array)
Using dictionary/set = extra space.