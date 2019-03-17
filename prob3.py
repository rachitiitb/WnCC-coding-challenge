import cmath

myfile = open('C:\\Users\\DELL\\Desktop\\timestat.txt')

elements = myfile.readlines()       #makes each line of the timestat file an element of a list 'elements'
i= 1

real = []                       #list of real time values
user = []                       #list of user time values
sys = []                        #list of sys time values

while(i<len(elements)):
    real1 = elements[i].split()[1].split('m')[1].split('s')[0]      #time in seconds
    real2 = elements[i].split()[1].split('m')[0]                    #time in minutes
    real.append(float(real1)+60*float(real2))

    user1 = elements[i+1].split()[1].split('m')[1].split('s')[0]    #time in seconds
    user2 = elements[i+1].split()[1].split('m')[0]                  #time in minutes
    user.append(float(user1)+60*float(user2))

    sys1 = elements[i+2].split()[1].split('m')[1].split('s')[0]     #time in seconds
    sys2 = elements[i+2].split()[1].split('m')[0]                   #time in minutes
    sys.append(float(sys1)+60*float(sys2))

    i = i+4                                    #not i+3 since there is a blank line in between

sum1 = 0
sum2 = 0
sum3 = 0

for item1 in real:
    sum1 += item1                   #stores summation of real time values
for item2 in user:
    sum2+= item2                    #stores summation of user time values
for item3 in sys:
    sum3+=item3                     #stores summation of sys time values

n = i//4                    #no. of runs

avg1 = sum1/n               #average of real time values
avg2 = sum2/n               #average of user time values
avg3 = sum3/n               ##average of sys time values

std1 = 0
std2 = 0
std3 = 0

for num1 in real:
    std1+= pow((num1 - avg1),2)             #stores summation of (X(i) - X(avg))^2

for num2 in user:
    std2+= pow((num2-avg2),2)               #stores summation of (X(i) - X(avg))^2

for num3 in sys:
    std3 += pow((num3-avg3),2)              #stores summation of (X(i) - X(avg))^2


dev1= cmath.sqrt(std1/n)            #standard deviation of real time values
dev2 = cmath.sqrt(std2/n)           #standard deviation of user time values
dev3 = cmath.sqrt(std3/n)           #standard deviation of sys time values

                                    #dev1,dev2 and dev3 are complex numbers

count1= 0               #will store number of values in
count2 =0               # average-standard deviation to average + standard deviation
count3 = 0              # for real,user and sys respectively.

for obj1 in real:
    if(abs(obj1-avg1)<dev1.real):           #compares absolute value of difference between time reading and average for real time
        count1+=1
for obj2 in user:
    if(abs(obj2-avg2)<dev2.real):           #compares absolute value of difference between time reading and average for user time
        count2+=1
for obj3 in sys:
    if(abs(obj3-avg3)<dev3.real):           #compares absolute value of difference between time reading and average for sys time
        count3+=1

print('Number of runs :',i//4)
print('Average time statistics')
print('real ',avg1 ,'user ',avg2,'sys ',avg3)
print('Standard deviation of Time statistics ')
print('real ',dev1.real,'user ',dev2.real,'sys ',dev3.real)
print('Number of runs within average- standard deviation to average+standard deviation' )
print('real ',count1 , 'user ',count2 ,'sys ',count3)
