#!/usr/bin/python

import argparse
import pexpect
from commands import getoutput as cmd

parser = argparse.ArgumentParser(description="A wrapper to the openssl csr generation")
parser.add_argument("-name", help="key name", dest="name", default="certificate")
parser.add_argument("-country", help="Country Name", dest="country", default="BR")
parser.add_argument("-state", help="State or Province Name ", dest="state", default="Rio Grande do Sul")
parser.add_argument("-city", help="Locality name", dest="city", default="Porto Alegre")
parser.add_argument("-org", help="Organization name", dest="org", default="Viewbox Ltda")
parser.add_argument("-unit", help="Organizational unit name", dest="unit", default="Matrix")
parser.add_argument("-cname", help="Common Name", dest="cname", default="Cristiano W. Araujo")
parser.add_argument("-email", help="Email Address", dest="email", default="cristianowerneraraujo@gmail.com")
parser.add_argument("-challenge", help="A challenge password (extra)", dest="challenge", default="")
parser.add_argument("-opt_company", help="An optional company name", dest="opt_company", default="")
args = parser.parse_args()

print cmd("openssl genrsa -out " + args.name + ".key 2048")

child = pexpect.spawn("openssl req -new -sha256 -key " + args.name + ".key -out " + args.name + ".csr")
print "1"
#print child.expect("[AU]:")
child.sendline(args.country)
print child.expect("\]:")
child.sendline(args.state)
print child.expect("\]:")
child.sendline(args.city)
print child.expect("\]:")
child.sendline(args.org)
print child.expect("\]:")
child.sendline(args.unit)
print child.expect("\]:")
child.sendline(args.cname)
print child.expect("\]:")
child.sendline(args.email)
print child.expect("\]:")
child.sendline(args.cname)
print child.expect("\]:")
child.sendline(args.challenge)
print child.expect("\]:")
child.sendline(args.opt_company)
print child.read()