# The Local Shift Equidistant Algorithm (LSEA)
Developed by **Faiq Ansari**

An optimized, low-overhead pipeline for calculating equidistant spatial points on a target axis without absolute origin coordinate expansions or multi-binomial expansions.

## 🚀 The Architecture
Traditional textbook coordinate systems calculate geometric relationships globally from the absolute origin (0,0). While mathematically universal, this forces hardware processors to square multiple absolute coordinate values, resulting in high floating-point bit widths, increased arithmetic operations, and potential processing overhead during real-time game rendering loop blocks.

The **Local Shift Equidistant Algorithm (LSEA)** optimizes this pipeline by forming a **Local Translation Vector**. The algorithm computes the relative horizontal separation directly, avoiding the need to expand the horizontal coordinates into separate squared terms. 

### Key Performance Benefits:
* **Algorithmic Reduction:** Reduces the number of explicit squaring operations from four to three compared with a straightforward expanded implementation, offering a theoretical 25% reduction in those specific operations.
* **Localized Working Bounds:** Minimizes numerical scaling bottlenecks by isolating a localized relative horizontal span, isolating calculations away from global origin expansions.
* **Edge-Case Stability:** Automatically self-corrects for negative coordinate boundaries outside the visual interval using signed distance geometry principles.

---

## 🛠️ The Implementation (Python)

def find_equidistant_x_axis(x1, y1, x2, y2):
    """
    Computes the equidistant point (x, 0) on the x-axis 
    using the optimized Local Shift Equidistant Algorithm.
    Author: Faiq Ansari
    """
    # Step 1: Calculate relative horizontal separation
    delta_x = x2 - x1
    
    # Step 2: Advanced Edge-Case Guards for Vertical Alignment
    if delta_x == 0:
        if abs(y1) == abs(y2):
            raise ValueError("Infinite equidistant solutions exist (x1 == x2, |y1| == |y2|)")
        raise ValueError("No equidistant point exists on the x-axis (x1 == x2, |y1| != |y2|)")
    
    # Step 3: Run the single-expansion shift formula (3 explicit squares)
    b2 = (y1**2 - y2**2 + delta_x**2) / (2 * delta_x)
    
    # Step 4: Translate localized vector back to absolute coordinates
    target_x = x2 - b2
    
    return target_x
    
---

## 📊 Benchmarks & Verification
To analyze the performance profile of LSEA against a straightforward expanded textbook implementation, an isolated benchmark script was executed across **5,000,000 continuous iterations** within this repository (`benchmark.py`).

### 🖥️ Environment Profile
* **Host Runtime:** Python 3.11 interpreted environment (Standard CPython)
* **Testing Routine:** Standard isolated execution blocks utilizing `time.perf_counter()` for high-resolution timing.
* **Sample Scope:** 5,000,000 high-frequency mathematical function cycles.

### 📈 Execution Benchmark Results
* **Textbook Expanded Method:** 2.8850 seconds total execution time.
* **Optimized LSEA Method:** 2.7008 seconds total execution time.
* **Measured Runtime Gain:** **~6.39% faster execution** under this specific high-frequency benchmark layout.

### Technical Analysis
The benchmark demonstrates a measurable reduction in runtime under this specific test configuration. While a 25% theoretical reduction in explicit squaring operations does not guarantee a linear 25% performance improvement in full-scale graphics rendering pipelines (where performance relies heavily on low-level compiler state, hardware vectorization, and language choice), the benchmark confirms a reliable reduction in local computational overhead under high-frequency iteration loops.
