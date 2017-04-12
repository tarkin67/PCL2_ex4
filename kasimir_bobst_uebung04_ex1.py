#!/usr/bin/env python3
# coding: utf8
# PCL II, Übung 4, FS17
# Aufgabe 1
# Autor: Kasimir Bobst
# Matrikel-Nr.: 14 723 423

import lxml.etree as ET
import glob
import sys


def getfreqwords(indir, outfile):
    for filename in glob.iglob(indir +
                               "/SAC-Jahrbuch_[0-9][0-9][0-9][0-9]_mul.xml"):
        print(filename)


def main():
    getfreqwords("C:/Users/kingo/Desktop/Text+Berg_Release_152_v01/" +
                 "Text+Berg_Release_152_v01/Corpus_XML/SAC", "")
    sys.exit()


if __name__ == "__main__":
    main()
