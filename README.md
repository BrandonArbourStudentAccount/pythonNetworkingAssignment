# File Hashing Module

This repostitory contains hashing.py, a file hashing script that takes an input file and creates a hash value. 

This hash value can be output to standard out, a file called hashes.txt, or both. 

It also has an option to compare the hash of a file to the hash saved previously in hashes.txt.

## Usage

Calculate hash of file at \<PATH> then output to standard out and save to hashes.txt
- python hashing.py -path \<PATH>

Calculate hash of file at \<PATH> then output to <file/std-out/both>
- python hasning.py -path \<PATH> -output <file/std-out/both>

Calculate hash of file at \<PATH> then compare to hash saved in hashes.text
- python hashing.py -path \<PATH> -compare <True/False>