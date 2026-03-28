import subprocess

def grab_error_from_file(file_name):
    try:
	#run the code and grabs the output and grabs the text
        result = subprocess.run(["python3", file_name],capture_output=T	rue, text = True)
	
	#checks if file has an error
	if result.returncode != 0:
	    return result.stderr
	#if there is no error it would just return nothing
	return None

    #if it crashes it grabs that error through the exception
    except Exception as e:
	return f"System error: {stre(e)}"

	
