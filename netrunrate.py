#to calculate net run rate of a given team

print('Enter the name of the team')
n=input()
print('Enter the number of runs scored by the team')
r=int(input())
print('Enter the number of overs faced')
o=int(input())
print('Enter the number of runs conceded')
r1=int(input())
print('Enter the number of overs bowled')
o1=int(input())

nr1=r/o
nr2=r1/o1
nrr=nr1-nr2
print('The net run rate of the team ' +n)
print(nrr)
