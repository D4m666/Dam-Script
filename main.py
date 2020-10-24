import os, sys, time, datetime
from pyfiglet import Figlet
from traceroute import trct
from portscan import rhost
from BandWidthServerSide import bwss
from BandWidthClientSide import bwcs






def template():
	f = Figlet(font='epic')
	g = Figlet(font='straight')
	os.system('clear')
	print f.renderText('Dam Script')
	print g.renderText('Coded by D4m3')
	print ('Automated Monitoring Tool')
	print ('')
	

	
def iftop():
	template()
	print("\n   ---Network Monitor---")
	print("\n   Chose the interface ")
	print("\n  [1] Wlan0\n  [2] Eth0\n  [3] Back to Menu")
	inp = input("\n  --->  ")
	
	if inp == 1:
		os.system('iftop -i wlan0')

	if inp == 2:
		os.system('iftop -i eth0')
	
	if inp == 3:
		main()
	
	else:
		print("  Invalid input..")
		time.sleep(2)
		iftop()
	
	main()
	


		
def glanceMod():
	template()
	print("\n   --- Sytem Monitor ---")
	print('\n     Chose one option ')
	print("\n  [1] Start Local Monitoring\n  [2] Start WebServer Monitoring\n  [3] Back to Menu")
	inp = input("\n  --->  ")
	
	if inp == 1:
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
		
	if inp == 2:
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
		
	if inp == 3:
		main()
		
	else:
		print("  Invalid input..")
		time.sleep(2)
		glanceMod()	
	
	main()
	



def tracer():
	template()
	print("\n   ---Tracerouter---\n")
	trct()
	main()
	



def PortScanner():
	template()
	print("\n   ---Port Scanner---")
	rhost()



def bandwidth():
	template()
	print("\n   ---Bandwidth Test---")
	print("\n    Chose one options")
	print("\n  [1] Start Server Side\n  [2] Start Client Side\n  [3] Help\n  [4] Back to Menu")
	inp = input("\n  --->  ")
	
	if inp == 1:
		template()
		print("\n   ---Bandwidth Test---")
		bwss()
		
	if inp == 2:
		template()
		print("\n   ---Bandwidth Test---")
		bwcs()
		
	if inp == 3:
		template()
		print("\n   ---Bandwidth Test---")
		print("\n In order for you test the Bandwidth") 
		print("you need to start the server side in a machine") 
		print("and the client side in a difrent machine!")
		print("\n If you want to download one of the scripts needed to run this test")
		print("use the comand 'git clone https://github.com/D4m666/Python-Scripts/BandWitdthServerSide.py'")
		print("or 'git clone https://github.com/D4m666/Python-Scripts/BandWitdthClientSide.py' ")
		print("Press 'q' to go back to main menu...")
		inp = raw_input("\n  --->  ")
		if inp == 'q':
			bandwidth()
	
	if inp == 4:
		main()
		
	else:
		print("  Invalid input..")
		time.sleep(2)
		bandwidth()


		
		
def main():
	template()
	print("  Where do you wanna go")
	print("\n  [1] System Monitor\n  [2] Network Monitor\n  [3] PortScanner\n  [4] Traceroute\n  [5] Bandwidth Test\n  [6] Credits\n  [7] Quit")
    
	try:
		question = int(input("\n  --->  "))
        
	except Exception:
		print("Invalid input..")
		time.sleep(2)
		main()
        
	if question == 1:
		glanceMod()
		
	elif question == 2:
		iftop()
		
	elif question == 3:
		PortScanner()

	elif question == 4:
		tracer()
	
	elif question == 5:
		bandwidth()
	
	elif question == 6:
		os.system('clear')
		print("  Coded by D4m3  ")
		print("")
		print("The creatr of Dam Script is not reponsible for any of your activities while using the script!")
		print("This Script is meant to help you monitor your machine and keep track of any problems it might have.")
		print("  Press 'q' to go back to main menu...")
		inp = raw_input("\n  --->  ")
		if inp == 'q':
			main()
        
	elif question == 7:
		print("  Closing..")
		time.sleep(2)
		sys.exit()
        
	else:
		print("  Invalid input..")
		time.sleep(2)
		main()
        

main()
