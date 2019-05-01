#!/bin/bash

rm -f largefile.txt
for i in {1..1000}; do echo "a" >>largefile.txt ; done
for i in {1..16} ; do cat largefile.txt >>l2 ; done ; mv l2 largefile.txt
for i in {1..16} ; do cat largefile.txt >>l2 ; done ; mv l2 largefile.txt
for i in {1..16} ; do cat largefile.txt >>l2 ; done ; mv l2 largefile.txt
for i in {1..16} ; do cat largefile.txt >>l2 ; done ; mv l2 largefile.txt

ls -la largefile.txt 

