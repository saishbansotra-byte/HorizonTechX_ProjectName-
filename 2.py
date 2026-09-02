print("Welcome to the chatbot! You can ask me questions like 'hello', 'what is your name?', 'how are you?', 'what can you do?', or say 'goodbye' to exit.")
q={1:"hello",2:"what is your name?",3:"how are you?",4:"what can you do?",5:"goodbye"}
print(q)

def function():
    while True:
        a=int(input("Enter your question (1-5): "))
        if a==5:
            print("Goodbye! Have a great day!")
        elif a==1:
            print("Hello! How can I help you?")
        elif a==2:
            print("I am a chatbot created to assist you.")
 
        elif a==3:
            print("I am just a program, but I'm functioning well!")
        elif a==4:
            print("I can answer your questions and provide information.")
        else:
            pass
   
        
print(function())
        