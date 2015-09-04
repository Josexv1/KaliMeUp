#!/usr/bin/python
import os
# Colores de consola
#W  = '\033[0m'  # white (normal)
#R  = '\033[31m' # red
#G  = '\033[32m' # green
#O  = '\033[33m' # orange
#B  = '\033[34m' # blue
#P  = '\033[35m' # purple
#C  = '\033[36m' # cyan
#GR = '\033[37m' # gray
import sys, traceback, platform
if platform.linux_distribution() == ('Sana', '', ''): #Will Fix this soon.
   main()
else: 
	print 'Parece que no estas usando Kali Linux 2.0'
	print 'No podemos dejarte usar este programa'
#Pedimos ser ROOT
if os.getuid() != 0:
	print '\033[31m[!]\033[33m ERROR: \033[36m KaliMeUp \033[33m debe correr como\033[34m root\033[0m'
	print '\033[31m[!]\033[33m Inicia sesion como root \033[34m(sudo su)\033[0m o \033[34m sudo kalimeup \033[0mo \033[34msudo python kalimeup.py\033[0m'
	exit(1)
def banner():
		#Limpiamos e imprimimos el banner
		os.system('clear');
		print '''
##    ##    ###    ##       #### ##     ## ######## ##     ## ########  
##   ##    ## ##   ##        ##  ###   ### ##       ##     ## ##     ## 
##  ##    ##   ##  ##        ##  #### #### ##       ##     ## ##     ## 
#####    ##     ## ##        ##  ## ### ## ######   ##     ## ########  
##  ##   ######### ##        ##  ##     ## ##       ##     ## ##        
##   ##  ##     ## ##        ##  ##     ## ##       ##     ## ##        
##    ## ##     ## ######## #### ##     ## ########  #######  ##  
Instalador Automatico para Kali linux 2.0 Sana  

 \033[1;32m Autor: Jose Suarez | Github: https://github.com/Josexv1\033[1;m'''

def main():
	try:
		def menu():
			while True:
				banner();
				print '''
1) Repositorios
2) Instalar herramientas
3) Instalar Backbox-Anonymous
5) Ayuda
99) Salir

			'''
				#Comenzamos con la primer opcion
				opcion0 = raw_input("\033[1;36mUsar > \033[1;m")
			
				while opcion0 == "1":
					banner();
					print '''
1) Agregar repositorios extras (Solo Kali 2.0)
2) Agregar repositorio de Firefox
3) Agregar repositorio de TOR
3) Actualizar tu kali linux
4) Ver el contenido de sources.list
99) Atras

					'''
					repo = raw_input("\033[1;32mUsar ?> \033[1;m")
					#Comenzamos con las opciones del menu de repositorios
					if repo == "1":
						print '\033[31m[!] PD: Solo agrega los repositorios si no usaste un Mirrior!!'
						xx = raw_input('Quieres continuar? Y/N')
						if xx == "Y" or "y":
								cmd1 = os.system("echo '#Repositorios extra de Kali.")
								cmd2 = os.system("echo 'deb http://http.kali.org/kali sana main non-free contrib\ndeb http://security.kali.org/kali-security sana/updates main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >> /etc/apt/sources.list")
						else:
							menu()
					elif repo == "2":
						print '\033[31m[!] PD: Esto solamente instalara los repositorios de Firefox, para instalarlo ve a Herramientas!'
						xx = raw_input('Quieres continuar? Y/N')
						if xx == "Y" or "y":
								cmd1 = os.system("echo '#Repositorios extra Firefox.")
								cmd2 = os.system("echo 'deb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main' >> /etc/apt/sources.list")
								op1 = raw_input('Los repositorios de Firefox fueron instalados. Quieres instalar Firefox ahora? Y/N')
								if op1 == "y" or"Y":
									cmd4 = os.system('apt-get update')
									cmd5 = os.system('apt-get remove iceweasel')
									cmd6 = os.system('apt-get install firefox-mozilla-build')
									cmd7 = os.system('apt-get update')
						else:
							menu()
					elif repo == "2":
						if xx == "Y" or "y":
							cmd1 = os.system("echo '#Repositorios extra Tor.")
							cmd2 = os.system("echo 'deb http://deb.torproject.org/torproject.org jessie main\ndeb-src http://deb.torproject.org/torproject.org jessie main' >> /etc/apt/sources.list")
					elif repo == "3":
						cmd3 = os.system("apt-get update -m")
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')
						print file.read()
					elif repo == "99":
						menu()
					else:
						print ("\033[1;31mComando invalido\033[1;m")
					# Fin Opciones de repositorios!
				#Opcion 2 del menu principal	
	except KeyboardInterrupt:
		os.system('clear')
		print "El usuario ha presionado CTRL+C, Apagando KaliMeUp"
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
