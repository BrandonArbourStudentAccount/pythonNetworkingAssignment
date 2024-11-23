import hashlib
import argparse

def getHash(path):
    try:
        inputFile=open(path,mode='r')
        fileText=inputFile.read().encode(encoding='UTF-8')
        hash=hashlib.sha256(fileText).hexdigest()
        return(hash)
    except FileNotFoundError:
        print("The file \""+path+"\" does not exist.")
        exit()
    except UnicodeDecodeError:
        print("The file \""+path+"\" can't be decoded.")
        exit()
    except:
        print("Something went wrong")
        exit()


def writeHash(hash):
    outputFile=open('hashes.txt',mode='w')
    outputFile.write(hash)
    outputFile.close()

def readHash():
    hashFile=open('hashes.txt',mode='r')
    fileText=hashFile.read()
    return(fileText)

parser=argparse.ArgumentParser(
    description="File hashing arguements.",
    prefix_chars='-'
)

parser.add_argument('-path',
    type=str,
    required=True,
    help="Path of file to be hashed."
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