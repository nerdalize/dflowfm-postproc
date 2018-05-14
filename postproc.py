import argparse
from netCDF4 import Dataset

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', default='/data/westerscheldt_100_map.nc', help='input file location')
args = parser.parse_args()

# Read the NetCDF datafile
dataset = Dataset(args.file, "r")

# Print the amount of keys
keys = dataset.variables.keys()
print("- The file {} contains {} NetCDF variables.".format(args.file, len(keys)))

# Print the description of the first variable
print("- Description of variable {}:".format(keys[0]))
print("")
print(dataset.variables[keys[0]])

# Close
dataset.close()
