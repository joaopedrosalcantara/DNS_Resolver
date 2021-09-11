import socket, sys
import PySimpleGUI as sg

class TelaPython:
	#layout
	def __init__(self):
		layout = [
			[sg.Text('URL'), sg.Input(key='url')],
			[sg.Button('Enviar', bind_return_key=True)],
			[sg.Output(size=(50,10))]
		]
		#janela
		self.janela = sg.Window("DNS Resolver").layout(layout)
		

	def Iniciar(self):
		while True:
			#dados na tela
			self.button, self.value = self.janela.Read()
			url = self.value['url']
			if len(url) >= 2:
				host = url
				print(host, "---->", socket.gethostbyname(host))
			else:
				print("voce nao passou o argumento")
				print("metodo de uso:")
				print("python DNS_Resolver.py enderecoDoSite")

tela = TelaPython()
tela.Iniciar()
#if len(sys.argv) >= 2:
#	host = sys.argv[1]
#	print(host, "---->", socket.gethostbyname(host))
#else:
#    print("voce nao passou o argumento")
#    print("metodo de uso:")
#    print("python DNS_Resolver.py enderecoDoSite")