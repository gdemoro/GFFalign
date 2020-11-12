#!/usr/bin/env python3

import imp
import unittest

from os.path import expanduser, join

# use expanduser to locate its home dir and join bin and candy module paths
#candy_module_path =  join(expanduser("~"), "bin", "candy")
#print(candy_module_path)

# load the module without .py extension
gffalign = imp.load_source("gffalign")
print(gffalign)

#class CandyTestCase(unittest.TestCase):

 #   def testCandy(self):
 #       candyOutput = candy.candy()

  #      assert candyOutput == "candy"
