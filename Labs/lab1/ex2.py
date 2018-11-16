def main():
   print ("Introduza vinte numeros")
   num_vec = []
   i=0
   while i<20:
    num_vec.append(input("> "))
    i=i+1 
   
   sum=0
   for x in num_vec:
    sum = x + sum

   sum= sum/20.0 
   print "A media dos 20 numeros e:\n" 
   print sum


if __name__ == '__main__':
   main()