# file_organizer.py
import os
import random
import hashlib
import logging
import concurrent.futures

# Set up logging
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
handler = logging.FileHandler('file_organizer.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class FileOrganizer:
    def __init__(self):
        # self.folder_path = folder_path
        # self.extensions = self.find_extensions(self.folder_path) if extensions is None else extensions
        self.folder_path = None
        self.extensions = None

    def find_extensions(self, path):
        extensions = set()
        for dirPath, _, fileNames in os.walk(path):
            for file in fileNames:
                extension = os.path.splitext(file)[1][1:]  # Get extension and remove dot
                if extension:  # If there's an extension, add it to the set
                    extensions.add(extension.lower())
        return extensions

    def create_dirs(self):
        for ext in self.extensions:
            directory_path = os.path.join(self.folder_path, ext + "_org")
            if not os.path.exists(directory_path):
                os.mkdir(directory_path)

    def compare_files(self, file1_path, file2_path):
        # Open the files and hash them
        with open(file1_path, 'rb') as f:
            hash1 = hashlib.md5(f.read()).hexdigest()
        with open(file2_path, 'rb') as f:
            hash2 = hashlib.md5(f.read()).hexdigest()
        # Return whether the hashes are the same
        return hash1 == hash2

    def organize(self, extension):
        ext_folder = os.path.join(self.folder_path, extension + "_org")
        for dirPath, _, fileNames in os.walk(self.folder_path):
            for file in fileNames:
                if file.endswith(extension):
                    source_path = os.path.join(dirPath, file)
                    dest_path = os.path.join(ext_folder, file)
                    # If the file is in the downloads folder (not in a subfolder)
                    if dirPath == self.folder_path:
                        try:
                            # If file doesn't exist in the destination
                            if not os.path.exists(dest_path):
                                os.rename(source_path, dest_path)
                                logger.info(f'Moved file {file} to {dest_path}')
                            else:
                                # If file exists, compare and delete if duplicate
                                if self.compare_files(source_path, dest_path):
                                    os.remove(source_path)
                                    logger.info(f'Deleted duplicate file {file}')
                                else:
                                    while os.path.exists(dest_path):
                                        base, ext = os.path.splitext(file)
                                        file = f"{base}{random.randint(0,99999)}{ext}"
                                        dest_path = os.path.join(ext_folder, file)
                                    os.rename(source_path, dest_path)
                                    logger.info(f'Moved and renamed file {file} to {dest_path}')
                        except Exception as e:
                            logger.error(f'Error while trying to move file {file}: {str(e)}')

    def delete_empty_dirs(self):
        for dirPath, _, _ in os.walk(self.folder_path, topdown=False):
            try:
                os.rmdir(dirPath)
                logger.info(f"Deleted empty directory: {dirPath}")
            except OSError:
                pass

    def organize_folder(self, folder_path, extensions=None):
        self.folder_path = folder_path
        self.extensions = self.find_extensions(self.folder_path) if extensions is None else extensions
        self.create_dirs()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.organize, self.extensions)
        self.delete_empty_dirs()

