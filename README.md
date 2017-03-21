# Keyword comparator - Diego Chavez
#Libs
Texblob - Release v0.12.0 <textblob.readthedocs.io>
Python 3

#Install dependencies
>$ pip3 install -U textblob
>$ python3 -m textblob.download_corpora

#Main test

Default use (script.txt transcript_1.txt transcript_2.txt transcript_3.txt 10)
>$ python3 main.py

Generic use
>$ python3 main.py <script.txt> [<transcript.txt>] <n>


# Lib skimming.py
Class Keyword to get word-score
>class Keyword: <word:string> <score:num>

getKeywords: get all keywords in a file
>getKeywords(<filename>) -> [Keyword]

topKeywords: get N top keywords in a file
>topKeywords(<filename>, <int>) -> [Keywords]

normalizeKeywords: normalize the score in array keyword
>normalizeKeywords([Keyword]) -> [Keyword]

skimming: update the keyword array with the noun of a new line
>skimming (<string>,<section>,[Keywords]) -> [keyword]

