import minibar
import time
from minibar.widgets import Widget

for i in minibar.bar(range(50), template="{i:4}/{total:4} {bar:30}"):
    time.sleep(0.1)
