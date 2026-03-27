import sys
print("Number of arguments:"), len(sys.argv)
print("Argument List:", str(sys.argv))

for i, arg in enumerate(sys.argv):
	print(f"Argument {i}: {arg}")
if len(sys.argv) == 1:
    print("No command-line arguments provided.")
