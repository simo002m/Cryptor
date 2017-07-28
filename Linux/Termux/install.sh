#Get the path of the script
script_path=$(dirname $(realpath $0))

#Copy the file to /data/data/com.termux/files/usr/bin
cp $script_path/../../cryptor.py /data/data/com.termux/files/usr/bin/cryptor
