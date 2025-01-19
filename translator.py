import sys
import os

def main():
    # print(sys.argv[1])
    file_name = sys.argv[1]
    run = (f"{file_name[:len(file_name)-4]}.cpp")
    compiled = open(f"{file_name[:len(file_name)-4]}.cpp",'w')
    x = 0
    with open(file_name,"r") as codeFile:
        for line in codeFile:
            # print(type(line))
            # print(line)
            x=x+1
            # print(line)

            # Implemantation of comment
            if line[0] == '@':
                continue
            
            # Implimentation of blank space
            elif line == "\n":
                continue
            
            elif "#ADD" in line[0:4]:
                if "I/O" in line[4:10]:
                    compiled.write("#include<iostream>\n")
                elif "MATH" in line[4:12]:
                    compiled.write("#include<cmath>\n")
                
            
            # Implimentation of the Start Key Word
            elif "START" in line.upper():
                compiled.write("int main(){\n")

            #inplimatation of int datatype 
            elif "INT" in line[0:3]:
                compiled.write(f"\tint{line[3:len(line)-1]};\n")
            
            #inplimatation of STRING datatype 
            elif "STR" in line[0:3]:
                compiled.write(f"\tstd::string {3:};\n")
            
            #inplimatation of FLOAT datatype 

            elif "FLOAT" in line[0:6]:
                compiled.write(f"\tdouble {line[6:len(line)-1]};\n")
            
            # Implimentation of Char datatype
            elif "CHAR" in line[0:4]:
                compiled.write(f"\tchar {line[4:len(line)-1]};\n")


            ########### Pointer datatype ############

            elif "INT*" in line[0:4]:
                compiled.write(f"\t*int {line[4:len(line)-1]};\n")
            
            #inplimatation of FLOAT datatype 

            elif "FLOAT*" in line[0:7]:
                compiled.write(f"\tdouble *{line[7:len(line)-1]};\n")
            
            # Implimentation of Char datatype
            elif "CHAR*" in line[0:5]:
                compiled.write(f"\tchar *{line[5:len(line)-1]};\n")

            

            ################ End of Pointer Datatype #####################
            
            # Implimentation of the write Keyword
            elif "WRITE" in line:
                if line[len(line)-1] == ';':
                    compiled.write(f"\tstd::cout<<{line[6:len(line)-1]}<<std::endl;\n")
                else:
                    compiled.write(f"\tstd::cout<<{line[6:len(line)-1]};\n")
                # print(line[6:])
            elif "READ" in line:
                for x in range(len(line)):
                    if line[x] == ',':
                        break
                # var = input(line[5:x])
                compiled.write(f"\tstd::cout<<{line[5:x]};\n")
                compiled.write(f"\tstd::cin>>{line[x+1:]}")


            # Implimentation of Arrays
            elif "ARY" in line[0:3]:
                # Define Array Types
                if "ARYINT" in line[0:6]:
                    # Integer Array
                    for x in range(len(line)-1):
                        if line[x+5] != "":
                            break
                    for g in range(len(line)-1):
                        if line[g] == ",":
                            break
                    compiled.write(f"\tint {line[x+7:g]}[{line[g+1:len(line)-1]}];\n")
                # Floating point array
                elif "ARYFLOAT" in line[0:8]:
                    # Integer Array
                    for x in range(len(line)-1):
                        if line[x+8] != "":
                            break
                    for g in range(len(line)-1):
                        if line[g] == ",":
                            break
                    compiled.write(f"\tdouble {line[x+9:g]}[{line[g+1:len(line)-1]}];\n")
                
                # Character Array
                elif "ARYCHAR" in line[0:7]:
                    # Integer Array
                    for x in range(len(line)-1):
                        if line[x+7] != "":
                            break
                    for g in range(len(line)-1):
                        if line[g] == ",":
                            break
                    compiled.write(f"\tchar {line[x+8:g]}[{line[g+1:len(line)-1]}];\n")
                
                if "ARYSTR" in line[0:6]:
                    # Integer Array
                    for x in range(len(line)-1):
                        if line[x+5] != "":
                            break
                    for g in range(len(line)-1):
                        if line[g] == ",":
                            break
                    compiled.write(f"\tstd::string {line[x+7:g]}[{line[g+1:len(line)-1]}];\n")
            

            elif any(op in line for op in ("+", "-", "/", "*","=")):
                compiled.write(f"\t{line}")
            elif "END" in line[:3]:
                compiled.write("\treturn 0;\n")
                compiled.write("}")
            # else:
            #     print(f"Syntax Error at line {x}")
    # os.system(f" gcc {run} -o {run[:4]}")
    # os.system(f"./{run[:4]}")
if __name__ == '__main__':
    main()