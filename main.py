import skimming as sk
import sys


def main(argv=sys.argv):
	print("======================================")
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

	# Get top N keywords of a text
	topScript = sk.topKeywords(script, n)
	
	print("======================================")
	print("Top keyword script: "+topScript[0].word)
	print("======================================")
	print("Top "+str(n)+" Keywords")
	for kw in topScript:
		print(kw.word+', score: '+str(kw.score))

	#Get all keywords of a text
	allScriptKeyword = sk.getKeywords(script)

	allTransKw = []
	scoreTrans = []
	maxScoreScript = 0

	#get all keywords of a transcript array
	for idx, tr in enumerate(arrayTrans):
		allTransKw.append(sk.getKeywords(tr))
		tmpScore = 0
		for scrKw in allScriptKeyword:
			#get the max score possible
			maxScoreScript = maxScoreScript + scrKw.score
			for trKw in allTransKw[idx]:
				if scrKw.word == trKw.word:
					#get the score of each keyword-match
					tmpScore = tmpScore + (scrKw.score + trKw.score)/2
		scoreTrans.append(tmpScore)

	print("======================================")

	for idx, tr in enumerate(arrayTrans):
		print("Transcript "+ tr +" score: "+str(scoreTrans[idx]/maxScoreScript))		



if __name__ == "__main__":
    main()
