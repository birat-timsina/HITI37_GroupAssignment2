# Expression Parser & Evaluator
def tokenaziation(exp):
    #initailize tokens list
    tokens = []
    i = 0

    #loop through expression and tokenize it based on character type
    while i < len(exp):
        current_char = exp[i]

        #checking for white space and skipping it
        if current_char.isspace():
            i += 1
            continue

        #checking for digits 
        elif current_char.isdigit():
            num = current_char
            i += 1

            #loop to capture the entire number if it has more than one digit
            while i < len(exp) and exp[i].isdigit():
                num += exp[i]
                i += 1
            tokens.append(("NUM", int(num)))

        #checking for operators
        elif current_char in "+-*/":
            tokens.append(("OP", current_char))
            i += 1

        #checking for parentheses
        elif current_char == "(":
            tokens.append(("LPAREN", current_char))
            i += 1

        #checking for right parentheses
        elif current_char == ")":           
            tokens.append(("RPAREN", current_char))
            i += 1

        #if the character is not recognized, raise a ValueError
        else:
            return "ERROR"
    
    #append an end token to signify end of expression
    tokens.append(("END", ""))
    return tokens

def parse_factor(tokens):
    global pos
    token_type, value = tokens[pos]
    
    #parsing unary minus
    if value == "-":
        pos += 1
        val, tree = parse_factor(tokens)
        return -val, f"(neg {tree})"
    
    #parsing number
    elif token_type == "NUM":
        pos += 1
        return float(value), value
    
    #parsing parentheses
    elif value == "(":
        pos += 1
        val, tree = parse_expression(tokens)
        
        #checking for closing parentheses
        if tokens[pos][1] != ")":
            raise Exception("Missing )")
        
        pos += 1
        return val, tree
    
    else:
        raise Exception("Invalid syntax")
        


def parse_expression(tokens):
    global pos

    #calling parse_term to get left operand and its tree
    left, tree = parse_term(tokens)
    
    #loop to handle addition and subtraction
    while tokens[pos][1] in ["+", "-"]:
        op = tokens[pos][1]
        pos += 1

        #calling parse_term to get right operand and its tree
        right, right_tree = parse_term(tokens)
        
        #handleing addition
        if op == "+":
            left = left + right

        #handling subtraction    
        else:
            left = left - right
        
        #building tree for current operation
        tree = f"({op} {tree} {right_tree})"
    
    return left, tree



def parse_term(tokens):
    global pos
    left, tree = parse_factor(tokens)
    
    #loop to handle multiplication and division
    while tokens[pos][1] in ["*", "/"]:
        op = tokens[pos][1]
        pos += 1
        right, right_tree = parse_factor(tokens)
        tree = f"({op} {tree} {right_tree})"

        #handleing multiplication
        if op == "*":
            left = left * right

        #handling division and checking for division by zero    
        else:
            if right == 0:
                raise ZeroDivisionError(tree)
            left = left / right
        
    
    return left, tree


#define function to evaluate expressions from a file
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
            if tokens == "ERROR":
                results.append({"input": exp, "tree": "ERROR", "tokens": "ERROR", "result": "ERROR"})
                continue

            token_str = ""
            for t in tokens:
                if t[0] == "END":
                    token_str += "[END]"
                else:
                    token_str += f"[{t[0]}:{t[1]}] "

            #parsimg the expression
            global pos
            pos = 0
            try:
                value, tree = parse_expression(tokens)
            except ZeroDivisionError as e:

                #if division by zero error occurs, capture tree and mark result as ERROR
                results.append({"input": exp, "tree": str(e),
                            "tokens": token_str.strip(), "result": "ERROR"})
                continue
            except Exception as e:

                #if any other parsing error occurs, capture error message and mark result as ERROR
                results.append({
                    "input": exp,
                    "tree": f"ERROR: {str(e)}",
                    "tokens": token_str.strip(),
                    "result": "ERROR"
                })
                continue
            
            
            #format result
            if value.is_integer():
                result_val = int(value)
            else:
                result_val = round(value, 4)
            
            #append final result to results list
            results.append({
                "input": exp,
                "tree": tree,
                "tokens": token_str.strip(),
                "result": result_val
            })
        
        except:
            #if any unexpected error occurs during tokenization or parsing, mark all fields as ERROR
            results.append({
                "input": exp,
                "tree": "ERROR",
                "tokens": "ERROR",
                "result": "ERROR"
            })

    #writing output file
    with open("output.txt", "w") as f:
        for r in results:
            f.write(f"Input: {r['input']}\n")
            f.write(f"Tree: {r['tree']}\n")
            f.write(f"Tokens: {r['tokens']}\n")
            f.write(f"Result: {r['result']}\n\n") 

#main function
if __name__ == "__main__":            
              
    #calling evaluate function with input.txt file
    evaluate_file("input.txt")

