import random
def singleplayer():
    global a,b,c,d,e,f,g,h,i
    def symbol(symbol_p1):
        while (symbol_p1!="X" or symbol_p1!="O"):
            if symbol_p1=="O":
                print(p1," has chosen 'O',therfore computer gets 'X' ")
                symbol_p2="X"
                return symbol_p1,symbol_p2
            elif symbol_p1=="X":
                print(p1," has chosen 'X',therfore computer gets 'O' ") 
                symbol_p2="O"
                return symbol_p1,symbol_p2
            elif symbol_p1!="X" and symbol_p1 != "O":
                symbol_p1=input("choose either X or O: ")
                continue 
    

    def grid():
        global a,b,c,d,e,f,g,h,i
        print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |
               ''')
    def avaliable(k):
        while (k=='1' and a!="1") or (k=='2' and b!="2") or (k=='3' and c!="3") or(k=='4' and d!="4") or (k=='5' and e!="5") or (k=='6' and f!="6") or (k=='7' and g!="7") or (k=='8' and h!="8") or (k=='9' and i!="9") or (k!='1' and k!='2' and k!='3' and k!='4' and k!='5' and k!='6' and k!='7' and k!='8' and k!='9'):
            while (k=='1' and a!="1") or (k=='2' and b!="2") or (k=='3' and c!="3") or(k=='4' and d!="4") or (k=='5' and e!="5") or (k=='6' and f!="6") or (k=='7' and g!="7") or (k=='8' and h!="8") or (k=='9' and i!="9"):  
                k=input(p1 + " this place is already taken choose another: ")
            while (k!='1' and k!='2' and k!='3' and k!='4' and k!='5' and k!='6' and k!='7' and k!='8' and k!='9'):   
                k=input(p1 + " enter a number between 1 and 9: ")
        return k
    def pos(k):
        k=int(k)
        global a,b,c,d,e,f,g,h,i        
        if k==1:
            a=symbol_p1  
        elif k==2:    
            b=symbol_p1    
        elif k==3:    
            c=symbol_p1
        elif k==4:   
            d=symbol_p1  
        elif k==5:    
             e=symbol_p1
        elif k==6:
            f=symbol_p1
        elif k==7:
            g=symbol_p1
        elif k==8:
            h=symbol_p1
        elif k==9:
            i=symbol_p1
    def func():
        global a,b,c,d,e,f,g,h,i
        if e=="5":
            e=symbol_p2
        elif g=="7":
            g=symbol_p2
        elif i=="9":
            i=symbol_p2
        elif a=="1":
            a=symbol_p2
        elif c=="3":
            c=symbol_p2
        elif d=="4":
            d=symbol_p2
        elif f=="6":
            f=symbol_p2
        elif b=="2":
            b=symbol_p2
        elif h=="8":
            h=symbol_p2
    def towin():
        global a,b,c,d,e,f,g,h,i
        if (a==b==symbol_p2) and c=="3":
            c=symbol_p2
        elif (a==c==symbol_p2) and b=="2":
            b=symbol_p2
        elif (b==c==symbol_p2) and a=="1":
            a=symbol_p2
        elif (d==e==symbol_p2) and f=="6":
            f=symbol_p2
        elif (d==f==symbol_p2) and e=="5":
            e=symbol_p2
        elif (e==f==symbol_p2) and d=="4":
            d=symbol_p2   
        elif (g==h==symbol_p2) and i=="9":
            i=symbol_p2
        elif (g==i==symbol_p2) and h=="8":
            h=symbol_p2    
        elif (i==h==symbol_p2) and g=="7":
            g=symbol_p2
        elif (a==d==symbol_p2) and g=="7":
            g=symbol_p2
        elif (a==g==symbol_p2) and d=="4":
            d=symbol_p2 
        elif (g==d==symbol_p2) and a=="1":
            a=symbol_p2 
        elif (b==e==symbol_p2) and h=="8":
            h=symbol_p2  
        elif (b==h==symbol_p2) and e=="5":
            e=symbol_p2  
        elif (h==e==symbol_p2) and b=="2":
            b=symbol_p2
        elif (c==f==symbol_p2) and i=="9":
            i=symbol_p2                
        elif (c==i==symbol_p2) and f=="6":
            f=symbol_p2      
        elif (c==f==symbol_p2) and c=="3":
            c=symbol_p2
        elif (a==e==symbol_p2)and i=="9":
            i=symbol_p2
        elif (a==i==symbol_p2)and e=="5":
            e=symbol_p2 
        elif (i==e==symbol_p2)and a=="1":
            a=symbol_p2       
        elif(c==e==symbol_p2)and g=="7":
            g=symbol_p2
        elif(c==g==symbol_p2)and e=="5":
            e=symbol_p2 
        elif(g==e==symbol_p2)and c=="3":
            c=symbol_p2
    def todraw():
        global a,b,c,d,e,f,g,h,i
        if (a==b==symbol_p1) and c=="3":
            c=symbol_p2
        elif (a==c==symbol_p1) and b=="2":
            b=symbol_p2
        elif (b==c==symbol_p1) and a=="1":
            a=symbol_p2
        elif (d==e==symbol_p1) and f=="6":
            f=symbol_p2
        elif (d==f==symbol_p1) and e=="5":
            e=symbol_p2
        elif (e==f==symbol_p1) and d=="4":
            d=symbol_p2   
        elif (g==h==symbol_p1) and i=="9":
            i=symbol_p2
        elif (g==i==symbol_p1) and h=="8":
            h=symbol_p2    
        elif (i==h==symbol_p1) and g=="7":
            g=symbol_p2
        elif (a==d==symbol_p1) and g=="7":
            g=symbol_p2
        elif (a==g==symbol_p1) and d=="4":
            d=symbol_p2 
        elif (g==d==symbol_p1) and a=="1":
            a=symbol_p2 
        elif (b==e==symbol_p1) and h=="8":
            h=symbol_p2  
        elif (b==h==symbol_p1) and e=="5":
            e=symbol_p2  
        elif (h==e==symbol_p1) and b=="2":
            b=symbol_p2
        elif (c==f==symbol_p1) and i=="9":
            i=symbol_p2                
        elif (c==i==symbol_p1) and f=="6":
            f=symbol_p2      
        elif (c==f==symbol_p1) and c=="3":
            c=symbol_p2
        elif (a==e==symbol_p1)and i=="9":
            i=symbol_p2
        elif (a==i==symbol_p1)and e=="5":
            e=symbol_p2 
        elif (i==e==symbol_p1)and a=="1":
            a=symbol_p2       
        elif(c==e==symbol_p1)and g=="7":
            g=symbol_p2
        elif(c==g==symbol_p1)and e=="5":
            e=symbol_p2 
        elif(g==e==symbol_p1)and c=="3":
            c=symbol_p2
    def computer_turn():
        if ((a==b==symbol_p2) and c=="3") or((a==c==symbol_p2) and b=="2") or((b==c==symbol_p2) and a=="1")or((d==e==symbol_p2) and f=='6')or((d==f==symbol_p2) and e=="5")or((e==f==symbol_p2) and d=="4")or((g==h==symbol_p2) and i=="9")or((g==i==symbol_p2) and h=="8")or((i==h==symbol_p2) and g=="7")or((a==d==symbol_p2) and g=="7")or((a==g==symbol_p2) and d=='4')or((g==d==symbol_p2) and a=='1')or((b==e==symbol_p2) and h=='8')or((b==h==symbol_p2) and e=='5')or((h==e==symbol_p2) and b=='2')or((c==f==symbol_p2) and i=='9')or((c==i==symbol_p2) and f=='6')or((i==f==symbol_p2) and c=='3')or((a==e==symbol_p2)and i=='9')or((a==i==symbol_p2)and e=='5')or((i==e==symbol_p2)and a=='9')or((c==e==symbol_p2)and g=='7')or((c==g==symbol_p2)and e=='7')or((g==e==symbol_p2)and c=='3'):
            towin()
        elif ((a==b==symbol_p1) and c=="3") or((a==c==symbol_p1) and b=="2") or((b==c==symbol_p1) and a=="1")or((d==e==symbol_p1) and f=='6')or((d==f==symbol_p1) and e=="5")or((e==f==symbol_p1) and d=="4")or((g==h==symbol_p1) and i=="9")or((g==i==symbol_p1) and h=="8")or((i==h==symbol_p1) and g=="7")or((a==d==symbol_p1) and g=="7")or((a==g==symbol_p1) and d=='4')or((g==d==symbol_p1) and a=='1')or((b==e==symbol_p1) and h=='8')or((b==h==symbol_p1) and e=='5')or((h==e==symbol_p1) and b=='2')or((c==f==symbol_p1) and i=="9")or((c==i==symbol_p1) and f=='6')or((i==f==symbol_p1) and c=='3')or((a==e==symbol_p1)and i=='9')or((a==i==symbol_p1)and e=='5')or((i==e==symbol_p1)and a=='9')or((c==e==symbol_p1)and g=='7')or((c==g==symbol_p1)and e=='7')or((g==e==symbol_p1)and c=='3'):
            todraw()
        else:
            func()
    x=0
    while x!=1:
        p1=input("Enter your name: ")
        a,b,c,d,e,f,g,h,i="1","2","3","4","5","6","7","8","9"
        print("Computer has toss the coin")
        toss=input(p1 + " choose Heads or Tails: ")
        toss=toss.capitalize()
        while toss!="Heads" and toss!="Tails":
            toss=input(p1 + " Enter  either Heads or Tails: ") 
            toss=toss.capitalize()
        r=random.randint(0,1)   
        if (r==0 and toss=="Heads") or (r==1 and toss=="Tails"):
            print(p1,"has won the toss")
            print("so",p1,",will have first turn")
            z=input(p1+" choose either X or O symbol: ")
            z=z.capitalize()
            symbol_p1,symbol_p2=symbol(z)
            print(symbol_p1,symbol_p2)
            count=0
            while count<10:
                grid()
                L=input(p1+" select your position : ")
                M=avaliable(L)
                N=pos(M)
                grid()
                if (a==b==c==symbol_p1)or(d==e==f==symbol_p1)or(g==h==i==symbol_p1)or(a==d==g==symbol_p1)or(b==e==h==symbol_p1)or(c==f==i==symbol_p1)or(a==e==i==symbol_p1)or(c==e==g==symbol_p1):
                    print('p1,has won the game')
                    break
                count=count+1
                if count==9:
                    print("The game is tied")
                    break
                print("Computer Turn")
                computer_turn()
                grid()
                if (a==b==c==symbol_p2)or(d==e==f==symbol_p2)or(g==h==i==symbol_p2)or(a==d==g==symbol_p2)or(b==e==h==symbol_p2)or(c==f==i==symbol_p2)or(a==e==i==symbol_p2)or(c==e==g==symbol_p2):
                    print("Computer has won the game")
                    break
                count=count+1 
        else:
            print("computer has won the toss")
            print("So computer will have first turn")    
            z=input(p1+" choose your symbol: ")
            z=z.capitalize()
            symbol_p1,symbol_p2=symbol(z)
            print(symbol_p1,symbol_p2)
            count=0
            while count<10:
                grid()
                print("Computer Turn")
                computer_turn()
                grid()
                if (a==b==c==symbol_p2)or(d==e==f==symbol_p2)or(g==h==i==symbol_p2)or(a==d==g==symbol_p2)or(b==e==h==symbol_p2)or(c==f==i==symbol_p2)or(a==e==i==symbol_p2)or(c==e==g==symbol_p2):
                    print("Computer has won the game")
                    break
                count=count+1
                if count==9:
                    print("The game is tied")
                    break
                L=input(p1+" select your position : ")
                M=avaliable(L)
                N=pos(M)
                grid()
                if (a==b==c==symbol_p1)or(d==e==f==symbol_p1)or(g==h==i==symbol_p1)or(a==d==g==symbol_p1)or(b==e==h==symbol_p1)or(c==f==i==symbol_p1)or(a==e==i==symbol_p1)or(c==e==g==symbol_p1):
                    print('p1,has won the game')
                    break
                count=count+1
        print("Do you want to play again")
        Z=(input("Press Y to play again,or any other key to enter menu(press enter after pressing button): "))
        Z=Z.capitalize()
        if Z=="Y":
            continue
        else:
            break

print("                                       Welcome to a game of tic tac toe")    
x=0
while x!=1:    
    menu = eval(input('''
