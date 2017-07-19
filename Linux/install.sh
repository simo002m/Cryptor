#Get the path of the script
script_path=$(dirname $(realpath $0))

#Copy the file to /usr/local/bin and change permissions to match the other files in that directory.

sudo cp $script_path/../cryptor.py /usr/local/bin/cryptor
sudo chown root:root /usr/local/bin/cryptor
sudo chmod a-rwx /usr/local/bin/cryptor
sudo chmod a+rx /usr/local/bin/cryptor
sudo chmod u+w /usr/local/bin/cryptor
