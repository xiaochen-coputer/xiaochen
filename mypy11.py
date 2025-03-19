import random
poetry=('山行','赠刘景文','夜书所见','望天门山','饮湖上初晴后雨','望洞庭')
s=set()
while len(s)<3:
    index=random.randint(0,5)
    poet=poetry[index]
    s.add(poet)
print(s)
