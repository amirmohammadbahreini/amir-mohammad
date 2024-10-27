import random
d = {
"s":'sang' ,
"k" : "kaghaz",
"gh" :'gheichi'
}
your_wonond = 0
AI_wound = 0

for i in range(5):
    lst = ["s","k","gh"]
    Ai_choice = random.choice(lst)
    print(d[Ai_choice])
    choice_ = input("Enter choice sang,kaghaz,gheichi(s,k,gh)(exit): ")
    if choice_ != "s" and choice_ != "k" and choice_ != "gh" and choice_ != "exit" :
        print("Please enter a (s,k,gh)(exit)")
        your_wonond -= 1
        print(f"AI wound = {AI_wound} | your wonond = {your_wonond}")
        continue
    elif choice_ == "s" or  choice_ == "k" or choice_ == "gh" :
        if (Ai_choice == 's' and choice_ == 'gh') or (Ai_choice == 'gh' and choice_ == 'k') or( Ai_choice == 'k' and choice_ == 's'):
            print(f"AI choice is {d[Ai_choice]} and you choose is {d[choice_]} >>> you last:(  )")
            AI_wound+=1
        elif Ai_choice == choice_ :
                    print(f"AI choice is {d[Ai_choice]} and you choose is {d[choice_]} >>> nobady wound")   
        elif ( choice_ == 's' and Ai_choice == 'gh') or (choice_ == 'gh' and  Ai_choice== 'k') or( choice_ == 'k' and  Ai_choice== 's'):
            print(f"AI choice is {d[Ai_choice]} and you choose is {d[choice_]} >>> you wound")
            your_wonond+=1

    print(f"AI wound = {AI_wound} | your wonond = {your_wonond}")
    print(20*"**")
if AI_wound> your_wonond:
    print("AI Wound and You lose")
elif AI_wound == your_wonond:
    print("nobody wound")
else:
    print("You Wound and AI lose")