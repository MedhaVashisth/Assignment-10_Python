#!/usr/bin/env python
# coding: utf-8
1. While shutil. copy() will copy a single file, shutil. copytree() will copy an entire folder and every folder and file contained in it.

2. rename() method in Python is used to rename a file or directory. This method renames a source file/ directory to specified destination file/directory.

3. The send2trash functions will move a file or folder to the recycle bin, while shutil functions will permanently delete files and folders.

4. The zipfile.ZipFile() function is equivalent to the open() function; the first argument is the filename, and the second argument is the mode to open the ZIP file in (read, write, or append).

5. 
# In[1]:


import os, shutil

def selectiveCopy(folder, extensions, destFolder):
	folder = os.path.abspath(folder)
	destFolder = os.path.abspath(destFolder)
	print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			name, extension = os.path.splitext(filename)
			if extension in extensions:
				fileAbsPath = foldername + os.path.sep + filename
				print('Coping', fileAbsPath, 'to', destFolder)
				shutil.copy(fileAbsPath, destFolder)


# In[2]:


extensions = ['.php', '.py']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)


# In[ ]:




