# Day 01 — Fast I/O & Input/Output Patterns

## 🎯 Goals
- Master Python's fast I/O for Codeforces
- Handle every possible input format used in CF problems
- Avoid TLE caused by slow I/O

---

## ⚡ Why Fast I/O?

Python's default `input()` is slow for large inputs. Use `sys.stdin.readline` instead.

```python
import sys
input = sys.stdin.readline    # Override input globally — do this EVERY submission
```

**Speed comparison (1 million reads):**
| Method | Speed |
|--------|-------|
| `input()` | ~5s |
| `sys.stdin.readline` | ~1s |
| `sys.stdin.read().split()` | ~0.3s |

---

## 📥 All Input Patterns

### Single integer
```python
n = int(input())
```

### Two integers on one line
```python
a, b = map(int, input().split())
```

### List of n integers on one line
```python
a = list(map(int, input().split()))
```

### n followed by a list (same line or next line)
```python
n = int(input())
a = list(map(int, input().split()))
```

### Multiple test cases
```python
t = int(input())
for _ in range(t):
    # solve one test case
    n = int(input())
```

### Read entire input at once (FASTEST for large inputs)
```python
import sys
data = sys.stdin.read().split()
idx = 0
def rd():
    global idx
    idx += 1
    return data[idx - 1]

n = int(rd())
a = [int(rd()) for _ in range(n)]
```

### Read a string/line
```python
s = input().strip()   # .strip() removes trailing newline
```

### 2D grid of integers
```python
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
```

### 2D grid of characters
```python
n = int(input())
grid = [input().strip() for _ in range(n)]
# Access: grid[row][col]
```

### Read until EOF
```python
import sys
for line in sys.stdin:
    line = line.strip()
    if not line: break
    # process line
```

---

## 📤 Output Patterns

### Single value
```python
print(answer)
```

### Multiple values on one line
```python
print(a, b, c)              # space-separated
print(*[1, 2, 3])           # unpack list
```

### List output (newline-separated) — FAST
```python
print('\n'.join(map(str, answers)))
```

### YES/NO
```python
print("YES" if condition else "NO")
```

### Floating point with precision
```python
print(f"{answer:.9f}")
```

### Collect all outputs then print once (fastest)
```python
out = []
for _ in range(t):
    out.append(str(solve()))
print('\n'.join(out))
```

---

## 📝 Exercises

### Exercise 1
Read two integers a and b, print their sum.
```
Input:  3 5
Output: 8
```

### Exercise 2
Read t test cases. Each: read n integers and print their sum.
```
Input:
3
3 1 2 3
2 10 20
4 1 1 1 1

Output:
6
30
4
```

### Exercise 3
Read a 3×3 grid, print the sum of each row.

### Exercise 4
Read strings until EOF, print total character count.

---

## 🔗 Codeforces Practice Problems
1. [A. Watermelon](https://codeforces.com/problemset/problem/4/A) — basic I/O
2. [A. Way Too Long Words](https://codeforces.com/problemset/problem/71/A) — string I/O
3. [A. Team](https://codeforces.com/problemset/problem/231/A) — multi-test case
4. [A. Theatre Square](https://codeforces.com/problemset/problem/1/A) — math + I/O

---

## 💡 Key Takeaways
- **Always**: `import sys; input = sys.stdin.readline`
- For very large input: read all at once with `sys.stdin.read().split()`
- Use `print('\n'.join(...))` to batch output — much faster than many `print()` calls
- **Submit as PyPy3** on Codeforces for 3–5x speed boost
