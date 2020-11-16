

def editDistance(s1, s2):
    table = ([[i] for i in range(len(s1) + 1)])
    table[0] = [ i for i in range(0, len(s2) + 1)]
    
    
    file2.write('Minimum Edit Distance between: "' + str(s1) + '" and "' + str(s2) + '"\n"')
    file2.write("Weights/cost: Insertion: 1, Deletion: 1, Substitution: 2. \n\n")
    file2.write("After inserting both string with respect to empty string:\n\n")

    printTable(table, s1, s2)


    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            
            if (s1[i - 1] == s2[j - 1]):
                
                
                file2.write("'" + str(s1[i - 1]) + "'" + " is same as '" + str(s2[j - 1]) + "'\n\n")
                file2.write("D[i - 1][j] = " + str(table[i - 1][j]) + "\n")
                file2.write("D[i][j - 1] = " + str(table[i][j - 1]) + "\n")
                file2.write("D[i - 1][j - 1] = " + str(table[i - 1][j - 1]) + "\n")
                file2.write("\nMinimum of (D[i - 1][j] + 1), D[i][j - 1] + 1, D[i - 1][j - 1] + 0 (Character same))\n")

                if min((1 + table[i - 1][j]), (1 + table[i][j - 1]), table[i - 1][j - 1]) == (1 + table[i - 1][j]):
                    
                    file2.write("= D[i - 1][j] + 1\n")
                    
                if min((1 + table[i - 1][j]), (1 + table[i][j - 1]), table[i - 1][j - 1]) == (1 + table[i][j - 1]):
                    
                    file2.write("= D[i][j - 1] + 1\n")
                    
                if min((1 + table[i - 1][j]), (1 + table[i][j - 1]), table[i - 1][j - 1]) == (table[i - 1][j - 1]):
                    
                    file2.write("= D[i - 1][j - 1] + 0\n")
                
                
                file2.write("= " + str(min((1 + table[i - 1][j]), (1 + table[i][j - 1]), table[i - 1][j - 1])) + "\n")

                table[i].append(min((1 + table[i - 1][j]), (1 + table[i][j - 1]), table[i - 1][j - 1]))
            
            else:


                file2.write("'" + str(s1[i - 1]) + "'" + " is not same as '" + str(s2[j - 1]) + "'\n\n")
                file2.write("D[i - 1][j] = " + str(table[i - 1][j]) + "\n")
                file2.write("D[i][j - 1] = " + str(table[i][j - 1]) + "\n")
                file2.write("D[i - 1][j - 1] = " + str(table[i - 1][j - 1]) + "\n")
                file2.write("\nMinimum of (D[i - 1][j] + 1), D[i][j - 1] + 1, D[i - 1][j - 1] + 2 (Character not same))\n")
                
                if min((1 + table[i - 1][j]), (1 + table[i][j - 1]), (2 + table[i - 1][j - 1])) == (1 + table[i - 1][j]):
                    
                    file2.write("= D[i - 1][j] + 1\n")
                if min((1 + table[i - 1][j]), (1 + table[i][j - 1]), (2 + table[i - 1][j - 1])) == (1 + table[i][j - 1]):
                    
                    file2.write("= D[i][j - 1] + 1\n")
                if min((1 + table[i - 1][j]), (1 + table[i][j - 1]), (2 + table[i - 1][j - 1])) == (2 + table[i - 1][j - 1]):
                    
                    file2.write("= D[i - 1][j - 1] + 2\n")

                
                file2.write("= " + str(min((1 + table[i - 1][j]), (1 + table[i][j - 1]), (2 + table[i - 1][j - 1]))) + "\n")

                table[i].append(min((1 + table[i - 1][j]), (1 + table[i][j - 1]), (2 + table[i - 1][j - 1])))

            printTable(table, s1, s2)

    
    file2.write("Minimum Edit Distance: " + str(table[len(s1)][len(s2)]) + "\n")
  
def printTable(table, s1, s2):
    
    temp = ("_" * (6 * len(s2)))
    file2.write("\n" + str(temp) + "\n\n")
    for i in reversed(range(len(s1) + 1)):
        if i != 0:
            
            file2.write("| " + str(s1[i - 1]))
        else:
            
            file2.write("| # ")
        for j in range(len(s2) + 1):
            try:
                
                file2.write("| " + str(table[i][j]) + " ")
            except:
                
                file2.write("|   ")
        
        temp = ("_" * (6 * len(s2)))
        file2.write("|\n" + str(temp) + "\n\n")
    

    
    file2.write("|   | # ")
    for i in range(len(s2)):
        
        file2.write("| " + str(s2[i]) + " ")
    
    temp = ("_" * (6 * len(s2)))
    file2.write("|\n" + str(temp) + "\n\n")


file1 = open("C:/Users/Niloy/PycharmProjects/pythonProject/input.txt")
strings = file1.readline().split(" ")
file1.close()


file2 = open("C:/Users/Niloy/PycharmProjects/pythonProject/output.txt","w")
file2.write("") 
file2 = open("C:/Users/Niloy/PycharmProjects/pythonProject/output.txt","a")




editDistance(strings[0], strings[1])

