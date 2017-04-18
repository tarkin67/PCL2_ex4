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
    output_file = open(outfile, 'w', encoding="utf8")
    sentence_hashes = {}
    all_sentences = {}
    for filename in glob.iglob(indir +
                               "/SAC-Jahrbuch_[0-9][0-9][0-9][0-9]_mul.xml"):
        print(filename)
        for node in ET.iterparse(filename, tag="s"):
            # print all sentences that have at least 6 tokens
            if(len(node[1]) >= 6):
                sentence = ""
                for element in node[1]:
                    if(element.tag == "w"):
                        # print(str(element.get("lemma")))
                        sentence += str(element.get("lemma")) + " "
                sentence = sentence[:len(sentence) - 1]

                sentence_hash = hash(sentence)

                sentence_hashes[sentence_hash] = sentence

                if(sentence_hash in all_sentences):
                    all_sentences[sentence_hash] += 1
                else:
                    all_sentences[sentence_hash] = 1

            node[1].clear()

        counter = 0
        for val in sorted(all_sentences.items(),
                          key=lambda x: x[1], reverse=True)[:20]:
            print(sentence_hashes[val[0]] + ", " + str(val[1]))
            counter += 1

    output_file.close()


def main():
    getfreqwords("C:/Users/kingo/Desktop/Text+Berg_Release_152_v01/" +
                 "Text+Berg_Release_152_v01/Corpus_XML/SAC", "out.txt")
    sys.exit()


if __name__ == "__main__":
    main()
