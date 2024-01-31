# Program that determines a file's media type

# Prompts user input for file name
file_name = input("Please enter the name of the file: ")

# Convert entire str to lowercase and remove white space
file_name = file_name.lower().strip()

# Check suffix in file extension
if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")