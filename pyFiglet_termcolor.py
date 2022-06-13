# By Ezz

# -----------------------------
# Modules => Bult In Modules --
# -----------------------------
# [1] Modules is A File Countain A Set Of Functions
# [2] You Can  Import Module In Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# -------------------------------------------------

# import Main Module
# Import One Or Two Functions From Modules

import pyfiglet
import termcolor
from random import randint, random

# Show Where Is
# print(random)

# Show ALl Functions Inside Modules
# print(dir(random))

print(f"Print Random Float: {random()}")
print(f"Print Random Integer: {randint(1, 10)}")

print("_" * 35)

# ----------------------------------
# -- Modules => Craete Own Module --
# ----------------------------------

# Alias
import My_Module as ee

print(ee.cleanword("hdjvbdhfavfs"))


print("_" * 35)

# -----------------------------------------
# -- Module => Install External Packages --
# -----------------------------------------
# [1] Module vs Packages
# [2] External packages Downloaded From The Enternet
# [3] You Can Install Packages With Python Manager PIP
# [4] PIP Install The Packages And Its Dependecies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages Nd Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/
# --------------------------------------------------------------------

# print(dir(pyfiglet))
# print(dir(termcolor))

# print(pyfiglet.figlet_format("Ezz"))
# print(termcolor.colored("Ezz", "blue"))

print(termcolor.colored(pyfiglet.figlet_format("Ezz"), color="red"))
