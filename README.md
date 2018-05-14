# Delft3D FM post-processing

This very simple container was designed to show the potential of using post-processing containers for software like Delft3D FM.
The main file `postproc.py` will read a NetCDF datafile and print some of the datafile's basic characteristics.

## Usage
```
usage: postproc.py [-h] [--file FILE]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  input file location
```

## Usage with Nerd
`nerd job run --name dflowfm-postproc --input dflowfm-output:/input nerdalize/dflowfm-postproc`
