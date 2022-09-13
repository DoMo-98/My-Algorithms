

# Show Mandelbrot fractal
def mandelbrot( x, y, max_iterations ):
    c = complex( x, y )
    z = 0
    for i in range( max_iterations ):
        z = z ** 2 + c
        if abs( z ) > 2:
            return i
    return max_iterations

# My Julia fractal ???
def get_y( x, c ):
    return ( x ** 2 ) + c

# Show Julia fractal
def julia( x, y, max_iterations ):
    c = complex( x, y )
    z = 0
    for i in range( max_iterations ):
        z = z ** 2 + c
        if abs( z ) > 2:
            return i
    return max_iterations