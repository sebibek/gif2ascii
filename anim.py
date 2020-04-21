import pyglet, sys, os, time
from sty import Style, RgbFg, fg

def color(framesL, width, chars, anim):
    clear_console = 'clear' if os.name == 'posix' else 'cls'
    # Gets a list of RGB ('RGB') values of each frame
    framesRGB = [frame.image.get_data('RGB', -width*3) for frame in anim.frames]
    print('animation ready2run, running..\n')
    # Step through forever, frame by frame
    while True:
        for frame,frameL in zip(framesRGB, framesL):
            # Built up the string, by translating luminance values to characters
            outstr = ''

            # Define color from contigously stored RGB vals, map Luminance and repeat each char twice for correct aspect ratio
            for i in range(0,len(frame)-2,3):
                R = frame[i]
                G = frame[i+1]
                B = frame[i+2]
                pixel = frameL[i//3]
                fg.color = Style(RgbFg(R, G, B))
                outstr += fg.color + chars[(int(pixel) * (len(chars) - 1)) // 255]*2  + fg.rs + \
                          ('\n' if (i + 3) % (width*3) == 0 else '')

            # Clear the console
            os.system(clear_console)

            # Write the current frame on stdout and sleep
            sys.stdout.write(outstr)
            sys.stdout.flush()
        
            #time.sleep(0.01)

        time.sleep(3)


def greyscale(framesL, width, chars):
    clear_console = 'clear' if os.name == 'posix' else 'cls'
    print('animation ready2run, running..\n')
    # Step through forever, frame by frame
    while True:
        for frame in framesL:
            # Built up the string, by translating luminance values to characters
            outstr = ''
            for (i, pixel) in enumerate(frame):
                outstr += chars[(int(pixel) * (len(chars) - 1)) // 255]*2 + \
                          ('\n' if (i + 1) % width == 0 else '')

            # Clear the console
            os.system(clear_console)

            # Write the current frame on stdout and sleep
            sys.stdout.write(outstr)
            sys.stdout.flush()
        
            #time.sleep(0.01)

        time.sleep(3)

def animgif_to_ASCII_animation(animated_gif_path, colored=False, invert=False):
    # map greyscale to characters
    chars = ('#', '#', '@', '%', '=', '+', '*', ':', '-', '.', ' ') if invert is False else (' ', '.', '-', ':', '*', '+', '=', '%', '@', '#', '#')

    # load image
    anim = pyglet.image.load_animation(animated_gif_path)
    width = anim.frames[0].image.width # global img width
    # Gets a list of luminance ('L') values of each frame
    framesL = [frame.image.get_data('L', -width) for frame in anim.frames]

    if colored: color(framesL, width, chars, anim)
    else: greyscale(framesL, width, chars)

 

# run the animation based on some animated gif
if __name__ == '__main__':  # EXAMPLE USE: can be done from console
    # set parameters(config)
    colored = True # enable color mapping
    invert = False # invert greyscale (ASCII) mapping
    animated_gif_path = u"C:/Users/sebi/Desktop/GIFs/test.gif"
    # run the animation based on some animated gif with current parameters
    conv = animgif_to_ASCII_animation(animated_gif_path, colored, invert)
