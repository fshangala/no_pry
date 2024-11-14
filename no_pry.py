import argparse
import no_pry_mod

parser=argparse.ArgumentParser(
  prog="no_pry",
  description="Encrypts login credentials",
)
parser.add_argument("-s","--server",required=True)
parser.add_argument("-u","--username",required=True)
parser.add_argument("-p","--password",required=True)
parser.add_argument("-t","--type",default="b64",choices=["b64"])

args=parser.parse_args()
if args.type == "b64":
  credentials=no_pry_mod.Credentials(server=args.server,username=args.username,password=args.password)
  crypt=no_pry_mod.B64()
  token=crypt.encrypt(credentials=credentials)
  print(token)