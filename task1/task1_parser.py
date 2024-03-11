import argparse
from task1 import get_file_info


parser = argparse.ArgumentParser(description='Путь до директории')
parser.add_argument('-pth', type=str)
args = parser.parse_args()
print(args)
print(get_file_info(f'{args.pth}'))