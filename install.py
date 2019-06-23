import platform
import subprocess

if __name__=='__main__':
	try:
		if platform.system()=='Windows':
			subprocess.call(['install.bat'])
		else:
			subprocess.call(['./install.sh'])
	except KeyboardInterrupt:exit(0)
	except:raise
