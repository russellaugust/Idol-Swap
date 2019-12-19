# maybe flag for video files only, and then another for everything
# check volume checks - have it hault if there's two volumes for LEFT and RIGHT

import os, errno, argparse, datetime

def dir_path(string):
	# Checks if the path is a directory or not, just to confirm its real.	
	if os.path.isdir(string):
		return string
	else:
		export = "This is not a directory!  " + string
		raise NotADirectoryError(export)


def list_of_files(folder="", ext=".mov"):
	# Gets a list of files from a given directory.
	files = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(folder):
		for file in f:
			if ext in file:
				files.append(os.path.join(r, file))
	return files


def current_media_path_exists(file_left="", folder_left="", folder_center=""):
	# This will check if the paths match for the copy. They need to share a sub-tree path

	relate_left = os.path.relpath(file_left, folder_left)
	file_center = os.path.join(folder_center, relate_left)
	if os.path.exists(file_center):
		return True, file_center
	else:
		logging(file_left)
		return False, file_center


def perform_file_swap(left="", center="", right=""):
	# create folders if they don't already exist
	# shift the new files into the current folder, then shift the current files out in the backup.
	# it also creates temporary files during the process while shifting.

	create_dir_path(center)
	create_dir_path(right)

	os.system("mv '{}' '{}.tmp'".format(left, center))
	os.system("mv '{}' '{}'".format(center, right))
	os.system("mv '{}.tmp' '{}'".format(center, center))


def create_dir_path(file):
	# creates a directory for a given file path if it doesn't already exist.

	if not os.path.exists(os.path.dirname(file)):
		try:
			os.makedirs(os.path.dirname(file))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise


def logging(missing_file=""):
	# Just for logging whatever.
	logging_file ="/Users/mankedit/Desktop/idol_swap_log.txt" 

	if os.path.exists(logging_file):
		file1 = open(logging_file,"a") #append mode
	else:
		file1 = open(logging_file,"w") #write mode
		file1.write("The following files do NOT exist in the current struture. \n\n")

	file1.write("{} \n".format(missing_file))
	file1.close()

def parse_arguments():
	# terminal level interface for CLI

	parser = argparse.ArgumentParser(prog='idol swap', description='Tool used for replacing dailies with rebakes and retranscodes. It will replace the current dailies with retranscodes. The replaced dailies are preserved in a backup folder.')
	parser.add_argument('-r', '--retranscodes', type=dir_path, help='path to the retranscoded dailies.')
	parser.add_argument('-c', '--current', type=dir_path, help='path to the dailies to be replaced.')
	parser.add_argument('-b', '--backup', type=dir_path, help='path to back-up location.')
	args = parser.parse_args()

	if args.retranscodes and args.current and args.backup:
		print ("Processing files. Cross your fingers...")

		folder_left		= args.retranscodes
		folder_center	= args.current
		folder_right	= args.backup

		folder_date		= datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

		for file in list_of_files(folder_left):
			path_exists, file_center = current_media_path_exists(file, folder_left, folder_center)

			if path_exists:
				file_right = os.path.join(folder_right, folder_date, os.path.relpath(file_center, folder_center))
				perform_file_swap (left=file, center=file_center, right=file_right)

		print ("The idols have been swapped, but they belong in a museum!")

	else:
		parser.print_help()


def main ():
	parse_arguments()

if __name__== "__main__":
	main()