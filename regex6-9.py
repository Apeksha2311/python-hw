import re
data="7894561230,8974563210,235467,9892465153"
ptr=r"[6-9]\d{9}"
x=re.findall(ptr,data)
c=len(x)
print(c)


#que 2-without regex
def count_digit(i):

    counter = 0

    while i>0:

        i=i//10

        counter = counter + 1



    return counter



st = '678123456,953423151,8523121,98989231,3343534231'

li = st.split(',')

print(li)



for i in li:

    i = int(i)

    count = count_digit(i)



    if count==10:

        print('valid')

    else:

        print('invalid')
