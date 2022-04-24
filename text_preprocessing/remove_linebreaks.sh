#!/bin/bash

# Remove punctuation from INPUT.txt and saving to OUTPUT.txt
cat INPUT.txt | tr -d '[:punct:]' > OUTPUT.txt
