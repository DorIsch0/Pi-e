from Chef import Chef
import sys

FILENAME="test.chef"
debug=False


if len(sys.argv)>1:
 if sys.argv[1]=="d":
  debug=True
 elif sys.argv[1]=="info":
  print("forbidden var names: all instructions, furthermore: contents, dry ingredients, the, for")
  exit()
 else:
  if len(sys.argv)>2:
   debug=True
  FILENAME=sys.argv[1]

try:
    f=open(FILENAME,"r")
    c=f.read()
    f.close()
except IOError as t:
    print(t)
    exit()

mainChef=Chef(c)
#print(mainChef.parse(debug))
mainChef.parse(debug)
