#Turns DNA sequence into mRNA sequence
rna = ""
dna = str(input("Hello, enter your DNA: "))
newdna = dna.upper()
for i in range(len(dna)):
    if newdna[i] == 'A':
        rna += 'G'
    elif newdna[i] == 'G':
        rna += 'A'
    elif newdna[i] == 'T':
        rna += 'C'
    elif newdna[i] == 'C':
        rna += 'U'    
print("Your RNA is: " + rna )

print(rna[0:len(rna):3])
