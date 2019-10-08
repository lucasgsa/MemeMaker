#coding: utf-8

from PIL import ImageGrab,Image 
import pytesseract, numpy
# Essa linha é apenas para evitar um erro dado no meu pc, talvez em outro não precisa, só tirar se perceber esse erro.
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class IKimage():
	def capturaTela(self):
		"""
		Captura a tela atual do computador e retorna.
		"""
		return ImageGrab.grab()
		
	def abreImagem(self, caminho):
		"""
		Abre um arquivo de imagem e retorna.
		"""
		return Image.open(caminho)

	def retornaTexto(self, imagem):
		"""
		Retorna o texto contido em uma imagem.
		"""
		return pytesseract.image_to_string(imagem)

	def verificaImagem(self, imagem, blacklist):
		"""
		Verifica se em uma imagem contem determinadas palavras passadas em uma lista negra, e retorna uma lista com as palavras da lista negra que estao la.
		"""
		texto = self.retornaTexto(imagem)
		contidos = []
		for i in blacklist:
			if (i.upper() in texto or i.lower() in texto):
				contidos.append(i)
		return contidos
	def asArray(self, imagem):
		return numpy.array(imagem)
