import argparse
# parse=argparse.ArgumentParser()
# parse.add_argument('integer',type=int,help='display an integer')
# args=parse.parse_args()
# print (args.integer)
parse= argparse.ArgumentParser()
parse.add_argument('--square',help="display a square of a given number",type=int)
parse.add_argument("--cubic",help="display a cubic of a given number",type=int)


args=parse.parse_args()
if args.square:

    print(args .square**2)

if args.cubic:
    print(args.cubic**3)
#action= "store_true"//"store_const"
# parse=argparse.ArgumentParser(description="calculate the electron velocity")
# parse.add_argument("integer",metavar="N",type=int,nargs="+",help="display a integer")
# parse.add_argument("--sum",dest="accumlate",action="store_const",const=sum,
#                    default=max,help="sum the integer")
# args=parse.parse_args()
#
#
# print(args.accumlate(args.integer))
