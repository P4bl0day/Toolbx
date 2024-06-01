import os


def debian():
	options = input('''Hey, welcome. choose the magic number \n [1.cyber-sec], [2.developer],\n
 [3.cyber-sec(reverse-eng toolkit's)], [4.cyber-sec(social-eng toolkit's)]''')
	if options == '1':
		deb_eth_tool = ['nmap', 'nc', 'dirb', 'weevely', 'wireshark', 'sqlmap', 'sql', 'sqllite', 'crunch', 'aircrack-ng', 'wifite2', 'macchanger', 'bettercap',
		'proxychain4', 'dirbuster', 'beef-xss', 'hashcat', 'hash-identifier', 'dmitry', 'john', 'hidra', 'defcon', 'waffw0ff', 'medusa', 'nikto', 'recon-ng'
		, 'whatweb', 'theharvester', 'wfuzz', 'worldlists', 'tor', 'nano', 'vim', 'git', 'wget', 'curl', 'code']
		for i in deb_eth_tool:
			os.system("sudo apt-get update -y")
			os.system(f"sudo apt-get install {i} -y")		
		printf("\t\t\t you have finished your downlaod see you soon bye.\n")
		exit(0)
	elif options == '2':
		deb_dev_tool = ['nodejs', 'npm', 'php', 'sql', 'sqllite', 'python', 'python3', 'code', 'nano', 'vim', 'vi', 'git', 'curl', 'wget', 'notepad++', 'nc']
		for i in deb_dev_tool:
			os.system("sudo apt-get update -y")
			os.system(f"sudo apt-get install {i} -y")
		os.system("sudo apt-get install i686-w64-mingw32-g++ -y")
	elif options == '3':
		deb_rev_tools = ['jdktools', 'ghidra', 'virtualbox', 'vim', 'nano', 'edb-debugger', 'apktool', 'dex2jar', 'javasnoop', 'JD-GUI', 'OllyDbg', 'smali', 'Valgrind', 'yara']
		for i in deb_rev_tools:
			os.system("sudo apt-get update -y")
			os.system("sudo apt-get install {i} -y", i)
		os.system("sudo apt-get install i686-w64-mingw32-g++ -y")
		exit(0)
	elif options == '4':
		deb_soc_tools = ['git', 'wget', 'curl', 'king-phisher', 'code', ]
		for i in deb_soc_tools:
			os.system("sudo apt-get update")
			os.system("sudo apt-get install {i} -y")
		os.system("git clone https://github.com/KasRoudra/PyPhisher.git")
		os.system("git clone https://github.com/htr-tech/zphisher.git ")


def arch():
	options = input('''
\tone last step plase select you department?
\t1.pentester/ethical hacker
\t2.developer(web)
\t3.reverse Enginer
\t4.social Enginer
''')
	if options == '1':
		arch_eth_tool = ['nmap', 'nc', 'dirb', 'weevely', 'wireshark', 'sqlmap', 'sql', 'sqllite', 'crunch', 'aircrack-ng', 'wifite2', 'macchanger', 'bettercap',
		'proxychain4', 'dirbuster', 'beef-xss', 'hashcat', 'hash-identifier', 'dmitry', 'john', 'hidra', 'defcon', 'waffw0ff', 'medusa', 'nikto', 'recon-ng'
		, 'whatweb', 'theharvester', 'wfuzz', 'worldlists', 'tor', 'nano', 'vim', 'git', 'wget', 'curl', 'code']
		for i in arch_eth_tool:
			os.system("sudo pacman -Syu")
			os.system(f"sudo pacman -S {i} -y")
		print("\ndone!!")
	elif options == '2':
		arch_dev_tool = ['nodejs', 'npm', 'php', 'sql', 'sqllite', 'python', 'python3', 'code', 'nano', 'vim', 'vi', 'git', 'curl', 'wget', 'notepad++', 'nc']
		for i in arch_dev_tool:
			os.system("sudo pacman -Syu")
			os.system(f"sudo pacman -S {i} -y")
		print("\ndone!!")
	elif options == '3':
		arch_rev_tools = ['jdktools', 'ghidra', 'virtualbox', 'vim', 'nano', 'edb-debugger', 'apktool', 'dex2jar', 'javasnoop', 'JD-GUI', 'OllyDbg', 'smali', 'Valgrind', 'yara']
		for i  in arch_rev_tools:
			os.system("sudo pacman -Syu")
			os.system(f"sudo pacman -S {i} -y")
		print('\ndone!!')
	elif options == '4':
		arch_soc_tools = ['git', 'wget', 'curl', 'king-phisher', 'code', ]
		for i in arch_soc_tools:
			os.system("sudo pacman -Syu")
			os.system("sudo pacman -S 	{i} -y")
		os.system("git clone https://github.com/KasRoudra/PyPhisher.git")
		os.system("git clone https://github.com/htr-tech/zphisher.git ")


def redhat():
	options = input('''
one last step plase select you department?
\t1.pentester/ethical hacker
\t2.developer(web)
\t3.reverse Enginer
\t4.social Enginer
''')
	if options == '1':
		rh_eth_tool = ['nmap', 'nc', 'dirb', 'weevely', 'wireshark', 'sqlmap', 'sql', 'sqllite', 'crunch', 'aircrack-ng', 'wifite2', 'macchanger', 'bettercap',
		'proxychain4', 'dirbuster', 'beef-xss', 'hashcat', 'hash-identifier', 'dmitry', 'john', 'hidra', 'defcon', 'waffw0ff', 'medusa', 'nikto', 'recon-ng'
		, 'whatweb', 'theharvester', 'wfuzz', 'worldlists', 'tor', 'nano', 'vim', 'git', 'wget', 'curl', 'code']
		for i in rh_eth_tool:
			os.system("sudo yum update")
			os.system(f"sudo yum install {i} -y")
		print("\ndone!!")
	elif options == '2':
		rh_dev_tool = ['nodejs', 'npm', 'php', 'sql', 'sqllite', 'python', 'python3', 'code', 'nano', 'vim', 'vi', 'git', 'curl', 'wget', 'notepad++', 'nc']
		for i in rh_dev_tool:
			os.system("sudo yum update")
			os.system(f"sudo yum install {i} -y")
		print("\ndone!!")
	elif options == '3':
		rh_rev_tools = ['jdktools', 'ghidra', 'virtualbox', 'vim', 'nano', 'edb-debugger', 'apktool', 'dex2jar', 'javasnoop', 'JD-GUI', 'OllyDbg', 'smali', 'Valgrind', 'yara']
		for i  in rh_rev_tools:
			os.system("sudo yum update")
			os.system(f"sudo yum install {i} -y")
		print('\ndone!!')
	elif options == '4':
		rh_soc_tools = ['git', 'wget', 'curl', 'king-phisher', 'code', ]
		for i in rh_soc_tools:
			os.system("sudo yum update")
			os.system("sudo yum install {i} -y")
		os.system("git clone https://github.com/KasRoudra/PyPhisher.git")
		os.system("git clone https://github.com/htr-tech/zphisher.git ")




os_system = input('''what os are you using:
1,debian based os
2, arch based os 
3, redhat based os:
==>> ''')
try:
	if os_system == '1':
		debian()
	elif os_system == '2':
		arch()
	elif os_system == '3':
		redhat()
	else:
		print('unknown command')
except KeyboardInterrupt():
	exit_op = input('are you sure you want to exit, CTRL^c')
	print('existing from the tool box')
	exit()
	
		
