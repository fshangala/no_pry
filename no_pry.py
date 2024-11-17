import argparse
from src.no_pry_fshangala import no_pry_mod
import os

parser=argparse.ArgumentParser(
  prog="no_pry",
  description="Encrypts login credentials",
)
parser.add_argument("-s","--server",default="localhost")
parser.add_argument("-u","--username",default="root")
parser.add_argument("-p","--password")
parser.add_argument("-t","--type",default="b64",choices=["b64"])
parser.add_argument("-d","--decrypt",action="store_true")
parser.add_argument("-c","--code")
parser.add_argument("-f","--file")

args=parser.parse_args()

if args.file:
  if os.path.exists(args.file):
    if not os.path.isfile(args.file):
      print("Provided path is not a file")
      exit()
  else:
    print("File provided does not exist!")
    exit()
    
if args.decrypt:
  if args.code:
    credentials=no_pry_mod.decrypt(args.code)
    print(credentials)
    exit()
  elif args.file:
    no_pry_mod.decryptFile(args.file)
  else:
    print("Either argument -c or --code or argument -f or --file must be provided.")
    exit()
else:
  if args.password:
    if args.type == "b64":
      crypt=no_pry_mod.B64()
      credentials=no_pry_mod.Credentials(server=args.server,username=args.username,password=args.password)
      token=crypt.encrypt(credentials=credentials)
      print(token)
      exit()
  elif args.file:
    no_pry_mod.encryptFile(args.file)
  else:
    print("Either argument -p or --password or argument -f or --file must be provided.")
    exit()