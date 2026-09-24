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
