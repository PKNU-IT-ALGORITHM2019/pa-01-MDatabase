def search(words,word,start,end):
		if start == end-1:
			if words[start] == word:
				return start
			elif words[end]==word:
				return end
			else:
				print("Not Found.")
				if start is 0:
					return -1
				return start
			
		temp_i=1
		middle=int((start+end)/2)
		if words[middle] == word:
			while words[middle-temp_i] == word:
				if middle-temp_i<0:
					break
				temp_i+=1
			return middle-temp_i+1
		else:
			if words[middle] < word:
				return search(words,word,middle,end)
			else:
				return search(words,word,start,middle)

on=1
while on==1:
	uinput=input()
	oper=uinput.split(" ")
	if oper[0]=="read":
		if oper[0] is oper[-1]:
			continue
		filename=oper[1]
		#단어를 입력할때 띄어쓰기가 있는 경우
		i=1
		while oper[i] is not oper[-1]:
			filename+=" "+oper[i+1]
			i+=1
		with open(filename,"r",encoding="utf-8") as data:
			dictionary_temp = data.readlines()
		dictsize=len(dictionary_temp)
		dictlist=[]	#뜻까지 포함된 사전
		wordlist=[]		#단어만 저장
		for i in range(dictsize):
			if dictionary_temp[i] is not "\n":
				dictlist.append(dictionary_temp[i])
		for i in range(len(dictlist)):
			wordlist.append(dictlist[i].split(" (")[0].lower())
		listlen=len(wordlist)

	elif oper[0]=="exit":
		on=0
	elif oper[0]=="size": #단어장의 길이 출력
		print(listlen)
	elif oper[0]=="find":
		if oper[0] is oper[-1]:
			continue
		findword=oper[1]
		#단어를 입력할때 띄어쓰기가 있는 경우
		i=1
		while oper[i] is not oper[-1]:
			findword+=" "+oper[i+1]
			i+=1
		resultindex=search(wordlist,findword.lower(),0,listlen)
		
		count=0
		Rindex_temp=resultindex
		while Rindex_temp <= listlen:
			if wordlist[Rindex_temp] == findword:
				Rindex_temp+=1
				count+=1
			else:
				break
		if count is 0:
			print(dictlist[resultindex].split(")")[0],")")
			print("- - -")
			print(dictlist[resultindex+1].split(")")[0],")\n")
		else:
			print("Found",count,"items")
			for i in range(count):
				print(dictlist[resultindex])
				resultindex+=1
		
		

