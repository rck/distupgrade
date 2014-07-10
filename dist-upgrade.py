#!/usr/bin/env python2

import argparse
import subprocess
import sys
import pydoc

parser = argparse.ArgumentParser(
    description="List dist-upgrades by repo and interactively confirm \
    that upgrades should by applied")
parser.add_argument("-u" ,"--update", action="store_true",
                    help="Execute apt-get update first")
parser.add_argument("-f", "--force", action="store_true",
                    help="Force dist-upgrade without printing upgrades")

args = parser.parse_args()

def distupgrade():
    ret = subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"])
    sys.exit(ret)

def askyesnolist(question):
    ans =  raw_input(question + "? [Y/n/l] ")
    ans = ans.upper()
    if ans == '': ans = 'Y'
    return ans

def genrepopkgdict():
    output = subprocess.check_output(["sudo", "apt-get", "dist-upgrade", "-s"])
    output = output.split('\n')

    upgrades = {}
    for line in output:
        line = line.strip()
        if len(line) > 0 and line.startswith("Inst"):
            repo = line.split('(')[1].split()[1]
            if not upgrades.has_key(repo): upgrades[repo] = []
            upgrades[repo].append(line)

    return upgrades

def listupgrades(upgrades, verbose=True):
    txt = ""
    lines = 0
    for repo in upgrades:
        if verbose:
            txt += repo + ":\n"; lines += 1
            for pkg in sorted(upgrades[repo]):
                txt += " " + pkg + '\n'; lines +=1

        else: print repo + ':', len(upgrades[repo])

    if verbose and txt != "":
        if lines > 25: pydoc.pager(txt)
        else: print txt


def main():
    if args.update:
        subprocess.call(["sudo", "apt-get", "update"])

    if args.force:
        distupgrade()

    upgrades = genrepopkgdict()
    if len(upgrades) > 0:
        listupgrades(upgrades, verbose = False)
        while True:
            ans = askyesnolist("Install upgrades")

            if ans == 'Y': distupgrade()
            elif ans == 'L': listupgrades(upgrades)
            else: break
    else: print "There are no upgrades"

    sys.exit(0)

if __name__ == "__main__":
    main()

















