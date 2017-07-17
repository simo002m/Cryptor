#Copy the file to /usr/local/bin and change permissions to match the other files 
#in that directory.
sudo cp cryptor.py /usr/local/bin/cryptor
sudo chown root:root /usr/local/bin/cryptor
sudo chmod a-rwx /usr/local/bin/cryptor
sudo chmod a+rx /usr/local/bin/cryptor
sudo chmod u+w /usr/local/bin/cryptor
