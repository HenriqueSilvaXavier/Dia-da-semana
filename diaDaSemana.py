from datetime import datetime
hoje=datetime(year=2023, month=7, day=22)
s_hoje=7
print(hoje)
n=input("Digite a data: ")
n=n.split("/")
for k in range(0, len(n)):
	n[k]=int(n[k])
ndata=datetime(year=n[2], month=n[1], day=n[0])
d=(ndata-hoje).days+1
s=abs(d)%7
if d>=0:
	sd=(s_hoje+s)%7
elif d<0:
	sd=s_hoje-s
sd=sd-1
if sd==-1:
	sd=6
elif sd==0:
	sd=7
if sd==1:
	print("O dia da semana da data é domingo")
elif sd==2:
	print("O dia da semana da data é segunda-feira")
elif sd==3:
	print("O dia da semana da data é terça-feira")
elif sd==4:
	print("O dia da semana da data é quarta-feira")
elif sd==5:
	print("O dia da semana da data é quinta-feira")
elif sd==6:
	print("O dia da semana da data é sexta-feira")
elif sd==7:
	print("O dia da semana da data é sábado")