import pyglet, sys, os, time
from sty import Style, RgbFg, fg

class gif2ASCII:
    clear_console = 'clear' if os.name == 'posix' else 'cls'
    def __init__(self, animated_gif_path):      
        # load image
        self.anim = pyglet.image.load_animation(animated_gif_path)
        self.width = self.anim.frames[0].image.width # global img width
        # Gets a list of luminance ('L') values of each frame
        self.framesL = [frame.image.get_data('L', -self.width) for frame in self.anim.frames]

    def animate(self, colored=False, invert=True):
        # map greyscale to characters
        self.chars = ('#', '#', '@', '%', '=', '+', '*', ':', '-', '.', ' ') if invert is True else (' ', '.', '-', ':', '*', '+', '=', '%', '@', '#', '#')
        self.len = len(self.chars)

        if colored: self.color()
        else: self.greyscale()

    def greyscale(self):
        print('animation ready2run, running..\n')
        # Step through forever, frame by frame
        while True:
            for frame in self.yielderL():
                # Built up the string, by translating luminance values to characters
                outstr = ''

                # Map Luminance and repeat each char twice for correct aspect ratio
                for (i, pixel) in enumerate(frame):
                    outstr += self.chars[(int(pixel) * (self.len - 1)) // 255]*2 + \
                              ('\n' if (i + 1) % self.width == 0 else '')

                # Clear the console
                os.system(self.clear_console)

                # Write the current frame on stdout and sleep
                sys.stdout.write(outstr)
                sys.stdout.flush()
            
                #time.sleep(0.01)

            time.sleep(3)

    def yielderRGB(self):
        for frame in self.framesRGB:
            yield frame

    def yielderL(self):
        for frame in self.framesL:
            yield frame

    def color(self):
        # Gets a list of RGB ('RGB') values of each frame
        if not self.framesRGB:
            self.framesRGB = [frame.image.get_data('RGB', -self.width*3) for frame in self.anim.frames]
        print('animation ready2run, running..\n')
        # Step through forever, frame by frame
        while True:
            for frame,frameL in zip(self.yielderRGB(), self.yielderL()):
                # Built up the string, by translating luminance values to characters
                outstr = ''

                # Define color from contigously stored RGB vals, map Luminance and repeat each char twice for correct aspect ratio
                for i in range(0,len(frame)-2,3):
                    R = frame[i]
                    G = frame[i+1]
                    B = frame[i+2]
                    pixel = frameL[i//3]
                    fg.color = Style(RgbFg(R, G, B))
                    outstr += fg.color + self.chars[(int(pixel) * (self.len - 1)) // 255]*2  + fg.rs + \
                              ('\n' if (i + 3) % (self.width*3) == 0 else '')

                # Clear the console
                os.system(self.clear_console)

                # Write the current frame on stdout and sleep
                sys.stdout.write(outstr)
                sys.stdout.flush()
            
                #time.sleep(0.01)

            time.sleep(3)

    
if __name__ == '__main__':  # EXAMPLE USE: can be done from console
    # set parameters(config)
    colored = False # enable color mapping
    invert = True # invert greyscale (ASCII) mapping
    animated_gif_path = u"C:/Users/sebi/Desktop/GIFs/test.gif"
    # create a new gif2ASCII converter
    conv = gif2ASCII(animated_gif_path)
    # run the animation based on some animated gif with current parameters
    conv.animate(colored, invert)