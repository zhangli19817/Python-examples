def process_file(file):
    newfile=open(file)
    dics=dict()
    for line in newfile:
        line.replace('-','')
        process_line(line,dics)
    return dics


def process_line(line,dic):
    for word in line.split():
        word.strip(string.punctuation+string.whitespace)
        dic[word]=dic.get(word,0)+1

print(process_file("/Users/luffy/Downloads/emma.txt"))