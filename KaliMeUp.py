#!/usr/bin/python
# Colores de consola
#W  = '\033[0m'  # white (normal)
#R  = '\033[31m' # red
#G  = '\033[32m' # green
#O  = '\033[33m' # orange
#B  = '\033[34m' # blue
#P  = '\033[35m' # purple
#C  = '\033[36m' # cyan
#GR = '\033[37m' # gray
import os
import sys, traceback, platform, time
import urllib2
from urlparse import urlparse
#No usable aun.
# if platform.linux_distribution() == ('Sana', '', ''): #Will Fix this soon.
#   main()
# else: 
# 	print 'Parece que no estas usando Kali Linux 2.0'
# 	print 'No podemos dejarte usar este programa'

#Pedimos ser ROOT
if os.getuid() != 0:
	print '\033[31m[!]\033[33m ERROR: \033[36m KaliMeUp \033[33m debe correr como\033[34m root\033[0m'
	print '\033[31m[!]\033[33m Inicia sesion como root \033[34m(sudo su)\033[0m o \033[34m sudo kalimeup \033[0mo \033[34msudo python kalimeup.py\033[0m'
	exit(1)
def main():
	try:
		def banner():
		#Limpiamos e imprimimos el banner
			os.system('clear');
			print '''\033[33m
##    ##    ###    ##       #### ##     ## ######## ##     ## ########  
##   ##    ## ##   ##        ##  ###   ### ##       ##     ## ##     ## 
##  ##    ##   ##  ##        ##  #### #### ##       ##     ## ##     ## 
#####    ##     ## ##        ##  ## ### ## ######   ##     ## ########  
##  ##   ######### ##        ##  ##     ## ##       ##     ## ##        
##   ##  ##     ## ##        ##  ##     ## ##       ##     ## ##        
##    ## ##     ## ######## #### ##     ## ########  #######  ##  
Instalador Automatico para Kali linux 2.0 Sana  

 \033[32m Autor: Jose Suarez | Github: https://github.com/Josexv1\033[0m'''
		def menu():
			while True:
				banner();
				print '''
1) Repositorios
2) Instalar herramientas Rolling
3) Instalar Hacking Apps
4) Instalar Backbox-Anonymous
5) Ayuda
99) Salir
			'''
				#Comenzamos con la primer opcion
				opcion0 = raw_input("Usar > ")
			
				while opcion0 == "1":
					banner();
					print '''
1) Agregar repositorios extras (Solo Kali 2.0)
2) Agregar repositorio de Firefox
3) Agregar repositorio de TOR
4) Actualizar tu kali linux
5) Editar contenido de sources.list

99) Atras

					'''
					repo = raw_input("Usar ?> ")
					#Comenzamos con las opciones del menu de repositorios
					if repo == "1":
						print '[!] PD: Solo agrega los repositorios si no usaste un Mirrior!!'
						xx = raw_input('Quieres continuar? Y/N')
						if xx == "Y" or "y":
								cmd1 = os.system("echo '#Repositorios extra de Kali.")
								cmd2 = os.system("echo 'deb http://http.kali.org/kali sana main non-free contrib\ndeb http://security.kali.org/kali-security sana/updates main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >> /etc/apt/sources.list")
								os.system('clear')
								print ("Los repositorios extras de Kali linux fueron instalados")
								time.sleep(2)
								menu()
						else:
							menu()
					elif repo == "2":
						print '[!] PD: Esto solamente instalara los repositorios de Firefox, para instalarlo ve a Herramientas!'
						xx = raw_input('Quieres continuar? Y/N\n')
						if xx == "Y" or "y":
								cmd1 = os.system("echo '\n#Repositorios extra Firefox.\n")
								cmd2 = os.system("echo '\ndeb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main' >> /etc/apt/sources.list")
								os.system('clear')
								print ("Los repositorios de Firefox fueron instalados")
								time.sleep(2)
								menu()
						else:
							menu()
					elif repo == "3":
							cmd1 = os.system("echo '#Repositorios extra Tor.")
							cmd2 = os.system("echo '\ndeb http://deb.torproject.org/torproject.org jessie main\ndeb-src http://deb.torproject.org/torproject.org jessie main' >> /etc/apt/sources.list")
							os.system('clear')
							print ("Los repositorios de TOR fueron instalados")
							time.sleep(2)
							menu()
					elif repo == "4":
						print 'Vamos a actualizar su sistema, se paciente.'
						time.sleep(3)
						cmd = os.system("apt-get update -m")
					elif repo == "5":
						os.system('vim /etc/apt/sources.list')
					elif repo == "99":
						menu()
					else:
						print ("Comando invalido")
						time.sleep(0.5)
					# Fin Opciones de repositorios!
				#Opcion 2 del menu principal	
				while opcion0 == "2":
					banner();
					print '''
### Las herramientas Rolling hacen de Kali Linux
### una version con Apps de uso diario

1) Instalar usuario NO root   8)  Instalar MAT
2) Instalar Flash Player      9)  Instalar GIMP
3) Instalar LibreOffice       10) Instalar Dropbox
4) Instalar FileZilla         11) Instalar Bleachbit
5) Instalar Chromium          12) Instalar Sublime3
6) Instalar Thunderbird       13) Instalar PgAdmin3
7) Instalar Amarok

99) Atras 

					'''
					herr = raw_input("Usar ?> ")
					if herr == "1":
						print 'No implementado aun :c'
						time.sleep(2)
						menu()
					elif herr == "2":
						print 'No quieres instalar Flash player. Creeme.'
						time.sleep(2)
					elif herr == "3":
						os.system('apt-get install libreoffice')
						time.sleep(2)
					elif herr == "4":
						os.system('apt-get install fillezilla')
						time.sleep(2)
					elif herr == "5":
						os.system('apt-get install chromium')
						time.sleep(2)
					elif herr == "6":
						os.system('apt-get install thunderbird-mozilla-build')
						time.sleep(2)
					elif herr == "7":
						os.system('apt-get install amarok')
						time.sleep(2)
					elif herr == "8":
						os.system('apt-get install MAT')
						time.sleep(2)
					elif herr == "9":
						os.system('apt-get install gimp')
						time.sleep(2)
					elif herr == "10":
						print '[-] BETA!'
						opc = raw_input('Arquitectura? 32/64 bits > ')
						if opc == "32":
							print 'Instalaremos Dropbox 32 bits se paciente.\n'
							time.sleep(2)
							os.system('cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86" | tar xzf -')
							os.system('~/.dropbox-dist/dropboxd')
						else:
							print 'Instalaremos Dropbox 64 bits se paciente.'
							time.sleep(2)
							os.system('cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -')
							os.system('~/.dropbox-dist/dropboxd')
						time.sleep(2)
					elif herr == "11":
						os.system('apt-get install bleachbit')
						time.sleep(2)
					elif herr == "12":
						print '[-] BETA!'
						opc = raw_input('Arquitectura? 32/64 bits > ')
						if opc == "32":
							print 'Instalaremos Sublime text 3 32 bits se paciente.\n'
							time.sleep(2)
							os.system('wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3083_i386.deb')
							os.system('dpkg -i sublime-text_build-3083_i386.deb')
						else:
							print 'Instalaremos Sublime text 3 64 bits se paciente.\n'
							time.sleep(2)
							os.system('wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3083_amd64.deb')
							os.system('dpkg -i sublime-text_build-3083_amd64.deb')
						time.sleep(2)
					elif herr == "13":
						os.system('sudo apt-get install pgadmin3')
						time.sleep(2)
					elif herr == "99":
						menu()
					else:
						print ("Comando invalido")
						time.sleep(0.3)
				while opcion0 == "3":
						banner();
						print '''
### Herramientas de Hacking extras
### Coleccion de herramientas necesarias

1) Instalar  8)  Instalar 
2) Instalar  9)  Instalar 
3) Instalar  10) Instalar 
4) Instalar  11) Instalar 
5) Instalar  12) Instalar 
6) Instalar  13) Instalar 
7) Instalar 

99) Atras 
						'''
						herr = raw_input("Usar ?> ")
						if herr == "1":
							print 'xd'
						elif herr == "2":
							print 'xd'
						elif herr == "99":
							menu()
						else:
							print ("Comando invalido")
							time.sleep(0.3)
				while opcion0 == "4":
						banner();
						print '''
Backbox-Anonymous enruta todo tu trafico por TOR.
Haciendo que cada conexion de cualquier programa use TOR para ocultar tu IP 
Y mejorar tu privacidad.

Puedes ver como instalarlo manualmente en 
https://github.com/Josexv1/Kali-Anonymous

1) Instalar Backbox-Anonymous
2) Probar conexion a Tor!
99) Atras 
						'''
						herr = raw_input("Usar ?> ")
						if herr == "1":
							os.system('git clone https://github.com/Josexv1/Kali-Anonymous.git')
							time.sleep(0.5)
							os.system('cp Kali-Anonymous/etc/default/backbox-anonymous /etc/default/')
							time.sleep(0.1)
							os.system('cp Kali-Anonymous/usr/bin/backbox-anonymous /usr/bin/')
							time.sleep(0.1)
							print 'Se ha instalado Backbox-Anonymous'
							print 'Vamos a iniciar TOR'
							time.sleep(0.5)
							os.system('service tor start')
							print 'Debemos esperar unos 5 segundos para que se abra la conexion correctamente'
							time.sleep(5)
							print 'Tor esta corriendo.'
							time.sleep(1)
							os.system('backbox-anonymous start')
							print 'Ahora todo tu trafico corre bajo TOR!'
							time.sleep(5)
						elif herr == "2":
							# Intento de probar conexion con TOR!
							try:
								print 'Vamos a probar tu conexion a Tor, si acabas de encender el demonio'
								print 'debes esperar unos 10 segundos a que se conecte bien la red Tor'
								time.sleep(5)
								print("\nEnviando una peticion a : https://check.torproject.org\n")
								resp_tor = urllib2.urlopen("https://check.torproject.org").read()
								tu_ip = resp_tor.split('<strong>')[1].split('</strong>')[0].strip()
								if not resp_tor or 'Congratulations' not in resp_tor:
								    print("Parece que Tor no se inicio bien.\n")
								    print("Tu IP parece ser: " + tu_ip + "\n")
								    time.sleep(3)
								else:
								    print("Felicitaciones! Ahora tu trafico pasa por Tor! :-)\n")
								    print("Tu IP parece ser: " + tu_ip + "\n")
								    time.sleep(3)
							except:
							    print("No pudomos llegar al sistema de pruebas!. Tienes Internet?\n")
							    time.sleep(3)
						elif herr == "99":
							menu()
						else:
							print ("Comando invalido")
							time.sleep(0.3)
				while opcion0 == "5":
						banner();
						print '''
Kali Me Up, es un software para instalar automaticamente muchas herramientas
Puedes instalar Firefox, Tor, Backbox-Anonymous y otras herramientas
Es Opensource y Puedes ver el codigo aqui:
https://github.com/Josexv1/KaliMeUp
Poco a poco se agregaran herramientas que no vienen incluidas en los repos
de Kali Linux oficiales, cuyo contenido esta en GitHub.

Puedes poner issues y/o Pull requests en el github.

99) Atras 
						'''
						opc2 = raw_input("Usar ?> ")
						if opc2 == "99":
							menu()
						else:
							print 'Comando invalido'
							time.sleep(0.3)
			menu()
		menu()	
	except KeyboardInterrupt:
	  os.system('clear')
	  print "Apagando el programa."
	except Exception:
	  traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()