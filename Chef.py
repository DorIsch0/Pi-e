'''
Pi.

Ingredients.
1 g a
2 g t

Method.
Put a into mixing bowl.
Put t into 2nd mixing bowl.
Clean 2nd mixing bowl.
Remove t from mixing bowl.
Pour contents of the mixing bowl into the baking dish.
Serves 1.
'''

import random

class Chef:
    def __init__(self,c,ms={}):
        self.code=c.split("\n")
        self.title=""
        self.mbs=ms
        self.bds={}
        self.il={}
        #self.num1s=0

    def parse(self,debug,startIdx=0):
        for i in range(len(self.code)-1,-1,-1):
            if self.code[i].startswith("#") or self.code[i].startswith("Pre-heat") or self.code[i].startswith("Cooking time"):
                self.code.pop(i)

        ## remove title
        if len(self.code)-startIdx>2:
            self.title=self.code[0].replace(".","")
            #self.code.pop(0)
        else:
            return "Syntax Error: Code must have at least 5 lines."

        ## remove comment and "Ingredients."
        #while self.code[0].startswith("Ingredients.")==False:
        ingsIdx=-1
        for i in range(startIdx+1,len(self.code)):
            #self.code.pop(0)
            if self.code[i].startswith("Ingredients."):
                ingsIdx=i
                break
        #self.code.pop(0)
        if ingsIdx==-1:
            print("Error: No ingredient list found for recipe "+self.title+".")
            exit()

        ## remove ingredients while storing them
        #while self.code[0]!="":
        methodIdx=-1
        for i_ in range(ingsIdx+1,len(self.code)):
            i=self.code[i_]
            if i=="":
                methodIdx=i_+2
                break
            #i=self.code.pop(0).split(" ")
            i=i.split(" ")
            ing=[None,None,None]
            '''
            if len(i)>=2:
                ing[0]=int(i[0]) if int(i[0])==float(i[0]) else float(i[0])
                if i[1] in ("g","kg","pinch","pinches"):
                    ing[1]="dry"
                elif i[1] in ("l","ml","dash","dashes"):
                    ing[1]="liquid"
                elif len(i)==3:
                    ing[1]="dry"
            ing[2]=i[-1]
            '''
            #print(i)
            if len(i)>1:
                if i[0][0].isnumeric():
                    ing[0]=int(i[0]) if int(i[0])==float(i[0]) else float(i[0])
                    i=i[1:]
                if i[0] in ("heaped","level"):
                    ing[1]="dry"
                    i=i[1:]
                if i[0] in ("g","kg","pinch","pinches"):
                    ing[1]="dry"
                    i=i[1:]
                elif i[0] in ("l","ml","dash","dashes"):
                    ing[1]="liquid"
                    i=i[1:]
                elif i[0] in ("cup","cups","teaspoon","teaspoons","tablespoon","tablespoons"):    
                    i=i[1:]
            ing[2]=" ".join(i)
            #print(ing)
            self.il[ing[2]]=ing
        #self.code.pop(0) # empty line
        #self.code.pop(0) # "Method."

        ## get the method
        while self.code[methodIdx] in ("","Method."):
            methodIdx+=1
        excode=[]
        #while len(self.code)>0 and self.code[0]!="":
        for i in range(methodIdx,len(self.code)):
            if self.code[i]=="":
                break
            excode.append(self.code[i])
        #if len(self.code)>0:
        #    self.code.pop(0)

        return self.exec(excode,debug)

    def getMB(self,mbn):
        if not (mbn in self.mbs):
            self.mbs[mbn]=[]
        return self.mbs[mbn]

    def getBD(self,bdn):
        if not (bdn in self.bds):
            self.bds[bdn]=[]
        return self.bds[bdn]

    def getIngName(self,ln): # from beginning of line
        n=""
        #print(ln)
        while True:
            #print(ln)
            while ln[0]!=' ' and ln[0]!=".":
                n+=ln[0]
                ln=ln[1:]
            ln=ln[1:]
            #print(n,self.il)
            if n in self.il:
                break
            else:
                n+=" "
        #print(ln,n)
        return n,ln

    def getMBN(self,ln):
        #print(ln)
        if ln[0].isnumeric():
            mbns=""
            while ln[0].isnumeric():
                mbns+=ln[0]
                ln=ln[1:]
            ln=ln[3:]
            return int(mbns),ln
        return 1,ln

    def exec(self,code,debug):
        for i in range(len(code)):
            # for if we are in a loop:
            if i>=len(code):
                return

            #if code[i]=="Try the p.":
                #self.num1s+=(1 if self.il["p"][0]>0 else 0)

            #if code[i].startswith("#"):
            #    continue
            if debug:
            #if 1==1:
                #    #print(code,i)
                #    print("{}: {}, {}".format(code[i],self.mbs,self.bds))
                if input("{}: {}, {}".format(code[i],self.mbs,self.bds))=="y":
                    print(self.il)
            if code[i]=="":
                return
            if code[i].startswith("Put "):
                self.put(code[i])
            elif code[i].startswith("Add "):
                self.add(code[i])
            elif code[i].startswith("Remove "):
                self.remove(code[i])
            elif code[i].startswith("Combine "):
                self.combine(code[i])
            elif code[i].startswith("Divide "):
                self.divide(code[i])
            elif code[i].startswith("Pour "):
                self.pour(code[i])
            elif code[i].startswith("Serves "):
                print(self.serves(code[i])+(("\n{}, {}".format(self.mbs,self.bds) if debug else "")))
                #print(self.num1s)
                exit()
                # not just return, to prevent just going one level up from auxiliary cook
            elif code[i].startswith("Refrigerate"):
                p=self.refrigerate(code[i])+(("\n{}, {}".format(self.mbs,self.bds) if debug else ""))
                if len(p)>0:
                #if 1==1:
                    print(p)
                return 0x20
            elif code[i].startswith("Take "):
                self.take(code[i])
            elif code[i].startswith("Fold "):
                self.fold(code[i])
            elif code[i].startswith("Liquefy ") or code[i].startswith("Liquify "):
                self.liquefy(code[i])
            elif code[i].startswith("Stir "):
                self.stir(code[i])
            elif code[i].startswith("Mix "):
                self.mix(code[i])
            elif code[i].startswith("Clean "):
                self.clean(code[i])
            elif code[i]=="Set aside.":
                return 0x10
            elif code[i].startswith("Serve "):
                self.servewith(code[i])
            else:
                if self.loop(code,i,debug)==0x20:
                    return 0x20

        if debug:
            return "{}, {}".format(self.mbs,self.bds)

    def put(self,ln):
        ln=ln[4:]
        #print(ln)
        n,ln=self.getIngName(ln)
        ing=self.il[n]
        mbn=1
        if len(ln)>4:
            ln=ln[5:]
            mbn=self.getMBN(ln)[0]
        mb=self.getMB(mbn)
        mb.append([ing[0],ing[1],ing[2]])

    def add(self,ln):
        if ln.startswith("Add dry ingredients"):
            sum=0
            for i in self.il:
                if self.il[i][1]=="dry":
                    sum+=self.il[i][0]
            ln=ln[20:]
            mbn=1
            if ln!="":
                ln=ln[3:]
                mbn=self.getMBN(ln)[0]
            mb=self.getMB(mbn)
            mb.append([sum,"dry","sum"])
            return
        ln=ln[4:]
        n,ln=self.getIngName(ln)
        ing=self.il[n]
        mbn=1
        if len(ln)>4:
            ln=ln[3:]
            mbn=self.getMBN(ln)[0]
        mb=self.getMB(mbn)
        #print(mbn,ing)
        mb[-1][0]+=ing[0]

    def remove(self,ln):
        ln=ln[7:]
        n,ln=self.getIngName(ln)
        ing=self.il[n]
        mbn=1
        #print([n,ln])
        if len(ln)>4:
            ln=ln[5:]
            mbn=self.getMBN(ln)[0]
        mb=self.getMB(mbn)
        mb[-1][0]-=ing[0]

    def combine(self,ln):
        ln=ln[8:]
        n,ln=self.getIngName(ln)
        ing=self.il[n]
        mbn=1
        if len(ln)>4:
            ln=ln[5:]
            mbn=self.getMBN(ln)[0]
        mb=self.getMB(mbn)
        mb[-1][0]*=ing[0]

    def divide(self,ln):
        ln=ln[7:]
        n,ln=self.getIngName(ln)
        ing=self.il[n]
        if ing[0]==0:
            print("Error: Dividing by zero is forbidden, you fool!")
            exit()
        mbn=1
        if len(ln)>4:
            ln=ln[5:]
            mbn=self.getMBN(ln)[0]
        mb=self.getMB(mbn)
        mb[-1][0]/=ing[0]

    def pour(self,ln):
        ln=ln[21:]
        mbn,ln=self.getMBN(ln)
        ln=ln[21:]
        bdn=self.getMBN(ln)[0]
        mb=self.getMB(mbn)
        bd=self.getBD(bdn)
        for i in mb:
            bd.append([i[0],i[1],i[2]])

    def serves(self,ln):
        ln=ln[7:-1]
        n=int(ln)
        output=""
        for i in range(1,n+1):
            for j in self.getBD(i):
                if j[1]=="liquid":
                    output+=chr(j[0])
                else:
                    output+=str(j[0])+" "
        return output

    def refrigerate(self,ln):
        ln=ln[11:]
        if ln==".":
            return ""
        ln=ln[5:]
        n=""
        while ln[0]!=" ":
            n+=ln[0]
            ln=ln[1:]
        n=int(n)
        output=""
        for i in range(1,n+1):
            for j in self.bds[i]:
                if j[1]=="liquid":
                    output+=chr(j[0])
                else:
                    output+=str(j[0])+" "
        return output

    def take(self,ln):
        ln=ln[5:]
        ing=self.getIngName(ln)[0]
        inp=input("{}: ".format(ing))
        self.il[ing][0]=float(inp) if ("." in inp) else int(inp)

    def fold(self,ln):
        ln=ln[5:]
        ing,ln=self.getIngName(ln)
        ln=ln[5:]
        mbn=self.getMBN(ln)[0]
        ig=self.getMB(mbn).pop()
        self.il[ing][0]=ig[0]

    def liquefy(self,ln):
        ln=ln[8:]
        if ln.startswith("contents"):
            ln=ln[9:]
            mbn=1
            if ln!="":
                mbn=self.getMBN(ln[7:])[0]
            for i in self.mbs[mbn]:
                i[1]="liquid"
        else:
            ing=self.getIngName(ln)[0]
            self.il[ing][1]="liquid"

    def stir(self,ln):
        ln=ln[5:]
        mbn=1
        pn=0
        if ln.endswith("minutes.") or ln.endswith("minute."):
            if ln.startswith("the"):
                ln=ln[4:]
                mbn,ln=self.getMBN(ln)
            ln=ln[:-9] if ln.endswith("minutes.") else ln[:-8]
            n=""
            while ln[-1]!=" ":
                n=ln[-1]+n
                ln=ln[:-1]
            pn=int(n)
        else:
            ing,ln=self.getIngName(ln)
            pn=self.il[ing][0]
            #print([ln])
            if ln!="":
                ln=ln[9:]
                mbn=self.getMBN(ln)[0]
        if len(self.mbs[mbn])-pn-1>=0:
            self.mbs[mbn].insert(len(self.mbs[mbn])-pn-1,self.mbs[mbn].pop())
        else:
            self.mbs[mbn].insert(0,self.mbs[mbn].pop())

    def mix(self,ln):
        mbn=1
        if ln!="Mix well.":
            mbn=self.getMBN(ln[8:])[0]
        random.shuffle(self.mbs[mbn])

    def clean(self,ln):
        mbn=self.getMBN(ln[6:])[0]
        self.mbs[mbn]=[]

    def servewith(self,ln):
        ln=ln[11:]
        for i in range(len(self.code)):
            if self.code[i]==ln:
                auxMbs={}
                for m in self.mbs:
                    auxMbs[m]=[[k for k in j] for j in self.mbs[m]]
                #print(auxMbs)
                auxChef=Chef("\n".join(self.code),auxMbs)
                auxChef.parse(False,i)
                fmb=self.getMB(1)
                fmba=auxChef.getMB(1)
                fmb.clear()
                for j in fmba:
                    fmb.append([k for k in j])
                break

    def loop(self,code,i,debug=False):
        ln=code[i]
        verb=code[i].split(" ")[0]
        ln=ln[len(verb)+5:]
        ing=self.getIngName(ln)[0]
        verbed=verb.lower()
        if verb.endswith("y"):
            verbed=verbed[:-1]+"i"
        elif verb.endswith("e"):
            verbed=verbed[:-1]
        verbed+="ed"
        idx=-1
        lvl=1
        for j in range(i+1,len(code)):
            #print(code[j],verbed,code[j].endswith("until "+verbed+"."))
            if code[j].endswith("until "+verbed+"."):
                if lvl==1:
                    idx=j
                    break
                else:
                    lvl-=1
            if (code[j].startswith(verb)) and (not ("until" in code[j])):
                lvl+=1
        if idx==-1:
            print("Error: loop starting with '"+code[i]+"' not closed.")
            exit()
        ll=code[idx]
        ic=code[i+1:idx]
        for j in range(i+1,idx+1):
            code.pop(i+1)
        dec=False
        ing2=None
        if ll.split(" ")[1]=="the":
            dec=True
            ing2=self.getIngName(ll.split("the ")[1])[0]
        ret=False
        while self.il[ing][0]>0:
            res=self.exec([l for l in ic],debug)
            if dec:
                self.il[ing2][0]-=1
            if res==0x10:
                break
            elif res==0x20:
                ret=True
                break
        if ret:
            return 0x20
