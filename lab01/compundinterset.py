#CI =p(1+r/100)^t-p
principle = float(input("Enter the principle:"))
rate = float(input("Enter the rate:"))
time = float(input("Enter the time:"))
CI = principle*(1+rate/100)**time-principle
print("The compound interest:", CI)