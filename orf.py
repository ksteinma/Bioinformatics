import re
global out

def orf(inbases):
    """
    Takes in DNA bases from a file and translates them to RNA. Finds all indices
    of a start codon. 'started' is set to True when a start codon is encountered.
    'started' is set to False when a stop codon is encountered. If 'started' is
    True when a stop codon is encountered, then the translated string is added to
    the set 'strings', which gets returned at the end. 
    """
    #must start with AUG
    #must end with UAG, UGA, or UAA
    strings = set()
    translation = ''
    started = False
    
    #find anywhere there is a start codon
    indices = [m.start() for m in re.finditer('AUG', inbases)] 

    #iterate beginning at all start codons
    for index in indices:
        bases = inbases[index:]
        #while there are still at least 3 codons left
        #translate to amino acids
        while (len(bases[:3])==3):
            if(bases[0]=='U'):
                if(bases[1]=='U'):
                    if(bases[2]=='U' or bases[2]=='C'):
                        if(started):
                            translation = translation + 'F'
                    else:
                        if(started):
                            translation = translation + 'L'
                elif(bases[1]=='C'):
                    if(started):
                        translation = translation + 'S'
                elif(bases[1]=='A'):
                    if(bases[2]=='U' or bases[2]=='C'):
                        if(started):
                            translation = translation + 'Y'
                    else:
                        #stop codon
                        if(started):
                            started = False
                            strings.add(translation)
                            translation = ''
                            break
                else:
                    if(bases[2]=='U' or bases[2]=='C'):
                        if(started):
                            translation = translation + 'C'
                    elif(bases[2]=='A'):
                        #stop codon
                        if(started):
                            started = False
                            strings.add(translation)
                            translation = ''
                            break
                    else:
                        if(started):
                            translation = translation + 'W'
            elif(bases[0]=='C'):
                if(bases[1]=='U'):
                    if(started):
                        translation = translation + 'L'
                elif(bases[1]=='C'):
                    if(started):
                        translation = translation + 'P'
                elif(bases[1]=='A'):
                    if(bases[2]=='U' or bases[2]=='C'):
                        if(started):
                            translation = translation + 'H'
                    else:
                        if(started):
                            translation = translation + 'Q'
                else:
                    if(started):
                        translation = translation + 'R'
            elif(bases[0]=='A'):
                if(bases[1]=='U'):
                    if(bases[2]=='G'):
                        #start codon
                        started = True
                        if(started):
                            translation = translation + 'M'
                    else:
                        if(started):
                            translation = translation + 'I'
                elif(bases[1]=='C'):
                    if(started):
                        translation = translation + 'T'
                elif(bases[1]=='A'):
                    if(bases[2]=='U' or bases[2]=='C'):
                        if(started):
                            translation = translation + 'N'
                    else:
                        if(started):
                            translation = translation + 'K'
                else:
                    if(bases[2]=='U' or bases[2]=='C'):
                        if(started):
                            translation = translation + 'S'
                    else:
                        if(started):
                            translation = translation + 'R'
            else:
                if(bases[1]=='U'):
                    if(started):
                        translation = translation + 'V'
                elif(bases[1]=='C'):
                    if(started):
                        translation = translation + 'A'
                elif(bases[1]=='A'):
                    if(bases[2]=='U' or bases[2]=='C'):
                        if(started):
                            translation = translation + 'D'
                    else:
                        if(started):
                            translation = translation + 'E'
                else:
                    if(started):
                        translation = translation + 'G'
            #move to next codon
            bases = bases[3:]
        
    return strings

def main():
    out = set()
    filename = input('Please enter the filename that you would like to read DNA codons from:\n')
    content = open(filename, 'r')
    bases = content.readline()
    
    #first, replace Ts with Us
    newbases = ''
    for codon in bases:
        if (codon=='A'):
            newbases = newbases + 'A'
        elif (codon=='T'):
            newbases = newbases + 'U'
        elif (codon=='G'):
            newbases = newbases + 'G'
        else:
            newbases = newbases + 'C'
    out.update(orf(newbases))
    
    #first reverse
    reverse = bases[::-1]
    #then complement
    for codon in reverse:
        if (codon=='A'):
            reverse = reverse + 'U'
        elif (codon=='T'):
            reverse = reverse + 'A'
        elif (codon=='G'):
            reverse = reverse + 'C'
        else:
            reverse = reverse + 'G'
    out.update(orf(reverse))

    #all done
    print(out)

if __name__ == "__main__":
    main()
