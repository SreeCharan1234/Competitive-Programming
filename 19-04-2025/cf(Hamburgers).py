#https://codeforces.com/contest/371/problem/C
#striver sde sheet Hambrugers
from collections import Counter 
d=Counter(input())
nb,ns,nc=map(int,input().split())
pb,ps,pc=map(int,input().split())
tp=int(input())
# print(d,type(nb),)
ub=nb//d['B']
us=ns//d['S']
uc=nc//d['C']
ans=min(ub,us,uc)
# print(nb,ns,nc,up,us,uc)
ub,us,uc=ub-(ans),us-(ans),uc-(ans)
nb,ns,nc=nb-(ans*d['B']),ns-(ans*d['S']),nc-(ans*d['C'])
print(nb,ns,nc,ub,us,uc)
print(ans)
while(ub>0 and us>0 and uc>0) and tp>0:
	y=0
	if ub==0 and tp>=(pb*(d['B']-nb)):
		print('nO')
		y=1
		tp=tp-(pb*(d['B']-nb))
		ub=ub+1
		nb=d['B']
	if us==0 and tp>=(ps*(d['S']-nc)):
		y=1
		tp=tp-(ps*(d['S']-nc))
		us=us+1
		ns=d['S']
		# print('NO')
	if uc==0 and tp>=(pc*(d['C']-nc)):
		y=1
		print(tp)
		tp=tp-(pc*(d['C']-nc))
		uc=uc+1
		nc=d['C']
		# print('NdfO',tp)
	# print(tp)
	if y==0:
		break
	if tp>=0 and y==1:
		ans=ans+1
		ub,us,uc=ub-1,us-1,uc-1
		nb,ns,nc=nb-d['B'],ns-d['S'],nc-d['C']
		# print(nb,ns,nc,ub,us,uc)

	else:
		break


print(ans)
print(nb,ns,nc,ub,us,uc)

totalprize=pb*(pb*(d['B']-nb)


