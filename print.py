import os
import sys
import subprocess
import pdfkit

pdfkit.from_file("slip.html", "out.pdf")

os.system("lp out.pdf")
#opener = "open" if sys.platform == "darwin" else "xdg-open"
#subprocess.call([opener, "out.pdf"])
