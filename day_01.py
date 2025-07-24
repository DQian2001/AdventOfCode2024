import numpy as np

def getInput():
   with open( "day_01_input.txt", "r" ) as f:
      return f.read()

def processInput( inputStr ):
   inputStrList = inputStr.strip().split( "\n" )
   inputStrListMtx = list( map( str.split, inputStrList ) )
   mtx = np.array( inputStrListMtx, dtype=int )
   leftList, rightList = mtx[ :, 0 ], mtx[ :, 1 ]
   leftList.sort()
   rightList.sort()
   return leftList, rightList

def solvePart1( leftList, rightList ):
   return sum( abs( leftList - rightList ) )

def solvePart2( leftList, rightList ):
   counts = np.array( [ ( rightList == v ).sum() for v in leftList ] )
   return sum( leftList * counts )

def main():
   inputStr = getInput()
   leftList, rightList = processInput( inputStr )
   ansPart1 = solvePart1( leftList, rightList )
   print( f"ansPart1: {ansPart1}" )

   # -------------------------------------------------

   ansPart2 = solvePart2( leftList, rightList )
   print( f"ansPart2: {ansPart2}" )

if __name__ == "__main__":
   main()
