def find_equidistant_x_axis(x1, y1, x2, y2):
    """
    Computes the equidistant point (x, 0) on the x-axis
    using the Local Shift Equidistant Algorithm.
    Author: Faiq Ansari
    """
    # Step 1: Calculate relative horizontal separation
    delta_x = x2 - x1

    # Step 2: Edge-Case Guards for Vertical Alignment
    if delta_x == 0:
        if abs(y1) == abs(y2):
            raise ValueError("Infinite equidistant solutions exist (x1 == x2, |y1| == |y2|)")
        raise ValueError("No equidistant point exists on the x-axis (x1 == x2, |y1| != |y2|)")

    # Step 3: Run the single-expansion shift formula (3 explicit squares)
    b2 = (y1**2 - y2**2 + delta_x**2) / (2 * delta_x)

    # Step 4: Translate localized vector back to absolute coordinates
    target_x = x2 - b2

    return target_x
