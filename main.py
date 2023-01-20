#!/usr/bin/env python3
import argparse
import os
import json
from parser import parse
from plot import draw_bar


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str)
    parser.add_argument('outdir', type=str, default=None, nargs='?')
    args = parser.parse_args()
    full_inpath = os.path.abspath(args.infile)
    full_outpath = os.path.abspath(args.outdir)

    names, tm_index, categories, gene_index = parse(full_inpath)
    for key in list(categories.keys()):
        new_key = key.replace('℃', '')
        categories[new_key] = categories[key]
        del categories[key]

    draw_bar(path=full_outpath, categories=categories)
    with open(f'{full_outpath}/names.json', 'w', encoding='utf-8') as file:
        json.dump(names, file)
    with open(f'{full_outpath}/tm_index.json', 'w', encoding='utf-8') as file:
        json.dump(tm_index, file)
    with open(f'{full_outpath}/gene_index.json', 'w', encoding='utf-8') as file:
        json.dump(gene_index, file)


if __name__ == '__main__':
    main()
