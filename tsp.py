#!/usr/bin/python

import sys, os, getopt

def printHelp():
  print
  print os.path.basename(sys.argv[0]) + " input.txt",
  print
  print "Enter the name of program followed by the name of the input file."
  print
  print "Options"
  print "\t--help,-h\tprint this help message"
  print
  print "The input file must be in formatted as 3 integers per line separated "
  print "by a space. The first integer is the id of the city. The second and "
  print "third integers should be the coordinates of the city."
  print

def main(argv):

  try:
    opts, args = getopt.getopt(argv, "ha:", ["help", "algorithm="])
  except getopt.GetoptError:
    printHelp()
    exit(2)

  for opt in opts:
    if opt[0] == "--help" or opt[0] == "-h":
      printHelp()
      exit(1)
    else:
      print "Invalid option: ", opt[0]
      printHel()
      exit(2)

  if len(args) < 1:
    printHelp()
    exit(1)

 
  inputFile = open(args[0])

  #while 1:

    #coinline = inputFile.readline()
    if not coinline:
      break

if __name__ == '__main__':
	main(sys.argv[1:])
