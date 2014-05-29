import minibar
import time
from minibar.widgets import Widget

minibar.get_terminal_width = lambda : 50

for i in minibar.bar(range(50)):
    time.sleep(0.1)
