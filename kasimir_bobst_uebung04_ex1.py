#!/usr/bin/env python3
# coding: utf8
# PCL II, Übung 4, FS17
# Aufgabe 1
# Autor: Kasimir Bobst
# Matrikel-Nr.: 14 723 423

import lxml.etree as ET
import glob
import sys
import os


def getfreqwords(indir, outfile):
    output_file = open(outfile, 'w', encoding="utf8")
    tmp_file_name = "tmp.txt"
    temp_file = open(tmp_file_name, "w+", encoding="utf8")
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
                        sentence += str(element.get("lemma")) + " "
                sentence = sentence[:len(sentence) - 1]

                sentence_hash = hash(sentence)

                save_hash_sentence_pair_in_file(
                    sentence_hash, sentence, temp_file)

                if(sentence_hash in all_sentences):
                    all_sentences[sentence_hash] += 1
                else:
                    all_sentences[sentence_hash] = 1

            node[1].clear()

    temp_file.close()
    print("Getting {} most common sentences...".format(str(20)))
    for val in sorted(all_sentences.items(),
                      key=lambda x: x[1], reverse=True)[:20]:

        output_file.write("{}, {}\n".format(
            read_sentence_from_file_with_hash(val[0], tmp_file_name),
            str(val[1])))

    output_file.close()
    print("Deleting temporary file...")
    os.remove(tmp_file_name)
    print("Done.")


def save_hash_sentence_pair_in_file(hash_val, sentence, file):
    """writes a sentence - hash pair to a temporary file"""
    file.write("{}\t{}\n".format(str(hash_val), sentence))


def read_sentence_from_file_with_hash(hash_val, file):
    """reads a sentence from a temporary file with a key"""
    temp_file = open(file, "r")
    for line in temp_file:
        # print("looking for {} in {}".format(str(hash_val), line))
        if (line.startswith(str(hash_val))):
            # return the substring starting with a tab
            return line[line.find("\t") + 1:len(line) - 1]

    temp_file.close()


def main():
    getfreqwords("C:/Users/kingo/Desktop/Text+Berg_Release_152_v01/" +
                 "Text+Berg_Release_152_v01/Corpus_XML/SAC", "out.txt")
    sys.exit()


if __name__ == "__main__":
    main()
