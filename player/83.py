a=int(input());
b=[];
d=0;
for i in range(a):
    b.append(int(input()));
for i in b:
    d=d|int(i)
print(d);
