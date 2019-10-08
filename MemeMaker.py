# coding: UTF-8
import IK, util, numpy
from PIL import Image
editor = IK.IKimage()

dic_config = util.lerConfig()

def getMemeConfig(nome):
	return dic_config.get(nome)
	
def adicionaImagem(imagem_meme, imagem_nova, posis):
	matriz_meme = editor.asArray(imagem_meme)
	matriz_imagem = editor.asArray(imagem_nova)
	pos1,pos2 = posis
	print len(matriz_meme),len(matriz_meme[0])
	pos1 = int((float(pos1)/100)*len(matriz_meme))
	pos2 = int((float(pos2)/100)*len(matriz_meme[0]))
	for i in range(len(matriz_imagem)):
		for j in range(len(matriz_imagem[i])):
			if len(matriz_meme) < i+pos1+1 or len(matriz_meme[0]) < j+pos2+1: continue
			matriz_meme[i+pos1][j+pos2] = matriz_imagem[i][j]
	imagem = Image.fromarray(matriz_meme)
	return imagem

def main():
	entradaNomeMeme = raw_input()
	imagem = editor.abreImagem("Memes/"+entradaNomeMeme)
	for config in getMemeConfig(entradaNomeMeme):
		pos = config[0]
		tamanhos = config[1]
		temp_imagem = editor.abreImagem("Banco Imagens/"+raw_input("Nome da imagem para adicionar ao meme:"))
		temp_imagem = temp_imagem.resize((tamanhos[0],tamanhos[1]), Image.ANTIALIAS)
		temp = adicionaImagem(imagem,temp_imagem,pos)
		imagem = temp
	imagem.save(raw_input("salvar como?"))
	print "FIM"
	imagem.show()
main()
