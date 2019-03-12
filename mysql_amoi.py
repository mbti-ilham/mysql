#!/usr/bin/python3
import mysql.connector

#tuple 
#fetchone recuppere une seul ligne

monServeur = "ensembldb.ensembl.org"
monLogin = "anonymous"
connexion = mysql.connector.connect(host = monServeur, user = monLogin)
curseur = connexion.cursor() # permet d'effectuer des requetes
"""
#1
curseur.execute("select version()") # ne retourne qu’une seule ligne
row = curseur.fetchone() # on recupere la ligne resultat
print("Version du serveur MySQL distant : ", row[0])

curseur.execute("select now()") # ne retourne qu’une seule ligne
row = curseur.fetchone() # on recupere la ligne resultat
print(type(row))
print("Date actuelle sur le serveur distant : ", row[0])
 

curseur.execute("select user()") # ne retourne qu’une seule ligne
row = curseur.fetchone() # on recupere la ligne resultat
print("information user : ", row[0])

curseur.execute("select database()") # ne retourne qu’une seule ligne
row = curseur.fetchone() # on recupere la ligne resultat
print("Base de donnee : ", row[0])

#2
curseur.execute("show databases") # ne retourne  lignes
rows = curseur.fetchall() # on recupere la ligne resultat
for row in rows:
	print(row[0])
#table transcri on peut recuperer transcript_id, gene_id
#trouver le gene qui a le plus de transcript
#group by having
#fetchall

"""
"""
#3
c=curseur.execute("show databases LIKE 'homo_sapiens_core\_%'")	
rows = curseur.fetchall() # on recupere la ligne resultat
row = curseur.fetchone()

for i in range(len(rows)):
		print (rows[i])
		la_plus_recente = rows[i]
print("%d lignes renvoyées" % len(rows))
print("homo_sapiens_core_ la plus récente est:",la_plus_recente)


"""

curseur.execute("use homo_sapiens_core_95_38")
row = curseur.fetchone()
print(row[0])



curseur.execute("select gene_id, count(*)FROM transcript GROUP BY gene_id HAVING count(*)FROM transcrit GROUP BY gene_id);")
rows = curseur.fetchall() 
row=rows[0]
print("%s" % row[0] ," ", row[1] )


transcript1= str(row[0])
print("%d ligne renvoyer"%len(rows))

curseur.execute("select transcript1 from transcript where geneid like"+transcript1)
rows = curseur.fetchall()
for row in rows:
 print("%s" % row[0])
print("%d lignes renvoyées" % len(rows))

curseur.close()
connexion.close()


