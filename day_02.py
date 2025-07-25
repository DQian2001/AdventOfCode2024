import numpy as np

def getInput():
   with open( "day_02_input.txt", "r" ) as f:
      return f.read()

def processInput( inputStr ):
   inputStrList = inputStr.strip().split( "\n" )
   return [ list( map( int, i.split() ) ) for i in inputStrList ]

def solvePart1( mtx ):
   diffs = map( np.diff, mtx )
   return sum(
         np.isin( i, [ 1, 2, 3 ] ).all() + np.isin( i, [ -1, -2, -3 ] ).all()
         for i in diffs
   )

def solvePart2( mtx ):
   return sum(
         any(
               np.isin( dif, [ 1, 2, 3 ] ).all() +
               np.isin( dif, [ -1, -2, -3 ] ).all() for dif in map(
                     np.diff,
                     # List comprehension to calculate "leave one out" per data list.
                     # This results in a list of lists, where each element is a list
                     # missing one value from the data list.
                     [ data[ : i ] + data[ i + 1 : ] for i in range( len( data ) ) ]
               )
         ) for data in mtx
   )

def main():
   inputStr = getInput()
   mtx = processInput( inputStr )
   ansPart1 = solvePart1( mtx )
   print( f"ansPart1: {ansPart1}" )

   # -------------------------------------------------

   ansPart2 = solvePart2( mtx )
   print( f"ansPart2: {ansPart2}" )

if __name__ == "__main__":
   main()
