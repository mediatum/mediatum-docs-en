# remove duplicate newlines for all rst files in the current dir:
#   for x in *.rst; do { rm -f $x; python remove_newline.py > $x; } < $x; done

import sys
lastline_empty = False

for line in sys.stdin:
    stripped = line.strip()
    if not stripped:
        if not lastline_empty:
            sys.stdout.write("\n")
        lastline_empty = True
    else:
        lastline_empty = False
        sys.stdout.write(line)
