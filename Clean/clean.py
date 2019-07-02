import re


class clean():

    myPath = 'C:\\Users\\ccharlton\\PycharmProjects\\Exercises\\Exercise2\\win\\'

    def openFile(self, file):
        try:
            with open(file, "r") as file:
                # print(filterlist.read())
                words = []
                for line in file:
                    line_words = line.split()
                    for word in line_words:
                        words.append(word)
            return words
        except Exception as e:
            print(e)



    def remove_whiteSpace(self, text):
        try:
            pattern = '\s'  # match all white space
            t = re.split(pattern, text)
            # t = re.findall(pattern, text)
            whiteSpace = ' '.join(t)
            return whiteSpace
        except Exception as e:
            print(e)



def main():
    c = clean()
    s = c.openFile("C:\\Users\\ccharlton\\PycharmProjects\\Exercises\\Exercise2\\win\\winSys_info_20190701-173708.txt")

    # c = c.remove_whiteSpace(s)
    print(s)
    # print(c)


if __name__ == '__main__':
    main()