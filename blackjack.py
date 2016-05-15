import random 
'''def dillerkards():
    diller.append(k[p])
    k.remove(k[p])
def playerkards():
    oc.append(k[p])
    k.remove(k[p])'''
    
def BJ():
    ockidiller=0
    player=[]
    diller=[]
    g=''
    a=0
    m=['hearts','diamonds','spades','clubs']
    c=[' ace',' king',' queen',' jack',' 10',' 9',' 8',' 7',' 6',' 5',' 4',' 3',' 2']
    k=[]
    ocki=0
    for i in m:
        for j in c:
            k.append(i+j)

    random.shuffle(k)
    
    for p in range (0,2):
        player.append(k[p])
        k.remove(k[p])
        if 'ace' in player[p]:
            l=raw_input('ace=11 or ace=1? 1/11')
            if l=='11':
               ocki+=11
            else:
                ocki+=1
        elif 'king' in player[p]:
            ocki+=10
        elif 'queen' in player[p]:
            ocki+=10
        elif 'jack' in player[p]:
            ocki+=10
        elif '10' in player[p]:
            ocki+=10
        elif '9' in player[p]:
            ocki+=9
        elif '8' in player[p]:
            ocki+=8
        elif '7' in player[p]:
            ocki+=7
        elif '6' in player[p]:
            ocki+=6
        elif '5' in player[p]:
            ocki+=5
        elif '4' in player[p]:
            ocki+=4
        elif '3' in player[p]:
            ocki+=3
        elif '2' in player[p]:
            ocki+=2
            
        print player
    print ocki

    
    for p in range (0,2):
        diller.append(k[p])
        k.remove(k[p])
        if 'ace' in diller[p]:
            ockidiller+=11         
        elif 'king' in diller[p]:
            ockidiller+=10            
        elif 'queen' in diller[p]:
            ockidiller+=10             
        elif 'jack' in diller[p]:
            ockidiller+=10             
        elif '10' in diller[p]:
            ockidiller+=10             
        elif '9' in diller[p]:
            ockidiller+=9             
        elif '8' in diller[p]:
            ockidiller+=8             
        elif '7' in diller[p]:
            ockidiller+=7
        elif '6'in diller[p]:
            ockidiller+=6
        elif '5' in diller[p]:
            ockidiller+=5
        elif '4' in diller[p]:
            ockidiller+=4
        elif '3' in diller[p]:
            ockidiller+=3
        elif '2' in diller[p]:
            ockidiller+=2
    
    '''print oc'''
    print  ('dillers kards --- '+ diller[0])
 
    g=raw_input('esho?')        
    if g=='yes':
        for p in range (2,len(k)):
            player.append(k[p-2])
            k.remove(k[p-2])
            print player
            
            if 'ace' in player[p]:
                l=raw_input('ace=11 or ace=1? 1/11:')
                if l=='11':
                    ocki+=11
                    print player[p]
                else:
                    ocki+=1
                    print player[p]
                 
            elif 'king' in player[p]:
                ocki+=10
                print player[p]
             
            elif 'queen' in player[p]:
                ocki+=10
                print player[p]
             
            elif 'jack' in player[p]:
                ocki+=10
                print player[p]
             
            elif '10' in player[p]:
                ocki+=10
                print player[p]
            elif '9' in player[p]:
                ocki+=9
                print player[p]
            elif '8' in player[p]:
                ocki+=8
                print player[p]
            elif '7' in player[p]:
                ocki+=7
                print player[p]
            elif '6' in player[p]:
                ocki+=6
                print player[p]
            elif '5' in player[p]:
                ocki+=5
                print player[p]
            elif '4' in player[p]:
                ocki+=4
                print player[p]
            elif '3' in player[p]:
                ocki+=3
                print player[p]
                
            
            elif '2' in player[p]:
                ocki+=2
                print player[p]
            print ocki
            if ocki>22 :
                print ocki
                ocki=0
                print 'too much'
                break
            g=raw_input('esho?')
            if g=='no':
                break
            elif g=='yes':
                continue
            '''diler '''
    print diller
    for p in range (2,len(k)):
            if ockidiller>=17 and ockidiller<22:
                print ('u dillera -- '+str(ockidiller)+' ockov')
                break
            elif ockidiller>21:
                print ('u dillera -- '+str(ockidiller)+' ockov i on proigral')
                ockidiller=0
                break
            diller.append(k[p-2])
            k.remove(k[p-2])
            print diller
            
            if 'ace' in diller[p]:
                l=raw_input('ace=11 or ace=1? 1/11:')
                if l=='11':
                    ockidiller+=11
                    print diller[p]
                else:
                    ockidiller+=1
                    print diller[p]
                 
            elif 'king' in diller[p]:
                ockidiller+=10
                print diller[p]
             
            elif 'queen' in diller[p]:
                ockidiller+=10
                print diller[p]
             
            elif 'jack' in diller[p]:
                ockidiller+=10
                print diller[p]

             
            elif '10' in diller[p]:
                ockidiller+=10
                print diller[p]
            elif '9' in diller[p]:
                ockidiller+=9
                print diller[p]
            elif '8' in diller[p]:
                ockidiller+=8
                print diller[p]
            elif '7' in diller[p]:
                ockidiller+=7
                print diller[p]
            elif '6' in diller[p]:
                ockidiller+=6
                print diller[p]
            elif '5' in diller[p]:
                ockidiller+=5
                print diller[p]
            elif '4' in diller[p]:
                ockidiller+=4
                print diller[p]
            elif '3' in diller[p]:
                ockidiller+=3
                print diller[p]
            elif '2' in diller[p]:
                ockidiller+=2
        

    if ockidiller>ocki:
        print "your stavka othodit casino"
    elif ockidiller==ocki:
        print"take your stavka"
    else:
        print"washa stavka 2x"
    popitkanomerpyat=raw_input('hotite/ne hotite sigrat eshyo?')
    if popitkanomerpyat=='hotite':
        BJ()
    else:
        print'ny i ladno'
     

        


    
        
        
        
        
    
   
    
        
