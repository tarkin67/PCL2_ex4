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
        for node in ET.iterparse(filename, tag="s"):
            # print all sentences that have at least 6 tokens
            if(len(node[1]) >= 6):
                for element in node[1]:
                    print(element.text)

            node[1].clear()


def main():
    getfreqwords("C:/Users/kingo/Desktop/Text+Berg_Release_152_v01/" +
                 "Text+Berg_Release_152_v01/Corpus_XML/SAC", "")
    sys.exit()


if __name__ == "__main__":
    main()
