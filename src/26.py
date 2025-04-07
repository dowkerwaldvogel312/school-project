import math

def calculate_cylinder_volume(radius, height):
    """
    Calculate the volume of a cylinder.
    
    Parameters:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.
        
    Returns:
        float: The volume of the cylinder.
    """
    return math.pi * radius ** 2 * height

# Example usage
radius = 5.0
height = 10.0
volume = calculate_cylinder_volume(radius, height)
print(f"The volume of the cylinder with radius {radius} and height {height} is: {volume:.2f}")
