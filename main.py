import os, sys, time, datetime
from pyfiglet import Figlet
from traceroute import trct
from portscan import rhost
from BandWidthServerSide import bwss
from BandWidthClientSide import bwcs
from iperfS import SSideD
from iperfS import SSideC
from iperfS import CSideD
from iperfS import CSideC




#############################################
# TEMPLATE
#############################################
def template():
	f = Figlet(font='epic')
	g = Figlet(font='straight')
	os.system('clear')
	print f.renderText('Dam Script')
	print g.renderText('Coded by D4m3')
	print ('Automated Monitoring Tool')
	print ('')




#############################################
# SYTEM MONITOR
#############################################
def glanceMod():
	try:
		template()
		print("\n   --- Sytem Monitor ---")
		print('\n     Chose one option ')
		print("\n  [1] Start Local Monitoring\n  [2] Start WebServer Monitoring\n  [3] Back to Menu")
		inp = raw_input("\n  --->  ")
		
		if inp == '1':
			try:
				os.system('clear')
				template()
				print("Loading")
				time.sleep(1)
				os.system('clear')
				template()
				print("Loading.")
				time.sleep(1)
				os.system('clear')
				template()
				print("Loading..")
				time.sleep(1)
				os.system('clear')
				template()
				print("Loading...")
				os.system('glances')
				
			except KeyboardInterrupt:
				glanceMod()
				
		elif inp == '2':
			try:
				os.system('clear')
				template()
				print("Loading")
				time.sleep(1)
				os.system('clear')
				template()
				print("Loading.")
				time.sleep(1)
				os.system('clear')
				template()
				print("Loading..")
				time.sleep(1)
				os.system('clear')
				template()
				print("Loading...")
				os.system("clear")
				template()
				print("Initializing")
				print("")
				os.system('glances -w')
				
			except KeyboardInterrupt:
				glanceMod()
				
		elif inp == '3':
			main()
			
		else:
			print("  Invalid input..")
			time.sleep(2)
			glanceMod()	

	except KeyboardInterrupt:
		glanceMod()
	




#############################################
# NETWORK MON
#############################################
def iftop():
	try:
		template()
		print("\n   ---Network Monitor---")
		print("\n   Chose the interface ")
		print("\n  [1] Wlan0\n  [2] Eth0\n  [3] Back to Menu")
		inp = raw_input("\n  --->  ")
	
		if inp == '1':
			os.system('sudo iftop -i wlan0')

		elif inp == '2':
			os.system('sudo iftop -i eth0')
	
		elif inp == '3':
			main()
	
		else:
			print("  Invalid input..")
			time.sleep(2)
			iftop()
		main()

	except KeyboardInterrupt:
		iftop()




#############################################
# IPERF MODULES
#############################################
def iperfServer():
	try:
		template()
		print("\n  [1] Default Options\n  [2] Custom Options\n  [3] Go Back")
		inp = raw_input("\n  --->  ")
			
		if inp == '1':
			
			try:
				SSideD()
				
			except KeyboardInterrupt:
				print("\n  Press 'q' to exit")
				inp = raw_input("\n  --->  ")
				
				if inp == 'q':
					iperfMain()
			
				else:
					print("  Invalid input..")
					time.sleep(2)
					iperfMain()
				
		elif inp == '2':
			
			try:
				SSideC()
				
			except KeyboardInterrupt:
				print("\n  Press 'q' to exi")
				inp = raw_input("\n  --->  ")
				
				if inp == 'q':
					iperfMain()
					
			
				else:
					print("  Invalid input..")
					time.sleep(2)
					iperfMain()

		elif inp == '3':
			iperfMain()
			
		else:
			print("  Invalid input..")
			time.sleep(2)
			iperfServer()

	except KeyboardInterrupt:
		iperfServer()


def iperfClient():
	try:
		template()
		print("\n  [1] Default Options\n  [2] Custom Options\n  [3] Go Back")
		inp = raw_input("\n  --->  ")

		if inp == '1':

			try:
				CSideD()

			except KeyboardInterrupt:
				print("\n  Press 'q' to exi")
				inp = raw_input("\n  --->  ")
				
				if inp == 'q':
					iperfMain()


				else:
					print("  Invalid input..")
					time.sleep(2)
					iperfMain()

		elif inp == '2':

			try:
				CSideC()

			except KeyboardInterrupt:
				print("\n  Press 'q' to exi")
				inp = raw_input("\n  --->  ")
				
				if inp == 'q':
					iperfMain()


				else:
					print("  Invalid input..")
					time.sleep(2)
					iperfMain()

		elif inp == '3':
			iperfMain()
			
		else:
			print("  Invalid input..")
			time.sleep(2)
			iperfServer()

	except KeyboardInterrupt:
		iperfClient()



