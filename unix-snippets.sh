### Check admin rights in dir
cd $(DIR)
ls -l .

### Check admin right in file
cd $(DIR)
ls -l $(FILE)

### Add to admin rights of file to make it executable
### More: https://askubuntu.com/questions/932713/what-is-the-difference-between-chmod-x-and-chmod-755
chmod +x $(FILE)

### Look for text in files
### Kudos: https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux
grep -rn $(DIRECTORY) -e '$(PATTERN)'
