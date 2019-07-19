import time
import re
import json
from subprocess import check_output


class JsonEditer:

    def retrieveKey(text):
        """Remove all divs from a string and return"""
        try:
            pattern = re.compile('\w.*\n')
            f = ''.join(re.findall(pattern, text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def retrieveValueAfterNewLine(text):
        """Remove all divs from a string and return"""
        try:
            pattern = re.compile('\n\w.*')
            f = ''.join(re.findall(pattern, text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def removeAfterNewLine(text):
        """Remove all divs from a string and return"""
        try:
            pattern = re.compile('\n\w.*')
            f = ''.join(re.sub(pattern, '', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def removeBeforeNewLine(text):
        """Remove html tags from a string"""
        try:
            pattern = '\w.*\n'
            clean = re.compile(pattern)  # Match all occurences of characters inside the bracets
            f = ''.join(re.sub(clean, '', text))  # Joins strings otherwise error is produced
            return f
        except Exception as e:
            print(e)

    def remove_whiteSpace(text):
        try:
            pattern = '\s'  # match all white space
            t = re.split(pattern, text)
            # t = re.findall(pattern, text)
            whiteSpace = ' '.join(t)
            return whiteSpace
        except Exception as e:
            print(e)


    #basic one column
    def dictMethod(output, string):
        k = JsonEditer.removeAfterNewLine(output)
        key = JsonEditer.remove_whiteSpace(k)
        # print(key)
        v = JsonEditer.retrieveValueAfterNewLine(output)
        value = JsonEditer.remove_whiteSpace(v)

        return {string: [key, value]}


    # two columns
    def twoColumns(output, string):
        # everything before and after the tab
        '^.*\t([^\t]+)$'

        # everything before the tab
        # key = '\w.*\t'
        key = '^.*\t'
        # everything after the tab
        value = '([^\:]+)$'
        v = '\t.*\n'

        # split output on new line
        m = re.split('\n', output)

        myD = {}
        for i in range(len(m)):
            keyTuple = ''.join(re.findall('.*\t', m[i]))
            cleankey = ''.join(re.sub('\t', '', keyTuple))
            valueTuple = ''.join(re.findall('\:.*', m[i]))
            cleanValue = ''.join(re.sub(':', '', valueTuple))
            myD.update({cleankey: cleanValue})
        i += 1
        return {string: myD}



    def beforeForwardSlashAndafterBackSlash(output, string):
        m = re.split('\n', output)
        myDict = {}

        i=0
        for i in range(len(m)):
            keyTuple = ''.join(re.findall('(^\S*/)', m[i]))
            valueTuple = ''.join(re.findall('\/.*', m[i]))
            myDict.update({keyTuple: valueTuple})
        i += 1
        return {string: myDict}

    def beforeforwardslashAndaftercolon(output, help):

        myD = {}
        m = re.split('\n', output)
        # print(m[0])

        i = 0
        for i in range(len(m)):
            # print(m[i])
            keyTuple = ''.join(re.findall('.*\:', m[i]))
            cleankey = ''.join(re.sub(':', '', keyTuple))
            valueTuple = ''.join(re.findall('\:.*', m[i]))
            cleanValue = ''.join(re.sub(':', '', valueTuple))
            if valueTuple == '' and keyTuple == '':
                if m[i] != '':
                    cleankey = ''
                    cleanValue = m[i]
                else:
                    break

            # string = re.sub(" ", '', valueTuple)
            myD.update({cleankey: cleanValue})
        i += 1

        return {help: myD}

    def whiteSpaceAndBackslash(output, string):
        myD = {}
        m = re.split('\n', output)
        i = 0
        for i in range(len(m)):
            keyTuple = ''.join(re.findall('(^\S*)', m[i]))
            valueTuple = ''.join(re.findall('\/.*', m[i]))
            myD.update({keyTuple: valueTuple})
        i += 1

        return {string: myD}


    def beforeEqualsAndAfterEquals(output, string):
        m = re.split('\n', output)
        myDict = {}
        i = 0
        for i in range(len(m)):
            keyTuple = ''.join(re.findall('(^\S*=)', m[i]))
            cleanKey = ''.join(re.sub('=', '', keyTuple))
            valueTuple = ''.join(re.findall('\=.*', m[i]))
            cleanValue = ''.join(re.sub('=', '', valueTuple))

            myDict.update({cleanKey: cleanValue})
        i += 1
        return {string: myDict}


    def beforeWhitespacesAndAfterWhitespace(output, string):
        m = re.split('\n', output)
        myDict = {}
        i = 1
        for i in range(len(m)):
            keyTuple = ''.join(re.findall('(^\S*)', m[i]))
            valueTuple = ''.join(re.sub('(^\S*)', '', m[i]))
            cleanValue = ''.join(re.sub('\s', '', valueTuple))
            myDict.update({keyTuple: cleanValue})
        i += 1

        return {string: myDict}




    def saveAsJson(words, save):
        try:
            with open(save, "w") as text_file:
                print(f'{words}', file=text_file)
        except Exception as e:
            print(e)


    def jsonCreater(myDict, os):

        # import json
        # myDict = {}
        jsonData = json.dumps(myDict)
        print(jsonData)
        JsonEditer.saveAsJson(jsonData, os +'.json')


