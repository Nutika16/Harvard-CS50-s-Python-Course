import sys

from IntroductionToProgramming.LibrariesAndModules.CreatingLibrary.saying import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])