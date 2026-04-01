
#define function
def evaluate_file(input_path: str):             
    results = [] #initailize results list
    
    #open file and read lines
    with open(input_path, "r") as f:  
        #read file line by line and store them in a list          
        lines = f.readlines()

    #accessing stored lines 
    for line in lines:  
        #strip actual content from line and print it                        
        exp = line.strip()                      
        
        if exp == "":
            continue
        try:
            #tokenize texpression and print the result
            tokens = tokenaziation(exp)            
            print(f"Tokens: {tokens}")
            
        except ValueError as e:
            print(f"Error: {e}")


def tokenaziation(exp):
    #initailize tokens list
    tokens = []
    i = 0
    #loop through expression and tokenize it based on character type
    while i < len(exp):
        char = exp[i]
        #checking for white space and skipping it
        if char.isspace():
            i += 1
            continue
        #checking for digits 
        elif char.isdigit():
            num = char
            i += 1
            #loop to capture the entire number if it has more than one digit
            while i < len(exp) and exp[i].isdigit():
                num += exp[i]
                i += 1
            tokens.append(("NUM", int(num)))
        #checking for operators
        elif char in "+-*/":
            tokens.append(("OP", char))
            i += 1
        #checking for parentheses
        elif char == "(":
            tokens.append(("LPAREN", char))
            i += 1
        #checking for right parentheses
        elif char == ")":           
            tokens.append(("RPAREN", char))
            i += 1
        #if the character is not recognized, raise a ValueError
        else:
            raise ValueError(f"Invalid character: {char}")
            i += 1
    #append an end token to signify the end of the expression
    tokens.append(("END", ""))
    return tokens


#main function
if __name__ == "__main__":                      
    #calling evaluate function with input.txt file
    evaluate_file("input.txt")