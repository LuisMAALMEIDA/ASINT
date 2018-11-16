class rpnCalculator:
    
    stack = []
    def __init__(self):
        self.stack=[]
    

    def pushValue(self, input):

        self.stack.append(input)    

    def popValue(self): 
        if( len(self.stack)>0):
            print (self.stack[len(self.stack)-1]) 
            self.stack.pop(len(self.stack)-1)
        else:
            print("A pilha esta vazia")    

    def add(self):
        
        if( len(self.stack)>1):
            aux1=self.stack[len(self.stack)-1]      
            self.stack.pop(len(self.stack)-1)
            aux2=self.stack[len(self.stack)-1]      
            self.stack.pop(len(self.stack)-1)
            self.stack.append(int(aux1)+int(aux2))
            
            
        else:
            print("A pilha tem menos do que dois elementos")    

        
    def sub(self):
        if( len(self.stack)>1):
            aux1=self.stack[len(self.stack)-1]      
        self.stack.pop(len(self.stack)-1)
        aux2=self.stack[len(self.stack)-1]      
        self.stack.pop(len(self.stack)-1)

        self.stack.append(int(aux1)-int(aux2))    
'''
def main():

    stack1=rpnCalculator()

    print("Introduza um dos seguintes comandos: push, pop, add, sub")

    str=input("> ")
    print(str)
    while((str)!= "q"):

        if(str== "push"):
            print("Introduza um n")
            stack1.pushValue(input("> "))
            
        if(str== "pop"):
            stack1.popValue()

        if(str== "add"):
            stack1.add()

        if(str== "sub"):
            stack1.sub()

        print("Introduza um dos seguintes comandos: push, pop, add, sub")
        str=input("> ")        

    
   


if __name__ == '__main__':
   main()
   
'''   
   
