from subprocess import getoutput

saída = getoutput('sudo docker ps -a').split('\n')
if len(saída) <= 1:
    exit(1)
saída = saída[1].split()[0]
print(saída)
