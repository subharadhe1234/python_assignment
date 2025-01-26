import sys
import subprocess
import os
if len(sys.argv)>1:
    data=sys.argv[1]
    subprocess.run(["fsutil", "file", "createnew", f"{data}", "0"])

else:
    print("Radhe")