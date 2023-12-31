# proto-board-circuit-drawing
Using images to visualize how to set up electronic components on proto boards

## Requirements
* [pillow](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html)

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

## COLORS
* aliceblue                      : #f0f8ff
* antiquewhite                   : #faebd7
* aqua                           : #00ffff
* aquamarine                     : #7fffd4
* azure                          : #f0ffff
* beige                          : #f5f5dc
* bisque                         : #ffe4c4
* black                          : #000000
* blanchedalmond                 : #ffebcd
* blue                           : #0000ff
* blueviolet                     : #8a2be2
* brown                          : #a52a2a
* burlywood                      : #deb887
* cadetblue                      : #5f9ea0
* chartreuse                     : #7fff00
* chocolate                      : #d2691e
* coral                          : #ff7f50
* cornflowerblue                 : #6495ed
* cornsilk                       : #fff8dc
* crimson                        : #dc143c
* cyan                           : #00ffff
* darkblue                       : #00008b
* darkcyan                       : #008b8b
* darkgoldenrod                  : #b8860b
* darkgray                       : #a9a9a9
* darkgrey                       : #a9a9a9
* darkgreen                      : #006400
* darkkhaki                      : #bdb76b
* darkmagenta                    : #8b008b
* darkolivegreen                 : #556b2f
* darkorange                     : #ff8c00
* darkorchid                     : #9932cc
* darkred                        : #8b0000
* darksalmon                     : #e9967a
* darkseagreen                   : #8fbc8f
* darkslateblue                  : #483d8b
* darkslategray                  : #2f4f4f
* darkslategrey                  : #2f4f4f
* darkturquoise                  : #00ced1
* darkviolet                     : #9400d3
* deeppink                       : #ff1493
* deepskyblue                    : #00bfff
* dimgray                        : #696969
* dimgrey                        : #696969
* dodgerblue                     : #1e90ff
* firebrick                      : #b22222
* floralwhite                    : #fffaf0
* forestgreen                    : #228b22
* fuchsia                        : #ff00ff
* gainsboro                      : #dcdcdc
* ghostwhite                     : #f8f8ff
* gold                           : #ffd700
* goldenrod                      : #daa520
* gray                           : #808080
* grey                           : #808080
* green                          : #008000
* greenyellow                    : #adff2f
* honeydew                       : #f0fff0
* hotpink                        : #ff69b4
* indianred                      : #cd5c5c
* indigo                         : #4b0082
* ivory                          : #fffff0
* khaki                          : #f0e68c
* lavender                       : #e6e6fa
* lavenderblush                  : #fff0f5
* lawngreen                      : #7cfc00
* lemonchiffon                   : #fffacd
* lightblue                      : #add8e6
* lightcoral                     : #f08080
* lightcyan                      : #e0ffff
* lightgoldenrodyellow           : #fafad2
* lightgreen                     : #90ee90
* lightgray                      : #d3d3d3
* lightgrey                      : #d3d3d3
* lightpink                      : #ffb6c1
* lightsalmon                    : #ffa07a
* lightseagreen                  : #20b2aa
* lightskyblue                   : #87cefa
* lightslategray                 : #778899
* lightslategrey                 : #778899
* lightsteelblue                 : #b0c4de
* lightyellow                    : #ffffe0
* lime                           : #00ff00
* limegreen                      : #32cd32
* linen                          : #faf0e6
* magenta                        : #ff00ff
* maroon                         : #800000
* mediumaquamarine               : #66cdaa
* mediumblue                     : #0000cd
* mediumorchid                   : #ba55d3
* mediumpurple                   : #9370db
* mediumseagreen                 : #3cb371
* mediumslateblue                : #7b68ee
* mediumspringgreen              : #00fa9a
* mediumturquoise                : #48d1cc
* mediumvioletred                : #c71585
* midnightblue                   : #191970
* mintcream                      : #f5fffa
* mistyrose                      : #ffe4e1
* moccasin                       : #ffe4b5
* navajowhite                    : #ffdead
* navy                           : #000080
* oldlace                        : #fdf5e6
* olive                          : #808000
* olivedrab                      : #6b8e23
* orange                         : #ffa500
* orangered                      : #ff4500
* orchid                         : #da70d6
* palegoldenrod                  : #eee8aa
* palegreen                      : #98fb98
* paleturquoise                  : #afeeee
* palevioletred                  : #db7093
* papayawhip                     : #ffefd5
* peachpuff                      : #ffdab9
* peru                           : #cd853f
* pink                           : #ffc0cb
* plum                           : #dda0dd
* powderblue                     : #b0e0e6
* purple                         : #800080
* rebeccapurple                  : #663399
* red                            : (255, 0, 0)
* rosybrown                      : #bc8f8f
* royalblue                      : #4169e1
* saddlebrown                    : #8b4513
* salmon                         : #fa8072
* sandybrown                     : #f4a460
* seagreen                       : #2e8b57
* seashell                       : #fff5ee
* sienna                         : #a0522d
* silver                         : #c0c0c0
* skyblue                        : #87ceeb
* slateblue                      : #6a5acd
* slategray                      : #708090
* slategrey                      : #708090
* snow                           : #fffafa
* springgreen                    : #00ff7f
* steelblue                      : #4682b4
* tan                            : #d2b48c
* teal                           : #008080
* thistle                        : #d8bfd8
* tomato                         : #ff6347
* turquoise                      : #40e0d0
* violet                         : #ee82ee
* wheat                          : #f5deb3
* white                          : (255, 255, 255)
* whitesmoke                     : #f5f5f5
* yellow                         : #ffff00
* yellowgreen                    : #9acd32

## Useful links
* [Soldering @adafruit](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation?view=all&gclid=Cj0KCQjw2qKmBhCfARIsAFy8buLI-RFEaL_sZ2PfE6EhshMXE-QVQoXlbcb2_yKwp0NnH7ex6vxv0BUaAlggEALw_wcB)
