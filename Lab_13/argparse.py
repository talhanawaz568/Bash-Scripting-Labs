import argparse

parser = argparse.ArgumentParser(description='Example script to demonstrate command-line arguments')
parser.add_argument('name', type=str, help='Name of the user')
parser.add_argument('--age', type=int, help='Age of the user', required=False, default=25)

args = parser.parse_args()

print(f"Name: {args.name}")
print(f"Age: {args.age}")
