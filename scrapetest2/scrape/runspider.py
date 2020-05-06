import sys

sys.path.append("/home/rc/Documents/scrapetest2")
sys.path.append("/home/rc/Documents/scrapetest2/scrape")

import os
import cmd
from scrape.spiders import scpr

print('============================= Starting Spider ================================')
os.system('python3 /home/rc/Documents/scrapetest2/scrape/main.py')
print('=============================  Spider Closed ================================')
