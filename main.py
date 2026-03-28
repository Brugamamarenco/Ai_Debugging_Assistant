import sys
import parser as pr
import analyzer as an

def main():
    # Check if a target file was provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <target_file>")
        return

    # Get the file from command-line arguments
    target_file = sys.argv[1]

    # Run the file and capture errors
    error_text = pr.grab_error_from_file(target_file)

    # Only call Gemini if there is an error
    if error_text:
        result = an.analyze_error(error_text)
    else:
        result = "No error to analyze"

    # Print program output
    print("\n---------Program Output------------")
    print(error_text if error_text else "No error")

    # Print analyzed result
    print("\n---------Analyzed Result-----------")
    print(result)

if __name__ == "__main__":
    main()