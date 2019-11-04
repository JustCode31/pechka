import time
x=0
starttime=int(input("введите время включения "))
temp=int(input("напишите начальную температуру "))
maxtemp=int(input("напишите максимальную температуру "))
# print("просьба далее время указывать в минутах")
speedg=int(input("напишите сколько градусов поднимается за минуту "))
wait=int(input("напишите время выстойки "))
speedc=int(input("напишите сколько градусов опускается за минуту "))
speedup=speedg/1
c=0
b=0
q=0
y=0
p=0
while q==0:
    while c==0:
        if temp<maxtemp:
            temp+=speedup
            x+=1
            # time.sleep(60)
        elif temp>maxtemp:
            temp=maxtemp
        elif temp==maxtemp:
            y=x
            # time.sleep(2400)
            x+=wait
            p=x
            c+=1
    while b==0:
        if temp>1200:
            temp-=speedc
            x+=1
        elif temp<=1200:
            b+=1
    v=x/60
    e1=v
    # print(e1)
    e1%=10
    # print(e1)
    v=v*10
    v=v//1
    v=v/10
    # e=e%10
    e=e1
    e=e*0.1
    v=v-e
    # print(e, v)
    e=e*0.6
    e%=10
    v//=1
    e = e * 100
    e //= 1
    e/=100
    # print(e)
    prtime=v+e
    pv=p/60
    pe1=pv
    # print(e1)
    pe1%=10
    # print(e1)
    pv=pv*10
    pv=pv//1
    pv=pv/10
    # e=e%10
    pe=pe1
    pe=pe*0.1
    pv=pv-pe
    # print(e, v)
    pe=pe*0.6
    pe%=10
    pv//=1
    pe = pe * 100
    pe //= 1
    pe/=100
    p=pe+pv
    p+=starttime
    yv=y/60
    ye1=yv
    # print(e1)
    ye1%=10
    # print(e1)
    yv=yv*10
    yv=yv//1
    yv=yv/10
    # e=e%10
    ye=ye1
    ye=ye*0.1
    yv=yv-ye
    # print(e, v)
    ye=ye*0.6
    ye%=10
    yv//=1
    ye = ye * 100
    ye //= 1
    ye/=100
    y=yv+ye
    y+=starttime
    prtime+=starttime
    # print(prtime)
    print("вы должны прийти в ", prtime,", начало охлаждения в ", p,", время выхода на режим:", y)
    r=input()
time.sleep(60)

