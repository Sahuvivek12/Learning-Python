# Secret a language

# Make a program to encode and decode strings

st = "Hello i am vivek"
stnew = st.rsplit(" ")

if (len(st)>=3):
    r1 = "sdf"
    r2 = "gjr"
    st = st[::-1]
    st = st[1:] + st[0]
    print(r1+st+r2)
else:
    
    print(st)