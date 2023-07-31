# proto-board-circuit-drawing
Using images to visualize how to set up electronic components on proto boards

## Basic Shapes
* Points
The point(xy, fill) method draws individual pixels. The xy argument represents a list of the points you want to draw. The list can be a list of
x- and y-coordinate tuples, such as [(x, y), (x, y), ...], or a list of x-
and y-coordinates without tuples, such as [x1, y1, x2, y2, ...]. The fill argument is the color of the points and is either an RGBA tuple or a string 
of a color name, such as 'red'. The fill argument is optional.
* Lines
The line(xy, fill, width) method draws a line or series of lines. xy is either a list of tuples, such as [(x, y), (x, y), ...], or a list of integers,
such as [x1, y1, x2, y2, ...]. Each point is one of the connecting points on the lines you’re drawing. The optional fill argument is the color of the
lines, as an RGBA tuple or color name. The optional width argument is the width of the lines and defaults to 1 if left unspecified.
* Rectangles
The rectangle(xy, fill, outline) method draws a rectangle. The xy argu- ment is a box tuple of the form (left, top, right, bottom). The left and top
values specify the x- and y-coordinates of the upper-left corner of the rect- angle, while right and bottom specify the lower-right corner. The optional
fill argument is the color that will fill the inside of the rectangle. The optional outline argument is the color of the rectangle’s outline.
* Ellipses
The ellipse(xy, fill, outline) method draws an ellipse. If the width and height of the ellipse are identical, this method will draw a circle. The xy
argument is a box tuple (left, top, right, bottom) that represents a box that precisely contains the ellipse. The optional fill argument is the color
of the inside of the ellipse, and the optional outline argument is the color of the ellipse’s outline.
* Polygons
The polygon(xy, fill, outline) method draws an arbitrary polygon. The xy argument is a list of tuples, such as [(x, y), (x, y), ...], or integers, such
as [x1, y1, x2, y2, ...], representing the connecting points of the polygon’s sides. The last pair of coordinates will be automatically connected to the
first pair. The optional fill argument is the color of the inside of the poly- gon, and the optional outline argument is the color of the polygon’s outline.
