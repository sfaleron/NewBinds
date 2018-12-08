#!/bin/sh

# defaults presume execution from the sphinx/
# directory under the repository root.

INPUT=${1:-.}
OUTPUT=${2:-output}

# restbuilder 0.2 (pip install sphinxcontrib-restbuilder)
# nests output directories (with warning)
rm -rf output

sphinx-build -b rst $INPUT $OUTPUT
