import math
import sys

OUTPUT_SIZE=32

#cos sin
#-sin cos

def square_poly(size):
    return [(-size,-size), (size,-size), (size,size), (-size,size)]

def rotate_poly(poly, angle):
    angle=-angle
    return [(x*math.cos(angle)+y*math.sin(angle), (-x*math.sin(angle)+y*math.cos(angle))) for (x,y) in poly]

def is_inside(poly, (tx,ty)):
    inside = False

    for i in range(0,len(poly)):
        xi=poly[i][0]
        yi=poly[i][1]
        xj=poly[(i+1)%len(poly)][0]
        yj=poly[(i+1)%len(poly)][1]
        if ( ((yi>ty) != (yj>ty)) and (tx < (xj-xi)*(ty-yi) / (yj-yi) + xi) ):
            inside = not inside
    return inside

def render(figure, boundary):
    # Returns an array of strings containing the characters . and #
    ret=[]
    for y in range(0,OUTPUT_SIZE):
        s=''
        for x in range(0,OUTPUT_SIZE):
            xp=float(x)/OUTPUT_SIZE*boundary*2-boundary
            yp=float(y)/OUTPUT_SIZE*boundary*2-boundary
            xp+=boundary/OUTPUT_SIZE
            yp+=boundary/OUTPUT_SIZE
            inside = is_inside(figure, (xp,yp))
            if (inside):
                s+='#'
            else:
                s+='.'
        ret.append(s)
    return ret

def get_tile(bitmap, sx, sy):
    ret=[]
    for y in range(0,8):
        val=0
        t=128
        for x in range(0,8):
            if bitmap[sy+y][sx+x]=='#':
                val += t
            t/=2
        ret.append(val)
    return ret

def output_tiles(f, bitmap):
    # Outputs the bitmap tile by tile in row major order
    for y in range(0,OUTPUT_SIZE/8):
        for x in range(0,OUTPUT_SIZE/8):
            tile=get_tile(bitmap, 8*x, 8*y)
            f.write(bytearray(tile))

def output_raw(f, bitmap):
    # Outputs the bitmap in row major order
    output=[]
    for y in range(0,OUTPUT_SIZE):
        for x in range(0,OUTPUT_SIZE/8):
            val=0
            t=128
            for xofs in range(0,8):
                if bitmap[y][x*8+xofs]=='#':
                    val += t
                t/=2
            output.append(val)
    f.write(bytearray(output))

ROT_FRAMES = 16
SIZES = [0.6, 0.7, 0.8, 0.9]


with open("squares.bin", "wb") as f:
    for size in SIZES:
        for angle in [math.pi/2*x/ROT_FRAMES for x in range(0,ROT_FRAMES)]:
            bitmap=render(rotate_poly(square_poly(size), angle), 1.8)
            #output_tiles(f, bitmap)
            output_raw(f, bitmap)
