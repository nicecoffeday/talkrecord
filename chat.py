



#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #sig 去掉記憶體編碼
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines: #把lines 裡的東西一個一個叫出來
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person :
       		new.append(person + ': ' + line)
    return(new)    

def write_file(filename, lines):
    with open(filename , 'w') as f:
        for line in lines:
            f.write(line + '\n')



#進入點
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('123.txt', lines) # 產生檔案的檔名

main()
