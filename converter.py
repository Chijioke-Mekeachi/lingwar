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
            x=x+1
            # print(line)
            if "START" in line:
                compiled.write("#include<iostream>\n")
                compiled.write("int main(){\n")
            if "INT" in line[0:3]:
                compiled.write(f"\tint {3:};\n")
            if "STR" in line[0:3]:
                compiled.write(f"\tstd::string {3:};\n")
            if "WRITE" in line:
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
                compiled.write(f"\tstd::cout<<{line[5:x-1]};\n")
                compiled.write(f"\tstd::cin>>{line[x+1:]}")
            elif line[0] == '@':
                continue
            elif "END" in line[:3]:
                compiled.write("\treturn 0;\n")
                compiled.write("}")
            else:
                print(f"Syntax Error at line {x}")
    # os.system(f" gcc {run} -o {run[:4]}")
    # os.system(f"./{run[:4]}")
if __name__ == '__main__':
    main()