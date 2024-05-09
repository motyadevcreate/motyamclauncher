print('Building motyamc, please wait...')

from time import sleep as wait

wait(0.1)

import pip
import os

pip.main(["install", "pyinstaller"])

os.system("pyinstaller launcher.py --onefile")

print("Done")

wait(1)
