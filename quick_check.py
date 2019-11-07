import sys

def classify(result_list):
    nearest1=result_list[0][0].split("-")[1]
    return nearest1

results={} #key: seq  value: [(target,score),(target,score),...]

for line in sys.stdin:
    line=line.strip()
    if line.startswith("#"):
        continue
    src,targ,escore=line.split("\t")
    escore=float(escore)
    results.setdefault(src,[]).append((targ,escore))

total=0
correct=0
for k,v in results.items():
    k=k.split("-")[1]
    total+=1
    if k==classify(v):
        correct+=1
print("ACC",correct/total*100, "(",correct,"/",total,")")

    

    
