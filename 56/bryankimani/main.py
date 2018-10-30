"""Media Files Durations Printer

This script receives a directory name and retrieves all mp3 (or mp4 or m4a) files.
It then sums up the durations of each file and prints them in a nice table with a
total duration..

This tool accepts mp3, m4a and mp3 files in a given directory.

This script requires that `mutagen` be installed within the Python
environment you are running this script in.
"""
import os
import mutagen


def get_media_files():
    """Return mp3, m4a or mp4 in the given Directory."""
    while True:
        directory_path = input("Enter Directory Path without quotes - ")
        try:
            if not directory_path:
                continue
        except ValueError:
            print("Please enter an appropriate value/ Directory path!")
        else:
            directory_media_files = []
            # strip in directory_path.strip() removes any Space at the Start and end of the
            # directory path
            for root, dirs, files in os.walk(directory_path.strip()):
                for filename in files:
                    if filename.endswith((".mp4", ".m4a", ".mp3")):
                        directory_media_files.append(os.path.join(root, filename))
                # Break allows you to go to only access the files in first level
                # del dirs[:] - Does the same thing
                break
            return directory_media_files


def get_media_file_duration(filename):
    """Return media file duration in seconds using mutagen."""
    media_item = mutagen.File(filename)
    media_length = media_item.info.length
    return media_length


def media_files_duration_dict():
    """Return a dictionary of media files duration in seconds."""
    directory_items = get_media_files()
    # Create a list of media file names
    file_names = [os.path.basename(file_path) for file_path in directory_items]
    # Create a list of media file duration in seconds
    file_durations = [
        get_media_file_duration(file_path) for file_path in directory_items
    ]
    # associate the filename to its duration in a dictionary
    media_files_dict = dict(zip(file_names, file_durations))
    return media_files_dict


def display_files_total_duration():
    """Display the dictionary of media files info in a table and
    sum of all media files duration in seconds."""
    files_duration_dict = media_files_duration_dict()
    if not files_duration_dict:
        print(
            "No mp3,mp4 or m4a files in the folder. Check if also you "
            "entered a valid Directory path"
        )
    else:
        print("{:<105} {:<100}".format("File Name", "Duration in Seconds"))
        print(
            "----------------------------------------------------------------------------"
            "------------------------------------------------------"
        )
        for value in files_duration_dict.items():
            key, num = value
            print("{:<105} {:<100}".format(key, num))
            print(
                "-------------------------------------------------------------------------"
                "---------------------------------------------------------"
            )
        print(
            "{:<105} {:<100}".format(
                "Total Duration in Seconds", sum(files_duration_dict.values())
            )
        )


if __name__ == "__main__":
    display_files_total_duration()
