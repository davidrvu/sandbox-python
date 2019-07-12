# DAVIDRVU - 2019

# pip import regex

import regex

#m = regex.findall("AAG", "CATGAAG")
#print(m)

#m = regex.findall("(AAG){s<=1}", "CATGAAG", overlapped=True) # means  allow up to 1 sustitution
#print(m)

def find_genome(to_find, full_genome):
    m = regex.findall("("+to_find+"){s<=1}", full_genome, overlapped=True) # means  allow up to 1 sustitution
    print(m)

    if len(m) == 1:
        position = full_genome.find(m[0])
        #print(position)
        print("Posicion final = " + str(position+1))

def main():
    full_genome = "ggccgcctcccgcgcccctctgtcccctcccgtgttcggcctcgggaagtcggggcggcgggcggcgcgggccgggaggggtcgcctcgggctcaccccgccccagggccgccgggcggaaggcggaggccgagaccagacgcggagccatggccgaggtgttgcggacgctggccg"
    to_find_list = []
    to_find_list.append("ccggcctcgggaag")
    to_find_list.append("ttgcggacgctagc")
    to_find_list.append("tcgggctccccccg")
    to_find_list.append("ggggggaaggcgga")
    to_find_list.append("tctgtccccccccg")

    for to_find in to_find_list:
        find_genome(to_find, full_genome)

if __name__ == "__main__":
    main()