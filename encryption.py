from random import randint
try:
    from Freq_data import *
except:
    print('Freq_data.py not found brutforce key guessing based on probability will not work!')
def ceasarhack(msg):
   
    mini=201
    for j in range(95):
        s=msg
        s=cesar(s,'1',j)
        dif=0
        d={}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for i in range(len(d)):
            key = list(d.keys())[i]
            d[key]=(d[key]/len(msg))*100
        for key in freq:
            try:
                dif+=abs(freq[key]-d[key])
            except:
                dif+=freq[key]
        if dif<mini:
            mini=dif
            tot=j
    print('accuracy:',round(100-(mini/2)),'shift:',tot)
    if mini>=100:
        print("WARNING very low accuracy the result might be wrong")
    return tot


def cesar(msg,a1,sd):
    if a1=='2' and sd=='':
        sd=ceasarhack(msg)
    elif a1=='2':
        sd*=-1
    elif sd=='':
        sd=randint(1,94)
        print('Key:',sd)
    elif sd not in range(0,95):
        print('Key must be in range 1,94')
        raise Exception

    letts=[]
    for i in range(len(msg)):
        newlet=chr((ord(msg[i])-32+sd)%95+32)
        letts.append(newlet)
    word=''.join(letts)
    return word

def vernam_dec(msg,key):
    dec=''
    if len(key)!=len(msg):
        print('The length of the key must be equal to the length of the msg')
        raise Exception
    for i in range(len(msg)):
        dec+=chr(ord(msg[i])^ord(key[i]))
    return dec
def vernam_enc(msg):
    key=''
    enc=''
    for i in range(len(msg)):
        key+=chr(randint(0,127))
        enc+=chr(ord(msg[i])^ord(key[i]))
    return enc,key

def rail_enc(msg,key):
    if len(msg)>=3:
        if key=='':
            key=randint(2,len(msg)-1)
            print('key:',key)
        key=int(key)
        if key<2:
            raise Exception
        fc=[['' for i in range(len(msg))] for j in range(key)]
        ncnt=0
        d=False
        for i in range(len(msg)):
            if ncnt==key-1 or ncnt==0:
                d=not(d)
            for j in range(key):
                if j==ncnt:       
                    fc[j][i]=msg[i]
                else:
                    fc[j][i]=''
            if d:
                ncnt+=1
            else:
                ncnt-=1
        resl=''
        for el in fc:
            for ch in el:
                resl+=ch
        return resl
    else:
        print('Length error')
        raise Exception

def rail_dec(msg,key):
    key=int(key)
    fc=[['' for i in range(len(msg)+key)] for j in range(key)]
    spc=key+(key-2)
    cnt=0
    kof=0
    for i in range(key):
        for j in range(len(msg) + 2 * key):
            if j>=len(msg):
                if j%spc==i:
                    if j-kof>=0 and cnt<len(msg) and j-kof<len(msg):
                        fc[i][j-kof]=msg[cnt]
                        cnt+=1
            else:
                if (i==0 and j%spc==0)and(j<len(msg)) or (i==key-1 and j%spc==key-1):
                    if cnt>=len(msg):
                        break
                    fc[i][j]=msg[cnt]
                    cnt+=1
                elif j%spc==i:
                    if j-kof>=0 and j<len(msg):
                        fc[i][j-kof]=msg[cnt]
                        cnt+=1
                    if j<len(msg):
                        fc[i][j]=msg[cnt]
                        cnt+=1
                else:
                    fc[i][j]='.'
        kof+=2
    ncnt=0
    d=False
    dec=''
    for i in range(len(msg)):
        if ncnt==key-1 or ncnt==0:
            d=not(d)
        for j in range(key):
            if j==ncnt:       
                dec+=fc[j][i]
        if d:
            ncnt+=1
        else:
            ncnt-=1
    return dec
    
def rail_hac(msg):
    mini=201
    for j in range(2,len(msg)):
        s=msg
        s=rail_dec(s,j)
        dif=0
        d={}
        s=s.upper()
        ss=''
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z' or s[i] == ' ':
                ss+=s[i]
        word=''
        sss=[]
        for i in range(len(ss)):
            if ss[i]!=' ':
                word+=ss[i]
            else:
                sss.append(word)
                word=''
        sss.append(word)
        for e in range(len(sss)):
            cnt=0
            for i in range(len(sss[e])-2):
                slg=sss[e][i:i+3]
                if slg in d:
                    d[slg]+=1
                else:
                    d[slg]=1
        total = sum(max(len(word) - 2, 0) for word in sss)
        for i in range(len(d)):
            key = list(d.keys())[i]
            if total!=0:
                d[key]=(d[key]/total)*100
        for key in trfreq:
            try:
                dif+=abs(trfreq[key]-d[key])
            except:
                dif+=trfreq[key]
        if dif<mini:
            mini2=mini
            mini=dif
            tot=j
        elif dif<mini2:
            mini2=dif
    print('accuracy:',round(100-(mini/2)),'shift:',tot)
    print('Second best fit accuracy:',round(100-(mini2/2)))
    if mini>=150:
        print("WARNING very low accuracy the result might be wrong")
    return rail_dec(msg,tot)




def main():
    print('Welcome to enctyprion program by Andrei Egorkin AKA Kuprisel You need to have files input.txt with your msg in it and empty file output.txt\nYou must have one line of input text to be encrypted/decrypted and a second line of the key if you are decrypting Vernam, when encrypting vernam the key is always generated randomly and will be outputed as the second line in output.txt')

    
    if input('Do you have the files ready (y/n)?')!='y':
        print('Prepare the files and restart the programm')
        exit()
    
    print('Whould you like? to use (1)cesar shifer (2)vernam (3)Rail fence cipher')
    a=input()
    print('Whould you like? to (1)encrypt (2)decrypt')
    a1=input()
    f = open("input.txt", "r")
    msg = f.readline()
    if len(msg)<3:
        print('input length must be more than 3 symbols')
        raise Exception
    if a=='2' and a1=='2':
        key=f.readline()
    f.close()
    if a=='1':
        if a1=='2':
            sd=input('what is the key (or leave empty to let the programm to guess it)?')
        else:
            sd=input('what is the key (or leave empty to generate randomly)?')
        try:
            sd=int(sd)
        except:
            pass

        out=cesar(msg,a1,sd)  
    elif a=='2' and a1=='1':
        out,key=vernam_enc(msg) 
        
    elif a=='2' and a1=='2':
        print('Put an empty third line in input.txt to avoid some bugs with \\n')
        out=vernam_dec(key,msg) 

    elif a=='3'and a1=='1':
        key=input('what is the key (or leave empty to generate randomly)?')
        out= rail_enc(msg,key)
    elif a=='3'and a1=='2':
        sd=input('what is the key (or leave empty to let the programm to guess it)?')
        key=sd
        if sd=='':
            out=rail_hac(msg)
        else:
            key=int(key)
            out=rail_dec(msg,key)
    f = open("output.txt", "w")
    if a=='2' and a1=='1':
        f.write(f'{out}\n{key}')
    else:
        f.write(out)
    f.close()
 


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e).__name__, e)
    except:
        print('the exeption was raised, restart the programm')

