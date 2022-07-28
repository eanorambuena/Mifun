import subprocess, sys, os

if len(sys.argv) < 2:
    print("Usage: py -m mifun <filename>")
    sys.exit(1)

file_name = sys.argv[1]

with open(file_name, "r") as f:
    text = f.read()

header = "from mifun import *"
footer = text.split("\n")[-1]

code = f"""{header}
{text[:-len(footer)]}
print({footer})"""

executable_name = "__mifun_executable__.py"

with open(executable_name, "w") as f:
    f.write(code)

subprocess.call([sys.executable, executable_name])

if os.path.exists(executable_name):
    os.remove(executable_name)
