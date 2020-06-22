# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#print(data)
aa = np.shape(data)
print(aa)
census = np.concatenate((data,new_record))
#print(census)
a = np.shape(census)
print(a)
#Code starts here
age = np.array(census[:,0])
print(age)
max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = np.std(age)
print(age_std)
print("=============")
race_0 = census[census[:,2] == 0]
#print(race_0)
race_1 = census[census[:,2] == 1]
#print(race_1)
race_2 = census[census[:,2] == 2]
#print(race_2)
race_3 = census[census[:,2] == 3]
#print(race_3)
race_4 = census[census[:,2] == 4]
#print(race_4)
len_0 = len(race_0)
print(len_0)
len_1 = len(race_1)
print(len_1)
len_2 = len(race_2)
print(len_2)
len_3 = len(race_3)
print(len_3)
len_4 = len(race_4)
print(len_4)
print("=============")
minority_race = len_3
print(minority_race) 
print("[Warning here may be the ans is not true]")
#print(len(census))

#///////////////////////////////////////////////////////
#*******************************************************
#////////////SENIOR CITIZEN/////////////////

senior_citizens = []
working_hours_sum = 0
for i in range(len(census)):
        if census[i,0] > 60:
                senior_citizens.append(i)
                working_hours_sum = working_hours_sum + census[i,6]
                
#for i in census[:,0]:
 #   if i > 60:
  #      senior_citizens.append(i)
        #working_hours_sum += j
print(working_hours_sum)
print(senior_citizens)
senior_citizens = np.asarray(senior_citizens)
print("senior citizens")
print(senior_citizens)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


#cmhfdmhtdjydhm//////////////////////////\
high = []
low = []
avg_pay_high = []
avg_pay_low = []
for i in range(len(census)):
        if census[i,1] > 10:
                high.append(census[i,:])
                avg_pay_high.append(census[i,7])

        else:
                low.append(census[i,:])
                avg_pay_low.append(census[i,7])

high = np.asarray(high)
print("high")
print(high)
low = np.asarray(low)
print("low")
print(low)

avg_pay_high = sum(avg_pay_high) / len(avg_pay_high)
print(avg_pay_high)
avg_pay_low = sum(avg_pay_low) /len(avg_pay_low)
print(avg_pay_low)
#averaage pay for high







