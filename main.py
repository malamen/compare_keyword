import skimming as sk
import sys


def main(argv=sys.argv):
	print ("Use $ python3 main.py <script.txt> [array Transcript.txt] <n-top-words>")
	print ("Default script.txt transcript_1.txt transcript_2.txt transcript_1.txt 10")
	script = ""
	arrayTrans = []
	n = 10
	if len(argv) == 1 :
		script = "script.txt"
		arrayTrans = ["transcript_1.txt", "transcript_2.txt", "transcript_3.txt"]
	else:
		script = argv[1]
		for x in range(2,len(argv)-1):
			arrayTrans.append(argv[x])
		n = int(argv[len(argv)-1])	

	topScript = sk.topKeywords(script, n)
	
	print(len(topScript))
	print("======================================")
	print("Top keyword script: "+topScript[0].word)
	print("Top "+str(n)+" Keywords")
	for kw in topScript:
		print(kw.word)


if __name__ == "__main__":
    main()
'''
arrayKeyword  = sk.getKeywords("transcript_3.txt")

print(len(arrayKeyword))

maxnoun = ''
maxpoints = 0
for keyword in arrayKeyword:
	if keyword.score > maxpoints:
		maxpoints = keyword.score
		maxnoun = keyword.word

print(maxnoun)
print(maxpoints)
'''