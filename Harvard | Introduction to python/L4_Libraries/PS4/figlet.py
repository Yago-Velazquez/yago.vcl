# https://pypi.org/project/pyfiglet/
from pyfiglet import Figlet
import sys
import random

fonts = Figlet().getFonts()

def printing(font_used):
    x = str(input("Input: "))
    f = Figlet(font= font_used)
    print(f"Output:\n {f.renderText(x)}")

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    printing(sys.argv[2])
elif len(sys.argv) == 1:
    printing(random.choice(fonts))
else:
    print("Invalid Usage")
    sys.exit()