def iperfMain():
	try:
		template()
		print("\n   --- Iperf ---")
		print('\n     Chose one option ')
		print("\n  [1] Server Side\n  [2] Client Side\n  [3] Back to Menu")
		inp = raw_input("\n  --->  ")
		
		if inp == '1': #Server Side
			iperfServer()
		
		elif inp == '2': #Client Side
			iperfClient()

		elif inp == '3': 
			main()

		else:
			print("  Invalid input..")
			time.sleep(2)
			iperfMain()

	except KeyboardInterrupt:
		iperfMain()





#############################################
# TRACEROUTE MODULE
#############################################
def tracer():
	try:
		template()
		print("\n   --- Traceroute ---")
		print('\n     Chose one option ')
		print("\n  [1] Launch Traceroute\n  [2] Back to Menu")
		inp = raw_input("\n  --->  ")
		if inp == '1':
			template()
			print("\n   --- Traceroute ---")
			print("")
			trct()
			print("\nPress 'q' to go back to main menu...")
			inp2 = raw_input("\n  --->  ")
			
			if inp2 == 'q':
				main()

			else:
				print('  Invalid input..')
				time.sleep(2)
				tracer()
				
		elif inp == '2':
			main()
			
		else:
			print("  Invalid input..")
			time.sleep(2)
			tracer()

	except KeyboardInterrupt:
		tracer()





#############################################
# PORT SCANNER MODULE
#############################################
def PortScanner():
	try:
		template()
		print("\n   ---Port Scanner---")
		print("\n    Chose one options")
		print("\n  [1] Launch Port Scanner\n  [2] Back to Menu")
		inp = raw_input("\n  --->  ")
		
		if inp == '1':
			template()
			print("\n   ---Port Scanner---")
			rhost()
			print("\nPress 't' to lauch Scanner again, and 'q' to go back to main menu...")
			inp = raw_input("\n  --->  ")
			
			if inp == 'q':
				main()
				
			elif inp == 't':
				PortScanner()

			else:
				print("  Invalid input..")
				time.sleep(2)
				PortScanner()
				
		elif inp == '2':
			main()
			
		else:
			print("  Invalid input..")
			time.sleep(2)
			PortScanner()

	except KeyboardInterrupt:
		PortScanner()




#############################################
# BANDWIDTH TEST MODULE
#############################################
def bandwidth():
	try:
		template()
		print("\n   ---Bandwidth Test---")
		print("\n    Chose one options")
		print("\n  [1] Start Server Side\n  [2] Start Client Side\n  [3] Help\n  [4] Back to Menu")
		inp = raw_input("\n  --->  ")
		
		if inp == '1':
			template()
			print("\n   ---Bandwidth Test---")
			bwss()
			
		elif inp == '2':
			template()
			print("\n   ---Bandwidth Test---")
			bwcs()
			
		elif inp == '3':
			def bandwidthHelp():
				template()
				print("\n   ---Bandwidth Test---")
				print("\n In order for you test the Bandwidth") 
				print("you need to start the server side in a machine") 
				print("and the client side in a difrent machine!")
				print("\n If you want to download one of the scripts needed to run this test")
				print("use the comand 'wget https://raw.githubusercontent.com/D4m666/Dam-Script/main/BandWidthServerSide.py' for the server side")
				print("or 'wget https://raw.githubusercontent.com/D4m666/Dam-Script/main/BandWidthClientSide.py' for client side ")
				print("Press 'q' to go back to main menu...")
				inp = raw_input("\n  --->  ")
				if inp == 'q':
					bandwidth()
				
				else:
					print("  Invalid input..")
					time.sleep(2)
					bandwidthHelp()
			bandwidthHelp()
		
		elif inp == '4':
			main()
			
		else:
			print("  Invalid input..")
			time.sleep(2)
			bandwidth()
	except KeyboardInterrupt:
		bandwidth()





#############################################
# CREDITS
#############################################
def Credits():
	try:
		template()
		print("The creatr of Dam Script is not reponsible for any of your activities while using the script!")
		print("This Script is meant to help you monitor your machine and keep track of any problems it might have.")
		print("\n  Press 'q' to go back to main menu...")
		inp = raw_input("\n  --->  ")
		if inp == 'q':
			main()
		else:
			print("  Invalid input..")
			time.sleep(2)
			Credits()

	except KeyboardInterrupt:
		Credits()





#############################################
# MAIN
#############################################
def main():
	try:
		template()
		print("  Where do you wanna go")
		print("\n  [1] System Monitor\n  [2] Network Monitor\n  [3] PortScanner\n  [4] Traceroute\n  [5] Bandwidth Test\n  [6] Iperf Test\n  [7] Credits\n  [8] Quit")
		question = raw_input("\n  --->  ")

		if question == '1':
			glanceMod()
			
		elif question == '2':
			iftop()
			
		elif question == '3':
			PortScanner()

		elif question == '4':
			tracer()
		
		elif question == '5':
			bandwidth()
			
		elif question == '6':
			iperfMain()
			
		elif question == '7':
			Credits()
	        
		elif question == '8':
			print("  Closing..")
			time.sleep(2)
			sys.exit()
	        
		else:
			print("  Invalid input..")
			time.sleep(2)
			main()
	except KeyboardInterrupt:
		os.system('clear')
		quit()

main()