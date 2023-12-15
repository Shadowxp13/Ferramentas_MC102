# -*- coding: utf-8 -*-

import os
import sys
import platform

if platform.system() == 'Windows':
	echo = 'type'
	comparar = 'fc'
	pythoncmd = 'python'
elif platform.system() == 'Linux':
	echo = 'cat'
	comparar = 'diff'
	pythoncmd = 'python3'
else:
	print("Sistema operacional não suportado.")
	sys.exit()

numlab = str(input("Digite o número do laboratório: ").zfill(2))
if not os.path.exists(f"Laboratório {numlab}"):
	print("Diretório", f'"Laboratório {numlab}"', "não encontrado.")
	sys.exit()


os.chdir(f"Laboratório {numlab}")

print("1 - Executar todos os testes")
print(f"2 - Executar apenas o arquivo lab{numlab}.py")

labfile = (f"lab{numlab}.py")

if not os.path.exists(labfile):
	print("Arquivo", labfile, "não encontrado.")
	sys.exit()

whichfile = input("Escolha sua opção: ")

if whichfile == '2':
	os.system(f'{pythoncmd} lab{numlab}.py')

else:
	i = 1
	testfile = "arq" + "{:02d}".format(i) + ".in"

	while (os.path.exists(testfile)):
		resfile = "arq" + "{:02d}".format(i) + ".out"
		if not os.path.exists(resfile):
			print("Arquivo", resfile, "não encontrado.")
			sys.exit()

		outfile = "arq" + "{:02d}".format(i) + ".res"
		if (os.path.exists(outfile)):
			answer = input("Arquivo " + outfile +
			               " existente. Pode ser sobrescrito (S/n)?")
			if answer == "n" or answer == "N":
				sys.exit()

		difffile = "arq" + "{:02d}".format(i) + ".diff"
		if (os.path.exists(difffile)):
			answer = input("Arquivo " + difffile +
			               " existente. Pode ser sobrescrito (S/n)?")
			if answer == "n" or answer == "N":
				sys.exit()

		os.system(f"{pythoncmd} " + labfile + " < " + testfile + " > " + outfile)
		if os.system(f"{comparar} " + outfile + " " + resfile + " > " + difffile) == 0:
			print("Teste ", "{:02d}".format(i), ": resultado correto")
		else:
			print("Teste ", "{:02d}".format(i), ": resultado incorreto")
			print(">>> Sua resposta:")
			os.system(f"{echo} " + outfile)
			print("\n", ">>> Resposta correta:")
			os.system(f"{echo} " + resfile)
			
		os.remove(outfile)
		os.remove(difffile)
		i = i + 1
		testfile = "arq" + "{:02d}".format(i) + ".in"
