

def evaluate_file(input_path: str):             #define function
    results = []                                #initailize results list
    
    with open(input_path, "r") as f:            #open file
        lines = f.readlines()                   #read file line by line and store them
    
    for line in lines:                          #accessing stored lines 
        exp = line.strip()                      #strip actual content from line
        print(exp)                              #print contents

if __name__ == "__main__":                      #main function
    evaluate_file("input.txt")                  #calling evaluate function with input.txt file