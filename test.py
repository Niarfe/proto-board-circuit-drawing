from PIL import Image, ImageDraw

board = Image.open('source/images/1608-00.jpg')
components = ImageDraw.Draw(board)


XOFFSET=253
YOFFSET=183
YPITCH=32.8
XPITCH=32.8
RADIUS=7

def convert_to_xy(cell):
    global XOFFSET
    global YOFFSET
    global YPITCH
    global XPITCH
    assert isinstance(cell, str), f"Expected str type for cell but got {type(cell)}, {str(cell)}"
    letter = cell[:1]
    x = int(cell[1:3])
    x -= 1
    assert x >= 0 and x < 16, f"Could not extract y coord from {cell}"
    y = {
            'A': 11,
            'B': 10,
            'C': 9,
            'D': 8,
            'E': 7,
            'F': 4,
            'G': 3,
            'H': 2,
            'I': 1,
            'J': 0,
            }.get(letter, None)
    assert y != None, f"Could not extract x coord from {cell}"
    _x = XOFFSET + x*XPITCH 
    _y = YOFFSET + y*YPITCH 
    return _x, _y 

def add_circle(comps, cell, fill='red', outline='cyan'):
    global RADIUS
    x, y = convert_to_xy(cell)
    comps.ellipse((x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS), fill=fill, outline=outline)

def add_jumper(comps, C1, C2, fill='black', width=12):
    c1_x, c1_y = convert_to_xy(C1)
    c2_x, c2_y = convert_to_xy(C2)
    comps.line([(c1_x, c1_y),(c2_x, c2_y)], fill=fill, width=width)

    
for cell in ['J1','I1', 'H1', 'G1', 'F1',
        'A1', 'B1', 'C1', 'D1', 'E1',
        'J15', 'A15',
        'E5',]:
    add_circle(components, cell)

add_jumper(components, 'B1', 'F9')
board.show()

def test_convert():
    assert (1 , 1) == convert_to_xy('J1')
    assert (10 ,1) == convert_to_xy('A1')
