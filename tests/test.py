import time

from superbar import bar

for i in bar(range(1000)):
    time.sleep(0.01)
