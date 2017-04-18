#!/usr/bin/env python3
# coding: utf8
# PCL II, Übung 4, FS17
# Aufgabe 2
# Autor: Kasimir Bobst
# Matrikel-Nr.: 14 723 423

import sys
import urllib.request
import bz2
import certifi
import lxml.etree as ET


def gettitles(infile, testfile, trainfile, k):
    raise NotImplementedError


def main():
    test_file = open("out2.txt", "w", encoding="utf8")
    print("Downloading")
    test = urllib.request.urlopen(
        "https://dumps.wikimedia.org/dewiki/" +
        "latest/dewiki-latest-pages-articles.xml.bz2", cafile=certifi.where())
    print("Done")
    for element in ET.iterparse(bz2.open(test)):
        test_file.write("{}\n".format(element))
    print("Opened")
    test_file.close()
    sys.exit()


if __name__ == "__main__":
    main()
