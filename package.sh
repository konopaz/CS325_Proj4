#!/bin/bash
echo "packing up deliverables into zip file..."

rm -Rf Group24Project4.zip
rm -Rf Group24Project4

mkdir -p Group24Project4
cp README.md Group24Project4/
cp tsp.py Group24Project4/
cp UnionFind.py Group24Project4/
cp tsp_example_1.txt Group24Project4/
cp tsp_example_1.txt.tour Group24Project4/
cp tsp_example_2.txt Group24Project4/
cp tsp_example_2.txt.tour Group24Project4/

zip -r Group24Project4.zip Group24Project4

rm -Rf Group24Project4
