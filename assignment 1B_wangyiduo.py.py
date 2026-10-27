# Name: [Wang Yiduo]
# Assignment One task 2

print("Question Answering Bot")
print("Type exit to leave the process")
ask=1
while ask==1:
	question = input("Ask me something: ")
	if question == "hello":
	    print("Bot: Hello! Nice to meet you.")
	elif question == "python":
	    print("Bot: Python is a language.")
	elif question == "HKU":
	    print("Bot: HKU is a university in HK")
	elif question == "human":
	    print("Bot: human created me")		
	elif question == "jetson":
	    print("Bot: Jetson Nano is an AI computer.")
	elif question == "ai":
	    print("Bot: AI means Artificial Intelligence.")
	elif question == "robot":
	    print("Bot: I am a chat robot")	
	elif question == "name":
	    print("Bot: My name is Python Bot.")
	elif question =="exit":
	    print("exit now")
	    ask=0
	else:
	    print("Bot: Sorry, I don't understand.")
