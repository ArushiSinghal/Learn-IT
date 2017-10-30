#!/usr/bin/python
import numpy
import csv
from csv import reader
from matplotlib import pyplot
import matplotlib.pylab as plt
import sys

#convert image into rgb matrix

image = sys.argv[1]
im = plt.imread(image)
print im
print im.shape
