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
import random


def gettitles(infile, testfile, trainfile, k):
    """writes @param k random titles of @param infile into @param testfile
    and all the other titles into @param trainfile
    """
    print("Processing...")
    train_file = open(trainfile, "w", encoding="utf8")
    reservoir = []
    for count, node in enumerate(
        ET.iterparse(infile, tag="{http:" +
                     "//www.mediawiki.org/xml/export-0.10/}title")):

        title_element = node[1]

        if count < k:
            reservoir.append(title_element.text)
        else:
            m = random.randint(0, count)
            if m < k:
                # write the title that is thrown out of the reservoir into the
                # trainfile
                train_file.write("{}\n".format(reservoir[m]))
                # update the reservoir
                reservoir[m] = title_element.text
            else:
                # write the title into the trainfile
                train_file.write("{}\n".format(title_element.text))

        title_element.clear()

    test_file = open(testfile, "w", encoding="utf8")
    for title in reservoir:
        # write the titles contained in the reservoir into the testfile
        test_file.write("{}\n".format(title))

    test_file.close()
    train_file.close()
    print("Done.")


def main():
    print("Getting xml file...")
    file = urllib.request.urlopen(
        "https://dumps.wikimedia.org/dewiki/" +
        "latest/dewiki-latest-pages-articles.xml.bz2", cafile=certifi.where())
    print("Done.")
    gettitles(bz2.open(file), "testfile.txt", "trainfile.txt", 20)
    sys.exit()


if __name__ == "__main__":
    main()
