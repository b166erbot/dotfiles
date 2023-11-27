from subprocess import getoutput

saída = getoutput('sudo docker ps -a').split('\n')[1]
saída = saída.split()[0]
print(saída)
