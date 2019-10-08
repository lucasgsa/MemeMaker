#coding: utf-8

def abrirConfig_texto():
	arquivo = open('memes_config.txt', 'r')
	return arquivo.read()

def lerConfig():
	config = abrirConfig_texto().split("\n")
	dic_config = {}
	for linha in range(len(config)):
		if len(config[linha]) == 0 or config[linha][0] == "#": continue
		if config[linha][0] == "+":
			lista = []
			nome = config[linha]
			i = linha+1
			while True:
				if len(config[i]) == 0 or config[i][0] == "#":
					i += 1
					continue
				elif config[i] == ">FIM<":
					break
				elif config[i][0] == "+":
					break
				lin = config[i].split("|")
				porcentagem = lin[0].split(",")
				tamanhos = lin[1].split(",")
				if len(porcentagem) <= 1:
					raise "O meme deve conter duas porcentagens!"
					break
				elif len(porcentagem) > 2:
					raise "O meme deve conter duas porcentagens!"
					break
				elif len(tamanhos) <= 1:
					raise "O meme deve conter dois tamanhos!"
					break
				elif len(tamanhos) > 2:
					raise "O meme deve conter dois tamanhos!"
					break
				else:
					lista.append(((int(porcentagem[0]),int(porcentagem[1])),((int(tamanhos[0]),int(tamanhos[1])))))
				i += 1
			dic_config[nome[1:len(nome)]] = lista
		if config[linha] == ">FIM<":
			break
	return dic_config
			
print lerConfig()
