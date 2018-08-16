# Input xlsx and select specified rows and columns to export csv

use python and library pandas to restructure a messy xlsx,sheet 2 except row 1, drop row 3 which is a filter applied

read through all the rows (index) to find the column with the name specified.
use id as the non-duplicated column (Primary key) as a reference, if does not use non-repeated column, the duplicated value will only appear once.
loop through the rows to record all the data into the list under the column name.
use to_csv to generate out the csv file with no index (index=false)


if the file is large, please add encoding to the code.

  import sys
  reload(sys)
  sys.setdefaultencoding('utf8')
