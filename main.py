import sys
import parser  as pr
import analyzer as an

def main():
	#checks if the correct amount of files were called and the targeted file 
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <target_file")
		return
	#grabs the targeted file 
	target_file =  sys.argv[1]
	
	
	#calling error parser to grab the error of the file 
	error_text = pr.grab_error_from_file(target_file)
	#calls analyze to analyze the error and find the root cause and simplify error
	result = an.analyze_error(error_text)
	
	#prints error it got if not no error was recieved it put no error recieved
	print("\n---------Program Output------------")
	print(error_text if  error_text else "No error")0
	
	#printing the analyzed result
	print("\n---------Analyzed Result-----------")
	print(result)
#checks if the file was actually called on the terminal and if it was it runs it 
if __name__ == "__main__":
	main()

