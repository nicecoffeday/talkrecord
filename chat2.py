



#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #sig 去掉記憶體編碼
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    Allen_word_count = 0
    Viki_word_count = 0
    Allen_sticker_count = 0
    Viki_sticker_count =0
    Allen_img_count =0
    Viki_img_count =0

    for line in lines: #把lines 裡的東西一個一個叫出來
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片':
                Allen_img_count += 1
            else:
                for m in s[2:]:
                    Allen_word_count += len(m)

        elif name == 'Viki': 
            if s[2] == '貼圖':
                Viki_sticker_count += 1 
            elif s[2] == '圖片':
                Viki_img_count += 1
            else :      
                for m in s[2:]:
                    Viki_word_count += len(m)
    print('Allen talk', Allen_word_count, '傳了',  Allen_sticker_count, '個貼圖')
    print('Viki talk', Viki_word_count, '傳了',  Viki_sticker_count, '個貼圖')
    print('Allen', '傳了', Allen_img_count, '個圖片')
    print('Viki', '傳了', Viki_img_count, '個圖片')
       # print(s)
    
def write_file(filename, lines):
    with open(filename , 'w') as f:
        for line in lines:
            f.write(line + '\n')



#進入點
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('123.txt', lines) # 產生檔案的檔名

main()
