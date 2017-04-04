import re

with open("../data/pg1404.txt") as f:
    text = f.readlines()

# break up into constituent papers
papers = {}
buffer = []
i = 0
authors = re.compile("^HAMILTON\n$|^JAY\n$|^MADISON\n$")

for line in text:
    if "FEDERALIST No." in line:
        papers[i] = buffer
        buffer = []
        i += 1
        continue

    line = re.sub(authors, "", line)
    buffer.append(line)


for paper_num, paper_txt in papers.items():
    with open("../data/federalist_" + str(paper_num) + ".txt", 'w') as f:
        for line in paper_txt:
            f.write(line)
            #print(line)



