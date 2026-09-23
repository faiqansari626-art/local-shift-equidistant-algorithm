import time

def standard_textbook_method(x1, y1, x2, y2):
    # Straightforward expanded baseline implementation (4 squares)
    x = (x1**2 - x2**2 + y1**2 - y2**2) / (2 * (x1 - x2)) if (x1 - x2) != 0 else 0
    return x

def local_shift_algorithm(x1, y1, x2, y2):
    # Faiq Ansari's Optimized LSEA Method (3 squares)
    delta_x = x2 - x1
    if delta_x == 0:
        return 0
    b2 = (y1**2 - y2**2 + delta_x**2) / (2 * delta_x)
    target_x = x2 - b2
    return target_x

# Execution Configuration
iterations = 5000000
x1, y1, x2, y2 = 2, -5, 5, 3

print(f"Running high-resolution test over {iterations:,} loops...")

# Baseline Test
start = time.perf_counter()
for _ in range(iterations):
    standard_textbook_method(x1, y1, x2, y2)
textbook_duration = time.perf_counter() - start

# Optimized Test
start = time.perf_counter()
for _ in range(iterations):
    local_shift_algorithm(x1, y1, x2, y2)
lsea_duration = time.perf_counter() - start

# Performance Outputs
print(f"Textbook Baseline: {textbook_duration:.4f} seconds")
print(f"LSEA Optimized   : {lsea_duration:.4f} seconds")
gain = ((textbook_duration - lsea_duration) / textbook_duration) * 100
print(f"Runtime Gain     : {gain:.2f}% Faster")
