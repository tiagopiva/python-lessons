# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


nome = input("Enter file:")
if len(nome) < 1:
   nome = "mbox-short.txt"
arquivo = open(nome)
lista = list()
for linha in arquivo:
    if linha.startswith('From:'):
        continue
    if linha.startswith('From'):       
        linha = linha.split()
        lista.append(linha[1])


dicionario = dict()
maismandou = None
qtd = None
for emails in lista:
    dicionario[emails]=dicionario.get(emails,0)+1
for k,v in dicionario.items():
    if qtd is None or v > qtd:
        maismandou = k
        qtd = v
        
        
print(maismandou,qtd)
