try:
    # Open the source file 'userdata.txt' in read mode
    with open('file_handling/userdata.txt', 'r') as red:
        # Read the content of the source file
        content = red.read()
        # Open the destination file 'backup.txt' in write+read mode
        with open('file_handling/backup.txt', "w+") as bkp:
            # Write the content of the source file into the backup file
            bkp.write(content)
            # Move the file pointer to the beginning of the backup file
            bkp.seek(0)
            # Read the content of the backup file
            backupcontent = bkp.read()
            # Print the content of the backup file to verify
            print(backupcontent)
except Exception as e:
    # Handle any exceptions that occur and print an error message
    print(f'Encountered a problem: {e}')