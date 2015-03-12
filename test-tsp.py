#!/usr/bin/python

import unittest
import tsp

class TestTsp(unittest.TestCase):
  
  def test_Point_distanceTo(self):
    pointA = tsp.Point(1, 0, 0)
    pointB = tsp.Point(2, 3, 4)
    self.assertEqual(pointA.distanceTo(pointB), 5)

    pointA = tsp.Point(1, 3, 4)
    pointB = tsp.Point(2, 0, 0)
    self.assertEqual(pointA.distanceTo(pointB), 5)

    pointA = tsp.Point(1, 2, 3)
    pointB = tsp.Point(2, 5, 7)
    self.assertEqual(pointA.distanceTo(pointB), 5)

    pointA = tsp.Point(1, 7, 5)
    pointB = tsp.Point(2, 3, 2)
    self.assertEqual(pointA.distanceTo(pointB), 5)

  def test_Point_equals(self):
    pointA = tsp.Point(1, 2, 3)
    pointB = pointA
    self.assertTrue(pointA == pointB)

    pointB = tsp.Point(2, 3, 4)
    self.assertFalse(pointA == pointB)

    pointC = tsp.Point(2, 5, 6)
    self.assertTrue(pointB == pointC)

  def test_Path_containPoint(self):
    pointA = tsp.Point(1, 0, 0)
    pathA = tsp.Path(pointA)
    self.assertTrue(pathA.containsPoint(pointA))
    self.assertTrue(pathA.size() == 1)

    pointB = tsp.Point(2, 3, 4)
    pathA.addPoint(pointB)
    self.assertTrue(pathA.containsPoint(pointB))
    self.assertTrue(pathA.containsPoint(pointA))
    self.assertTrue(pathA.size() == 2)

    self.assertFalse(pathA.containsPoint(tsp.Point(3, 5, 7)))

  def test_Path_copy(self):
    pointA = tsp.Point(1, 0, 0)
    pathA = tsp.Path(pointA)
    pathB = pathA.copy()
    self.assertTrue(pathB.size() == 1)
    self.assertTrue(pathB.containsPoint(pointA))

    pointB = tsp.Point(2, 1, 1)
    pathA.addPoint(pointB)
    self.assertTrue(pathB.size() == 1)
    self.assertFalse(pathB.containsPoint(pointB))

    pointC = tsp.Point(3, 2, 2)
    pathB.addPoint(pointC)
    self.assertTrue(pathA.size() == 2)
    self.assertFalse(pathA.containsPoint(pointC))


  def test_Path_distance(self):
    pointA = tsp.Point(1, 0, 0)
    pathA = tsp.Path(pointA)
    self.assertTrue(pathA.distance() == 0)

    pointB = tsp.Point(2, 3, 4)
    pathA.addPoint(pointB)
    self.assertTrue(pathA.distance() == 10)

    pointC = tsp.Point(3, 7, 7)
    pathA.addPoint(pointC)
    self.assertTrue(pathA.distance() == 20)

  def test_Path_compare(self):
    pointA = tsp.Point(1, 0, 0)
    pointB = tsp.Point(2, 3, 4)
    pointC = tsp.Point(3, 6, 8)

    pathA = tsp.Path(pointA)
    pathB = tsp.Path(pointA)
    self.assertTrue(pathA == pathB)

    pathA.addPoint(pointB)
    self.assertTrue(pathA > pathB)

    pathB.addPoint(pointB)
    self.assertTrue(pathA == pathB)

    pathB.addPoint(pointC)
    self.assertTrue(pathA < pathB)

  def test_PathFinder_findBestPath_noPoints(self):
    pointA = tsp.Point(1, 0, 0)
    pathFinder = tsp.PathFinder([])
    self.assertTrue(pathFinder.findBestPath() == None)

  def test_PathFinder_findBestPath_singlePoint(self):
    pointA = tsp.Point(1, 0, 0)
    pathFinder = tsp.PathFinder([pointA])
    bestPath = pathFinder.findBestPath()
    self.assertTrue(bestPath.distance() == 0)
    self.assertTrue(bestPath.size() == 1)
    self.assertTrue(bestPath.containsPoint(pointA))

  def test_PathFinder_findBestPath_twoPoints(self):
    pointA = tsp.Point(1, 0, 0)
    pointB = tsp.Point(2, 3, 4)
    pathFinder = tsp.PathFinder([pointA, pointB])
    bestPath = pathFinder.findBestPath()
    self.assertTrue(bestPath.distance() == 10)
    self.assertTrue(bestPath.size() == 2)
    self.assertTrue(bestPath.containsPoint(pointA))
    self.assertTrue(bestPath.containsPoint(pointB))

  def test_PathFinder_findBestPath_twoPoints(self):
    pointA = tsp.Point(1, 0, 0)
    pointB = tsp.Point(2, 3, 4)
    pointC = tsp.Point(3, 6, 8)
    pathFinder = tsp.PathFinder([pointA, pointB, pointC])
    bestPath = pathFinder.findBestPath()
    self.assertTrue(bestPath.distance() == 20)
    self.assertTrue(bestPath.size() == 3)
    self.assertTrue(bestPath.containsPoint(pointA))
    self.assertTrue(bestPath.containsPoint(pointB))
    self.assertTrue(bestPath.containsPoint(pointC))

  #def test_PathFinder_findBestPath_fourPoints(self):
    #points = []
    #points.append(tsp.Point(1, 0, 0))
    #points.append(tsp.Point(2, 2, 0))
    #points.append(tsp.Point(3, 2, 2))
    #points.append(tsp.Point(4, 0, 2))
    #pathFinder = tsp.PathFinder(points)
    #bestPath = pathFinder.findBestPath()
    #self.assertTrue(bestPath.distance() == 8)
    #self.assertTrue(len(bestPath.path) == 4)
    #for point in points:
      #self.assertTrue(bestPath.contains(point))

if __name__ == '__main__':
  unittest.main()
