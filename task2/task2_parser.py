import argparse
from task2 import Rectangle


parser = argparse.ArgumentParser(description='Принимаем ширину и высоту')
parser.add_argument('-wdth', type=int)
parser.add_argument('-hght', type=int)
args = parser.parse_args()
print(args)
print(Rectangle(args.wdth, args.hght))
