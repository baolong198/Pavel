f0=0;
f1=1;
f2=1;
for n in range(0,1001):
    fn=f0+f1
    f0=f1
    f1=fn
    print('Dãy fibonaci thứ ',n,' là:',fn)