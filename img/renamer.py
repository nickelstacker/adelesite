import os

def rename_files_in_directory(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Sort the files to maintain order
    files.sort()

    # Initialize a counter for renamed files
    img_counter = 1

    # Iterate over the files and rename them
    for filename in files:

        # Skip files that contain "background" in the name
        if "background" in filename or "renamer" in filename:
            continue

        # Construct the new file name
        new_name = f"img{img_counter}.jpeg"

        # Get the full paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_file, new_file)
        print("Renaming " + old_file + " to " + new_file)

        # Increment the counter
        img_counter += 1

    print(f"Renamed {img_counter - 1} files, skipped files with 'background' in their names.")

# Specify the directory
directory_path = "./"

# Call the function to rename files
rename_files_in_directory(directory_path)
