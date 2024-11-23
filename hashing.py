import hashlib
import argparse

def getHash(path):
    try:
        inputFile=open(path,mode='rb')
        fileText=inputFile.read()
        inputFile.close()
        hash=hashlib.sha256(fileText).hexdigest()
        return(hash)
    except FileNotFoundError:
        print("The file \""+path+"\" does not exist")
        exit()
    except PermissionError:
        print("Permission denied to \""+path+"\"")
        exit()
    except:
        print("Something went wrong getHash")
        exit()

def writeHash(hash):
    try:
        outputFile=open('hashes.txt',mode='w')
        outputFile.write(hash)
        outputFile.close()
    except FileNotFoundError:
        print("The file \"hashes.txt\" does not exist")
        exit()
    except PermissionError:
        print("Permission denied to \"hashes.txt\"")
        exit()
    except:
        print("Something went wrong with writeHash")
        exit()  

def readHash():
    try:
        hashFile=open('hashes.txt',mode='r')
        fileText=hashFile.read()
        return(fileText)
    except FileNotFoundError:
        print("The file \"hashes.txt\" does not exist")
        exit()
    except PermissionError:
        print("Permission denied to \"hashes.txt\"")
        exit()
    except:
        print("Something went wrong with readHash")
        exit()

parser=argparse.ArgumentParser(
    description="Creates a hash value for a file specified by the -path arguement. The hash value is output to standard out and hashes.txt by default.",
    prefix_chars='-'
)

parser.add_argument('-path',
    type=str,
    required=True,
    help="Path of file to be hashed. This arguement is required"
)

parser.add_argument('-output',
    type=str,
    choices=['file','std-out','both'],
    default='both',
    help="Specify how to output the hash. Defaults to both."
)

parser.add_argument('-compare',
    type=bool,
    choices=[True,False],
    default=False,
    help="Compare file to saved hash. Defaults to False."
)

hashArgs=parser.parse_args()

hash=getHash(hashArgs.path)

if hashArgs.compare == True:
    savedHash=readHash()
    if hash == savedHash:
        print("Hash of "+hashArgs.path+" is the same as the saved hash.")
    else:
        print("Hash of "+hashArgs.path+" is different from the saved hash.")
elif hashArgs.output == 'std-out':
    print(hash)
elif hashArgs.output == 'file':
    writeHash(hash)
elif hashArgs.output == 'both':
    print(hash)
    writeHash(hash)