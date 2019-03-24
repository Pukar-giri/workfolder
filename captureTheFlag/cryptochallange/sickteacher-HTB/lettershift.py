#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string
import argparse
def bruteforce(filename):
    words=["the "," be "," to "," of "," and "," a "," in "," that "," have "," I "," it "," for "," not "," on "," with "," he "," as "," you "," do "," at "," this "," but "," his "," by "," from "," they "," we "," say "," her "," she "," or "," an "," will "," my "," one "," all "," would "," there "," their "," what "," so "," up "," out "," if "," about "," who "," get "," which "," go "," me "," when "," make "," can "," like "," time "," no "," just "," him "," know "," take "," people "," into "," year "," your "," good "," some "," could "," them "," see "," other "," than "," then "," now "," look "," only "," come "," its "," over "," think "," also "," back "," after "," use "," two "," how "," our "," work "," first "," well "," way "," even "," new "," want "," because "," any "," these "," give "," day "," most "," us"]
    with open(filename,"r") as infile:
        text=infile.read()
        text=text.lower()
    for n in range(26):
        result=""
        for letter in text:
            if letter in string.ascii_letters:
                resascii=(ord(letter)+n)%(ord("z")+1)
                if resascii<ord("a"):
                    resascii=resascii+ord("a")
                result=result+chr(resascii)
            else:
                result=result+letter
        print("="*30)
        print("offset used is = ",n,)
        print("="*30)
        print(result)
        print("="*30)
        print("\n")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("filename")
    args=parser.parse_args()
    bruteforce(args.filename)
