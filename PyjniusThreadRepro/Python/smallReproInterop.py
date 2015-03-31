import sys, os
from jnius import autoclass

print 'CLASSPATH: ', os.environ['CLASSPATH']

Thing                 = autoclass('Thing')
