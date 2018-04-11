import argparse
import collections

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Lets get some info from the fq files")
    parser.add_argument("--file", help="Input file ")

    args = parser.parse_args()
    fq_list = []
    with open(args.file) as inFile:
        for line in inFile:
            if (line[0] == "@") and ("_" in line):
                end = line.find("-")
                fq_list.append(line[1:end])
    counter = collections.Counter(fq_list)
    for k,v in counter.items():
        print(k + " " + str(v))