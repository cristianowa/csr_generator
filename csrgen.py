#!/usr/bin/python

import sys
import argparse
import pexpect
from commands import getoutput as cmd

parser = argparse.ArgumentParser(description="A wrapper to the openssl CSR() generation")
parser.add_argument("-name", help="key name", dest="name", default="certificate")
parser.add_argument("-country", help="Country Name", dest="country", default="BR")
parser.add_argument("-state", help="State or Province Name ", dest="state", default="Rio Grande do Sul")
parser.add_argument("-city", help="Locality name", dest="city", default="Porto Alegre")
parser.add_argument("-org", help="Organization name", dest="org", default="Viewbox Ltda")
parser.add_argument("-unit", help="Organizational unit name", dest="unit", default="Matrix")
parser.add_argument("-cname", help="Common Name", dest="cname", default="Cristiano W. Araujo")
parser.add_argument("-email", help="Email Address", dest="email", default="cristianowerneraraujo@gmail.com")
parser.add_argument("-challenge", help="A challenge password (extra)", dest="challenge", default="")
parser.add_argument("-opt_company", help="An optional company name (extra)", dest="opt_company", default="")
parser.add_argument("-verify", help="print out CSR information", dest="verify", action="store_true")

args = parser.parse_args()
for arg in dir(args):
    if arg[0] != "_":
        locals()[arg] = args.__getattribute__(arg)

def generate_csr():
    cmd("openssl genrsa -out " + args.name + ".key 2048")
    child = pexpect.spawn("openssl req -new -sha256 -key " + args.name + ".key -out " + args.name + ".csr")
    for arg in [country, state, city, org, unit, cname, email, challenge, opt_company]:
        child.sendline(arg)
        child.expect("\]:")

def verify_csr():
    print cmd("openssl req -in " + name + ".csr -noout -text")

generate_csr()
if verify:
    verify_csr()