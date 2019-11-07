import sys

for idx,line in enumerate(sys.stdin):
    group,seq=line.strip().split("\t")
    print("> {}-{}".format(idx,group.replace(" ","_")))
    print(seq)
    print()
    
