print("----------------------------------------")
print("Rock ,Paper, Scissors Game Account Setup")
print("----------------------------------------")
while True:
    username=input("Pick a username:")
    password=input("Pick a password:")
    print("Your account has been setup")
    text_file=open("Rock Paper Scissor Game Username.txt","a")
    text_file.write("\n")
    text_file.write(username)
    text_file.write("\n")
    text_file.close()
    text_file=open("Rock Paper Scissor Game Passwords.txt","a")
    text_file.write("\n")
    text_file.write(password)
    text_file.write("\n")
    text_file.close()
    break