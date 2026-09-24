# The Local Shift Equidistant Algorithm (LSEA)

Developed by **Faiq Ansari**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An optimized, low-overhead pipeline for calculating equidistant spatial points on a target axis without absolute origin coordinate expansions or multi-binomial expansions.

## 🚀 The Architecture
Traditional textbook coordinate systems calculate geometric relationships globally from the absolute origin (0,0). While mathematically universal, this forces hardware processors to square multiple absolute coordinate values, resulting in high floating-point bit widths, increased arithmetic operations, and potential processing overhead during real-time game rendering loop blocks.

The **Local Shift Equidistant Algorithm (LSEA)** optimizes this pipeline by forming a **Local Translation Vector**. The algorithm computes the relative horizontal separation directly, avoiding the need to expand the horizontal coordinates into separate squared terms.

### Key Performance Benefits:
* **Algorithmic Reduction:** Reduces the number of explicit squaring operations compared with a straightforward expanded implementation (4→3 in 2D, 6→5 in 3D), offering a theoretical reduction in those specific operations.
* **Localized Working Bounds:** Minimizes numerical scaling bottlenecks by isolating a localized relative horizontal span, isolating calculations away from global origin expansions.
* **Edge-Case Stability:** Explicitly detects the vertical-alignment case (x1 == x2) and raises a descriptive `ValueError` instead of failing silently or crashing with an unhandled division error.

---

## 📐 2D Formula

$$x = x_2 - \left[ \frac{(y_1^2 - y_2^2) + (x_2 - x_1)^2}{2(x_2 - x_1)} \right]$$

## 🛠️ 2D Implementation (Python)

```python
def find_equidistant_x_axis(x1, y1, x2, y2):
    """
    Computes the equidistant point (x, 0) on the x-axis 
    using the optimized Local Shift Equidistant Algorithm.
    Author: Faiq Ansari
    """
    delta_x = x2 - x1

    if delta_x == 0:
        if abs(y1) == abs(y2):
            raise ValueError("Infinite equidistant solutions exist (x1 == x2, |y1| == |y2|)")
        raise ValueError("No equidistant point exists on the x-axis (x1 == x2, |y1| != |y2|)")

    b2 = (y1**2 - y2**2 + delta_x**2) / (2 * delta_x)
    target_x = x2 - b2
    return target_x
```

---

## 📐 3D Formula

$$x = x_2 - \left[ \frac{(y_1^2 - y_2^2) + (z_1^2 - z_2^2) + (x_2 - x_1)^2}{2(x_2 - x_1)} \right]$$

## 🛠️ 3D Implementation (Python)

```python
def find_equidistant_x_axis_3d(x1, y1, z1, x2, y2, z2):
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
    target_x = x2 - (numerator / (2 * delta_x))
    return target_x
```

See [`benchmark.py`](benchmark.py) for the full source, including both baseline and optimized versions used in testing.

---

## 📊 Benchmarks & Verification
To analyze the performance profile of LSEA against a straightforward expanded textbook implementation, an isolated benchmark script was executed across **5,000,000 continuous iterations** for both the 2D and 3D versions within this repository (`benchmark.py`).

### 🖥️ Environment Profile
* **Host Runtime:** Python 3 interpreted environment (Standard CPython)
* **Testing Routine:** Standard isolated execution blocks utilizing `time.perf_counter()` for high-resolution timing.
* **Sample Scope:** 5,000,000 high-frequency mathematical function cycles per version.

### 📈 Execution Benchmark Results

**2D**
* Textbook Expanded Method: 1.0039 seconds total execution time.
* Optimized LSEA Method: 0.9342 seconds total execution time.
* Measured Runtime Gain: **~6.94% faster execution**.

**3D**
* Textbook Expanded Method: 1.3156 seconds total execution time.
* Optimized LSEA Method: 1.2380 seconds total execution time.
* Measured Runtime Gain: **~5.90% faster execution**.

*(Results above were measured in a sandboxed test environment and will vary by machine and Python version — re-run `benchmark.py` locally to reproduce on your own hardware.)*

### Technical Analysis
The benchmark demonstrates a measurable reduction in runtime under this specific test configuration. While the theoretical reduction in explicit squaring operations does not guarantee a proportional performance improvement in full-scale graphics rendering pipelines (where performance relies heavily on low-level compiler state, hardware vectorization, and language choice), the benchmark confirms a reliable reduction in local computational overhead under high-frequency iteration loops, in both the 2D and 3D cases.
