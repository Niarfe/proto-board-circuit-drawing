from PIL import Image, ImageDraw


# BOARD PARAMETERS
XOFFSET=253
YOFFSET=183
YPITCH=32.8
XPITCH=32.8
RADIUS=7

# PRIVATE
def _convert_to_xy(cell):
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

def _add_circle(comps, cell, fill='red', outline='cyan'):
    global RADIUS
    x, y = _convert_to_xy(cell)
    comps.ellipse((x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS), fill=fill, outline=outline)

# PUBLIC
def add_jumper(comps, C1, C2, fill='blue', width=12):
    c1_x, c1_y = _convert_to_xy(C1)
    c2_x, c2_y = _convert_to_xy(C2)
    _add_circle(comps, C1, fill='silver')
    _add_circle(comps, C2, fill='silver')
    comps.line([(c1_x, c1_y),(c2_x, c2_y)], fill=fill, width=2*width)

def main(file_path):
    lines = open(file_path, 'r').readlines()
    board = Image.open('source/images/1608-00.jpg')
    components = ImageDraw.Draw(board)
    
    for line in lines:
        if line.startswith('jumper'):
            _, c1, c2 = line.strip().split()
            add_jumper(components, c1, c2)

    board.show()

## TESTS ##
def test_convert():
    assert (1 , 1) == _convert_to_xy('J1')
    assert (10 ,1) == _convert_to_xy('A1')

if __name__=="__main__":    
    import sys
    assert len(sys.argv) == 2, "Pass in file to process"

    main(sys.argv[1])

