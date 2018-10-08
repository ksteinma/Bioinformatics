def rna_translate(bases):
    """
    Takes in string of bases. Then, considers first group of three bases in the first codon.
    Finds the appropriate amino acid that the codon is associated with and adds that
    to the translation string. Then there are no longer three bases left,
    the translation is final and it is printed. 
    """
    translation = ''
    while (len(bases[:3])==3):
        if(bases[0]=='U'):
            if(bases[1]=='U'):
                if(bases[2]=='U' or bases[2]=='C'):
                    translation = translation + 'F'
                else:
                    translation = translation + 'L'
            elif(bases[1]=='C'):
                translation = translation + 'S'
            elif(bases[1]=='A'):
                if(bases[2]=='U' or bases[2]=='C'):
                    translation = translation + 'Y'
                #else:
                    #translation.append('stop')
            else:
                if(bases[2]=='U' or bases[2]=='C'):
                    translation = translation + 'C'
                elif(bases[2]=='A'):
                    translation = translation
                else:
                    translation = translation + 'W'
        elif(bases[0]=='C'):
            if(bases[1]=='U'):
                translation = translation + 'L'
            elif(bases[1]=='C'):
                translation = translation + 'P'
            elif(bases[1]=='A'):
                if(bases[2]=='U' or bases[2]=='C'):
                    translation = translation + 'H'
                else:
                    translation = translation + 'Q'
            else:
                translation = translation + 'R'
        elif(bases[0]=='A'):
            if(bases[1]=='U'):
                if(bases[2]=='G'):
                    translation = translation + 'M'
                else:
                    translation = translation + 'I'
            elif(bases[1]=='C'):
                translation = translation + 'T'
            elif(bases[1]=='A'):
                if(bases[2]=='U' or bases[2]=='C'):
                    translation = translation + 'N'
                else:
                    translation = translation + 'K'
            else:
                if(bases[2]=='U' or bases[2]=='C'):
                    translation = translation + 'S'
                else:
                    translation = translation + 'R'
        else:
            if(bases[1]=='U'):
                translation = translation + 'V'
            elif(bases[1]=='C'):
                translation = translation + 'A'
            elif(bases[1]=='A'):
                if(bases[2]=='U' or bases[2]=='C'):
                    translation = translation + 'D'
                else:
                    translation = translation + 'E'
            else:
                translation = translation + 'G'
        bases = bases[3:]
    
    print(translation)

def main():
    filename = input('Please enter the filename that you would like to read codons from:\n')
    content = open(filename, 'r')
    bases = content.readline()
    rna_translate(bases)

if __name__ == "__main__":
    main()