Press 1 for multiplayer mode
Press 2 for singleplayer mode
PRESS 3 to exit the game

'''))        
    if menu == 1:
        print("                                       You have chosen multiplayer mode")
        again=0
        while again!="Y":
            p1=input("Enter the name of player 1: ") 
            p2=input ("Enter the name of player 2: ")
            toss=input(p1 + " choose heads or tails: ")
            while toss!="heads" and toss!="tails":
                toss=input(p1 + " Enter  either heads or tails: ")
            r=random.randint(0,1)
            if (r==1 and toss=="heads") or (r==0 and toss=="tails"):
                print(p1,"has won the toss")
            symbol_p1= input(p1 + " choose O or X: ")
            while (symbol_p1!="X" or symbol_p1!="O"):
                if symbol_p1=="O":
                    print(p1," has chosen 'O',therfore", p2," gets 'X' ")
                    symbol_p2="X"
                    break
                elif symbol_p1=="X":
                    print(p1," has chosen 'X',therfore", p2," gets 'O' ") 
                    symbol_p2="O"
                    break
                elif symbol_p1!="X" and symbol_p1 != "O":
                    symbol_p1=input("choose either X or O: ")                        
                    continue 
            count=0
            a,b,c,d,e,f,g,h,i="1","2","3","4","5","6","7","8","9"
            print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |
               ''')               
            count=0
            while count<9:
                k=input(p1 + " select your position: ")
                while (k=='1' and a!="1") or (k=='2' and b!="2") or (k=='3' and c!="3") or(k=='4' and d!="4") or (k=='5' and e!="5") or (k=='6' and f!="6") or (k=='7' and g!="7") or (k=='8' and h!="8") or (k=='9' and i!="9") or (k!='1' and k!='2' and k!='3' and k!='4' and k!='5' and k!='6' and k!='7' and k!='8' and k!='9'):
                    while (k=='1' and a!="1") or (k=='2' and b!="2") or (k=='3' and c!="3") or(k=='4' and d!="4") or (k=='5' and e!="5") or (k=='6' and f!="6") or (k=='7' and g!="7") or (k=='8' and h!="8") or (k=='9' and i!="9"):  
                        k=input(p1 + " this place is already taken choose another: ")
                    while (k!='1' and k!='2' and k!='3' and k!='4' and k!='5' and k!='6' and k!='7' and k!='8' and k!='9'):   
                        k=input(p1 + " enter a number between 1 and 9: ")
                k=int(k)        
                if k==1:
                    a=symbol_p1  
                elif k==2:    
                    b=symbol_p1    
                elif k==3:    
                    c=symbol_p1
                elif k==4:   
                     d=symbol_p1  
                elif k==5:    
                     e=symbol_p1
                elif k==6:
                    f=symbol_p1
                elif k==7:
                    g=symbol_p1
                elif k==8:
                    h=symbol_p1
                elif k==9:
                    i=symbol_p1
                count=count+1    
                if count>=5:
                    if (a==b==c==symbol_p1)or(d==e==f==symbol_p1)or(g==h==i==symbol_p1)or(a==d==g==symbol_p1)or(b==e==h==symbol_p1)or(c==f==i==symbol_p1)or(a==e==i==symbol_p1)or(c==e==g==symbol_p1):
                        print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |
                    ''')
                                          
                        print(p1," has won the match") 
                    
                        break
                if count==9:
                    print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |

                ''')                        
                    print("the game has been drawn")    
            
                    break
                print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |

                ''')
                l=(input(p2 +" enter your position: "))
                while (l=='1' and a!='1') or (l=='2' and b!='2') or (l=='3' and c!='3') or(l=='4' and d!='4') or (l=='5' and e!='5') or (l=='6' and f!='6') or (l=='7' and g!='7') or (l=='8' and h!='8') or (l=='9' and i!='9') or (l!='1' and l!='2' and l!='3' and l!='4' and l!='5' and l!='6' and l!='7' and l!='8' and l!='9'):
                    while (l=='1' and a!='1') or (l=='2' and b!='2') or (l=='3' and c!='3') or(l=='4' and d!='4') or (l=='5' and e!='5') or (l=='6' and f!='6') or (l=='7' and g!='7') or (l=='8' and h!='8') or (l=='9' and i!='9') :
                        l=input(p2 + " this place is already taken choose another: ")
                    while (l!='1' and l!='2' and l!='3' and l!='4' and l!='5' and l!='6' and l!='7' and l!='8' and l!='9'):
                        l=input(p2+ " enter a number between 1 and 9: ")
                l=int(l)        
                if l==1:
                    a=symbol_p2 
                elif l==2:    
                    b=symbol_p2
                elif l==3:    
                    c=symbol_p2
                elif l==4:   
                    d=symbol_p2
                elif l==5:    
                    e=symbol_p2   
                elif l==6:
                    f=symbol_p2
                elif l==7:
                    g=symbol_p2
                elif l==8:
                    h=symbol_p2
                elif l==9:
                        i=symbol_p2
                count=count+1
                if count >=5:
                    if (a==b==c==symbol_p2)or(d==e==f==symbol_p2)or(g==h==i==symbol_p2)or(a==d==g==symbol_p2)or(b==e==h==symbol_p2)or(c==f==i==symbol_p2)or(a==e==i==symbol_p2)or(c==e==g==symbol_p2):
                        print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |
                        ''')
                             
                        print(p2," has won the match")
                        break
                print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |

                ''')
            else:
                print(p2,"has won the toss")
                symbol_p2=input(p2 + " choose X or O: ")
                while (symbol_p2!="X" or symbol_p2!="O"):
                    if symbol_p2=="O":
                        print(p2," has chosen 'O',therfore", p1," gets 'X' ")
                        symbol_p1="X"
                        break
                    elif symbol_p2=="X":
                        print(p2," has chosen 'X',therfore", p1," gets 'O'")
                        symbol_p1="O"
                        break 
                    elif symbol_p2!="X" and symbol_p2 != "O":
                        symbol_p2=input("choose either X or O: ")  
                        continue 
                count=0
                a,b,c,d,e,f,g,h,i="1","2","3","4","5","6","7","8","9"
                print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |
            ''')
                
                while count<9:
                    l=(input(p2 +" enter your position: "))
                    while (l=='1' and a!='1') or (l=='2' and b!='2') or (l=='3' and c!='3') or(l=='4' and d!='4') or (l=='5' and e!='5') or (l=='6' and f!='6') or (l=='7' and g!='7') or (l=='8' and h!='8') or (l=='9' and i!='9') or (l!='1' and l!='2' and l!='3' and l!='4' and l!='5' and l!='6' and l!='7' and l!='8' and l!='9'):
                        while (l=='1' and a!='1') or (l=='2' and b!='2') or (l=='3' and c!='3') or(l=='4' and d!='4') or (l=='5' and e!='5') or (l=='6' and f!='6') or (l=='7' and g!='7') or (l=='8' and h!='8') or (l=='9' and i!='9') :
                            l=input(p2 + " this place is already taken choose another: ")
                    while (l!='1' and l!='2' and l!='3' and l!='4' and l!='5' and l!='6' and l!='7' and l!='8' and l!='9'):
                            l=input(p2+ " enter a number between 1 and 9: ")
                    l=int(l)        
                     
                    if l==1:
                        a=symbol_p2 
                    if l==2:    
                        b=symbol_p2
                    if l==3:    
                        c=symbol_p2
                    if l==4:   
                        d=symbol_p2
                    if l==5:    
                        e=symbol_p2   
                    if l==6:
                        f=symbol_p2
                    if l==7:
                        g=symbol_p2
                    if l==8:
                        h=symbol_p2
                    if l==9:
                        i=symbol_p2
                    count=count+1 
        
                    if count>=5:
                        if (a==b==c==symbol_p2)or(d==e==f==symbol_p2)or(g==h==i==symbol_p2)or(a==d==g==symbol_p2)or(b==e==h==symbol_p2)or(c==f==i==symbol_p2)or(a==e==i==symbol_p2)or(c==e==g==symbol_p2):
                            print('''
                        |           |
                  ''',a,'''   |    ''',b,'''    |    ''',c,'''
                ________|___________|_________                                
                        |           |      
                  ''',d,'''   |    ''',e,'''    |    ''',f,'''
                ________|___________|__________
                        |           |     
                  ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                        |           |

                    ''')               
                            print(p2," has won the match")
                            break
                    if count==9:
                        print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |

                ''')             
                        print("The game has been drawn")    
                        break
                                
                    print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |

                ''')
        
                    k=input(p1 + " select your position: ")
                    while (k=='1' and a!="1") or (k=='2' and b!="2") or (k=='3' and c!="3") or(k=='4' and d!="4") or (k=='5' and e!="5") or (k=='6' and f!="6") or (k=='7' and g!="7") or (k=='8' and h!="8") or (k=='9' and i!="9") or (k!='1' and k!='2' and k!='3' and k!='4' and k!='5' and k!='6' and k!='7' and k!='8' and k!='9'):
                        while (k=='1' and a!="1") or (k=='2' and b!="2") or (k=='3' and c!="3") or(k=='4' and d!="4") or (k=='5' and e!="5") or (k=='6' and f!="6") or (k=='7' and g!="7") or (k=='8' and h!="8") or (k=='9' and i!="9"):  
                            k=input(p1 + " this place is already taken choose another: ")
                        while (k!='1' and k!='2' and k!='3' and k!='4' and k!='5' and k!='6' and k!='7' and k!='8' and k!='9'):   
                            k=input(p1 + " enter a number between 1 and 9: ")

                    k=int(k)   
                    if k==1:
                        a=symbol_p1   
                    elif k==2:    
                        b=symbol_p1    
                    elif k==3:    
                        c=symbol_p1
                    elif k==4:   
                        d=symbol_p1  
                    elif k==5:    
                        e=symbol_p1
                    elif k==6:
                        f=symbol_p1
                    elif k==7:
                        g=symbol_p1
                    elif k==8:
                        h=symbol_p1
                    elif k==9:
                        i=symbol_p1
                    count=count+1   
           
                    if count>=5: 
                        if (a==b==c==symbol_p1)or(d==e==f==symbol_p1)or(g==h==i==symbol_p1)or(a==d==g==symbol_p1)or(b==e==h==symbol_p1)or(c==f==i==symbol_p1)or(a==e==i==symbol_p1)or(c==e==g==symbol_p1):
                            print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |

                ''')
                            print(p1," has won the match")  
                                
                            break         

                    print('''
                    |           |
              ''',a,'''   |    ''',b,'''    |    ''',c,'''
            ________|___________|_________                                
                    |           |      
              ''',d,'''   |    ''',e,'''    |    ''',f,'''
            ________|___________|__________
                    |           |     
              ''',g,'''   |    ''',h,'''    |    ''',i,'''   
                    |           |

                ''')
            p=str(input("Do you want to play again , enter 'Y' for yes , press any other key to enter menu(press enter after pressing button): "))
            p=p.capitalize()
            if p=="Y":
                continue
            else:
                break
        
    elif menu == 2:
        print("                                       You have chosen singleplayer mode")
        singleplayer()
    elif menu==3:
        print("                                          Thanks for playing the game")
        break
    else:
        print("Enter a Valid Choice")
        menu = eval(input('''
Press 1 for multiplayer game
Press 2 for singleplayer game
PRESS 3 to exit the game

        '''))       
