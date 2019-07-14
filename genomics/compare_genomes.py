# DAVIDRVU - 2019

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer

def main():
    print("COMPARE GENOMES")

    #########0000000001111111111222222222233333333334444444444
    #########1234567890123456789012345678901234567890123456789
    ind07 = "gcctatcggtgaccaactcgatgggtctatcggcaagccacgcgatgtg"
    ind10 = "atatcttggcaaccaactcgatgggtctatcggcaagccacgcgatatg"

    #########0000000001111111111222222222233333333334444444444
    #########1234567890123456789012345678901234567890123456789
    ind03 = "gtcactcggtaggcctctcggtgagtatctcgataggtaactcggcgtc"
    ind12 = "atctctcggtaggcctctcggtgagtatctcgataggtctatcggtatg"

    print(longestSubstringFinder("apple pie available", "apple pies"))
    print(longestSubstringFinder(ind07, ind10))
    print("\n")
    print(longestSubstringFinder(ind03, ind12))



if __name__ == "__main__":
    main()