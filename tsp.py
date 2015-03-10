#!/usr/bin/python

import sys, os, getopt, math

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

def tsp(citiesMatrix):

  best = []
  best.append(sys.maxint)

  cities = citiesMatrix.keys()
  for city1 in cities:

    tmp = []
    tmp.append(0)

    for city2 in cities:
      if city1 != city2:
        tmp[0] = tmp[0] + citiesMatrix[city1][city2]
        tmp.append(city2)

    if tmp[0] < best[0]:
      best = tmp

  return best

def dist(a,b):
    # a and b are integer pairs (each representing a point in a 2D, integer grid)
    # Euclidean distance rounded to the nearest integer:
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    #return int(math.sqrt(dx*dx + dy*dy)+0.5) # equivalent to the next line
    return int(round(math.sqrt(dx*dx + dy*dy)))

def buildMatrix(cities):

  citiesMatrix = {}
  for city1 in cities:
    citiesMatrix[city1[0]] = {}

    for city2 in cities:
      if city1[0] == city2[0]:
        d = -1 # we'll interpret this as an "impossible" route
      else:
        d = dist((city1[1], city1[2]), (city2[1], city2[2]))

      citiesMatrix[city1[0]][city2[0]] = d

  return citiesMatrix

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

 
  cities = []
  inputFile = open(args[0])

  while 1:

    line = inputFile.readline()
    if not line:
      break

    (cityid, xcoord, ycoord) = line.rsplit()
    cities.append((int(cityid), int(xcoord), int(ycoord)))

  inputFile.close()

  citiesMatrix = buildMatrix(cities)

  results = tsp(citiesMatrix)
  outputFile = open(args[0] + ".tour", "w")

  for result in results:
    outputFile.write(str(result) + os.linesep)

  outputFile.close()

if __name__ == '__main__':
	main(sys.argv[1:])
