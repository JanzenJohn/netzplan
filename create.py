from Task import convert_csv_to_flowchart
import os
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "i:o:hn", ["input=", "output=", "help", "no-graphviz"])
except getopt.GetoptError as GE:
        print(GE.msg)
        sys.exit()

in_file = ""
out_file = ""
has_graphviz_disabled = False
for opt, arg in opts:
    if opt in ("-i", "--input"):
        in_file = arg
    elif opt in ("-o", "--output"):
        out_file = arg
    else:
        print(open("help.txt").read())
        sys.exit()

if ".dot" == out_file[-4:]:
    has_graphviz_disabled = True




if not has_graphviz_disabled:
    with open("output.dot", "w") as f:
        f.write(convert_csv_to_flowchart(in_file))
    os.system(f"dot output.dot -Tpng > {out_file}")
    os.remove("output.dot")
else:
    with open(out_file, "w") as f:
        f.write(convert_csv_to_flowchart(in_file))