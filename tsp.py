#!/usr/bin/python

import sys, os, getopt, math, time, copy
from Queue import PriorityQueue

def calcDist(pointA, pointB):
    dx = pointA.x - pointB.x
    dy = pointA.y - pointB.y
    return int(round(math.sqrt(dx*dx + dy*dy)))

class Point:

  distMatrix = {}

  def __init__(self, id, x, y):
    self.id = id
    self.x = x
    self.y = y

  def distanceTo(self, other):

    if self.id in Point.distMatrix and other.id in Point.distMatrix[self.id]:
      return Point.distMatrix[self.id][other.id]

    dx = self.x - other.x
    dy = self.y - other.y
    dist = int(round(math.sqrt(dx*dx + dy*dy)))

    if self.id not in Point.distMatrix:
      Point.distMatrix[self.id] = {}

    if other.id not in Point.distMatrix:
      Point.distMatrix[other.id] = {}

    Point.distMatrix[self.id][other.id] = dist
    Point.distMatrix[other.id][self.id] = dist

    return dist

  def __eq__(self, other):
    return self.id == other.id

  def __str__(self):
    return "(" + str(self.id) + ":" + str(self.x) + \
      "," + str(self.y) + ")"

class Path:

  def __init__(self, firstPoint):
    self.path = []
    self.path.append(firstPoint)
    self.pointsHash = {}
    self.pointsHash[firstPoint.id] = 1;
    self.dist = 0

  def distance(self):
    return self.dist + self.path[-1].distanceTo(self.path[0])

  def size(self):
    return len(self.path)

  def addPoint(self, point):
    self.dist = self.dist + self.path[-1].distanceTo(point)
    self.path.append(point)
    self.pointsHash[point.id] = 1

  def containsPoint(self, point):
    return point.id in self.pointsHash

  def copy(self):
    copiedPath = Path(self.path[0])
    copiedPath.path = self.path[:]
    copiedPath.dist = self.dist
    copiedPath.pointsHash = copy.deepcopy(self.pointsHash)
    return copiedPath

  def __cmp__(self, other):
    if other == None:
      return -1
    return self.distance() - other.distance()

  def __str__(self):
    s = str(self.path[0])
    for point in self.path[1:]:
      s = s + ">" + str(point)
    s = s + ">" + str(self.path[0])
    return s

class PathFinder:
  
  def __init__(self, pointsList):
    self.points = pointsList

  def findBestPath(self, seconds):

    #Handle some of the trivial cases
    if len(self.points) == 0:
      return None

    if len(self.points) == 1:
      return Path(self.points[0])

    if len(self.points) == 2:
      path = Path(self.points[0])
      path.addPoint(self.points[1])
      return path

    if len(self.points) == 3:
      path = Path(self.points[0])
      path.addPoint(self.points[1])
      path.addPoint(self.points[2])
      return path

    #Now it starts to get interesting
    bestPath = None

    priorityQ = PriorityQueue()
    for point in self.points:
      priorityQ.put(Path(point))

    start = time.clock()

    while not priorityQ.empty() and time.clock() - start <= seconds:

      tmpPath = priorityQ.get()

      if bestPath != None and bestPath <= tmpPath:
        pass

      else:

        if self.isComplete(tmpPath):
          if bestPath == None or bestPath > tmpPath:
            bestPath = tmpPath
        else:
          for point in self.points:
            if not tmpPath.containsPoint(point):
              tmpPath2 = tmpPath.copy()
              tmpPath2.addPoint(point)
              priorityQ.put(tmpPath2)
      
    return bestPath

  def isComplete(self, path):
    for point in self.points:
      if not path.containsPoint(point):
        return False
    return True

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
    opts, args = getopt.getopt(argv, "hm:", ["help", "minutes="])
  except getopt.GetoptError:
    printHelp()
    exit(2)

  minutes = 5

  for opt in opts:
    if opt[0] == "--help" or opt[0] == "-h":
      printHelp()
      exit(1)
    elif opt[0] == "--minutes" or opt[0] == "-m":
      minutes = int(opt[1])
    else:
      print "Invalid option: ", opt[0]
      printHel()
      exit(2)

  if len(args) < 1:
    printHelp()
    exit(1)

 
  points = []
  inputFile = open(args[0])

  while 1:

    line = inputFile.readline()
    if not line:
      break

    (pointid, xcoord, ycoord) = line.rsplit()
    points.append(Point(int(pointid), int(xcoord), int(ycoord)))

  inputFile.close()

  print "Starting run on", len(points), "data points..."
  startTime = time.clock()

  pathFinder = PathFinder(points)
  bestPath = pathFinder.findBestPath(minutes * 60)

  if bestPath == None:
    print "Couldn't find a good path in that time."

  print "Finished in ", (time.clock() - startTime)

  if bestPath != None:

    outputFile = open(args[0] + ".tour", "w")
    outputFile.write(str(bestPath.distance()) + os.linesep)

    for point in bestPath.path:
      outputFile.write(str(point.id) + os.linesep)

    outputFile.close()

if __name__ == '__main__':
	main(sys.argv[1:])
