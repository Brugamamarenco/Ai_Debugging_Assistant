import subprocess

def grab_error_from_file(file_name):
    try:
        # Run the Python file and capture output
        result = subprocess.run(
            ["python3", file_name],
            capture_output=True,
            text=True
        )

        # If there is an error, return it
        if result.returncode != 0:
            return result.stderr

        # No error
        return None

    except Exception as e:
        return f"System error: {str(e)}"