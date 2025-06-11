try:
    # Prompt the user to input a word to search for
    word = input("Input word: ")
    
    # Open the file 'userdata.txt' in read mode
    # The file path is relative to the current working directory
    with open("file_handling/userdata.txt", 'r') as f:
        # Read the entire content of the file
        content = f.read()
        
        # Check if the input word (case-insensitive) exists in the file content
        if word.lower() in content.lower():
            # If found, print a success message with the word and content
            print(f"found the word {word.lower()} in \"{content.lower()}\" ")
        else:
            # If not found, print a message indicating the word was not found
            print(f"Word {word} not found")

# Handle any exceptions that may occur during file operations or input
except Exception as e:
    # Print the error message
    print(f"problem {e} occured")