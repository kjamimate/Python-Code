------------------------------------------------------------------------------
# Name:        Write  and read to text file.
# Purpose:     Learning Python. Playing with writing and reading to text a text file in c:\
#
# Author:      Kjamimate.
#
# Created:     29/05/2015
# Copyright:   (c) user 2015
# Licence:     <Open>
#-------------------------------------------------------------------------------

import os

def wee():
	infile=open("c:\\test.txt", "w")       #Opens the file
	infile.write("1")                      #Writes the desired contents to the file
	infile.close()                         #Closes the file
	return

def waa():
	infile=open("c:\\test.txt", "w")       #Opens the file
	infile.write("2")                      #Writes the desired contents to the file
	infile.close()                         #Closes the file
	return





def read():
	with open ("c:\\test.txt", "r") as myfile:     #Opens the file
		num = myfile.readline()                    #Read from the text file
		print num                                  #Display text file content
		myfile.close()                             #Closes the file


def main():
	cho = raw_input("Type a number, 1, or 2 to write and 3 to read") #Input from user
	if cho == "1":                                                   #Choices to call def's
	 wee()
	if cho == "2":
	 waa()
	if cho =="3":
	 read()                                                          # Calling the read def


if __name__ == "__main__":                        #Calling main
		main()