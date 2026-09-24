import time

def standard_textbook_method(x1, y1, x2, y2):
    # Straightforward expanded baseline implementation (4 squares)
    denominator = 2 * (x1 - x2)
    if denominator == 0:
        if abs(y1) == abs(y2):
            return 0.0  # Fallback to prevent crash during iteration tests
        return 0.0
    return (x1**2 - x2**2 + y1**2 - y2**2) / denominator

def local_shift_algorithm(x1, y1, x2, y2):
    """
    Computes the equidistant point (x, 0) on the x-axis 
    using the optimized Local Shift Equidistant Algorithm.
    Author: Faiq Ansari
    """
    delta_x = x2 - x1
    
    # Edge-Case Guards for Vertical Alignment (x1 == x2)
    if delta_x == 0:
        if abs(y1) == abs(y2):
            raise ValueError("Infinite equidistant solutions exist (x1 == x2, |y1| == |y2|)")
        raise ValueError("No equidistant point exists on the x-axis (x1 == x2, |y1| != |y2|)")
        
    # LSEA Single-expansion core calculation (3 squares)
    b2 = (y1**2 - y2**2 + delta_x**2) / (2 * delta_x)
    return x2 - b2


def standard_textbook_method_3d(x1, y1, z1, x2, y2, z2):
    # Straightforward expanded baseline implementation (6 squares)
    denominator = 2 * (x1 - x2)
    if denominator == 0:
        if (y1**2 + z1**2) == (y2**2 + z2**2):
            return 0.0  # Fallback to prevent crash during iteration tests
        return 0.0
    return (x1**2 - x2**2 + y1**2 - y2**2 + z1**2 - z2**2) / denominator

def local_shift_algorithm_3d(x1, y1, z1, x2, y2, z2):
    """
    Computes the equidistant point (x, 0, 0) on the x-axis
    using the 3D Local Shift Equidistant Algorithm.
    Author: Faiq Ansari
    """
    delta_x = x2 - x1

    if delta_x == 0:
        if (y1**2 + z1**2) == (y2**2 + z2**2):
            raise ValueError("Infinite equidistant solutions exist (x1 == x2, equal radial distance)")
        raise ValueError("No equidistant point exists on the x-axis (x1 == x2, unequal radial distance)")

    numerator = y1**2 - y2**2 + z1**2 - z2**2 + delta_x**2
    return x2 - (numerator / (2 * delta_x))


if __name__ == "__main__":
    iterations = 5000000
    x1, y1, x2, y2 = 2, -5, 5, 3
    z1, z2 = -3, 4

    print(f"Running high-resolution test over {iterations:,} loops...")
    print("\n--- 2D Benchmark ---")

    start = time.perf_counter()
    for _ in range(iterations):
        standard_textbook_method(x1, y1, x2, y2)
    textbook_duration = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(iterations):
        local_shift_algorithm(x1, y1, x2, y2)
    lsea_duration = time.perf_counter() - start

    print(f"Textbook Baseline: {textbook_duration:.4f} seconds")
    print(f"LSEA Optimized   : {lsea_duration:.4f} seconds")
    gain = ((textbook_duration - lsea_duration) / textbook_duration) * 100
    print(f"Runtime Gain     : {gain:.2f}% Faster")

    print("\n--- 3D Benchmark ---")

    start = time.perf_counter()
    for _ in range(iterations):
        standard_textbook_method_3d(x1, y1, z1, x2, y2, z2)
    textbook_duration_3d = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(iterations):
        local_shift_algorithm_3d(x1, y1, z1, x2, y2, z2)
    lsea_duration_3d = time.perf_counter() - start

    print(f"Textbook Baseline: {textbook_duration_3d:.4f} seconds")
    print(f"LSEA Optimized   : {lsea_duration_3d:.4f} seconds")
    gain_3d = ((textbook_duration_3d - lsea_duration_3d) / textbook_duration_3d) * 100
    print(f"Runtime Gain     : {gain_3d:.2f}% Faster")
