import os
import re

class retrieve_sort_compare:

    myPath = 'C:\\Users\\ccharlton\\PycharmProjects\\Exercises\\Exercise2\\win\\' #Will need to pass this as a var
    # Lists files in this directory and searches for specific files
    def retrieve_sort(self, filename):

        try:
            files = os.listdir(retrieve_sort_compare.myPath)
            mylist = []
            for file in files:
                if file.lstrip().startswith(filename):  # Search for only the keywrd Noun
                    mylist.append(file)
                mylist.sort(reverse=True)
            # print(mylist)
            # print(mylist[0])
            # print(mylist[1])

            a = mylist[0]
            b = mylist[1]

            return mylist  # Return a the last two entries in the list

        except Exception as e:
            print(e)

    # This method takes in two files an compares them, if there is no change then it returns same
    def compare(self, path, file1, file2, str):
        try:
            with open(path + file1, "r") as f1:
                f1_text = f1.read()
            with open(path + file2, "r") as f2:
                f2_text = f2.read()
            # Find and print the diff:

            # Cast to a set
            A = {f1_text}
            B = {f2_text}

            # print(A.difference(B))
            # print(B.difference(A))

            compare_result = A.difference(B)

            if len(compare_result) == 0:
                print("\n No change")
            else:
                # print(compare_result)
                print("\n The " + str + " that have changed are: \n")
                str1 = ' '.join(compare_result)  # Joins strings otherwise error is produced
                print(str1)
                # str2 = ''.join(str1)  # Joins strings otherwise error is produced
                # compare_result_Count = Counter({str1})
                # print(str2)
                # print(compare_result_Count)

            return


        except Exception as e:

            print(e)

    # This method is used to run the class
    def run(self):
        try:
            CN = retrieve_sort_compare()  # Create instance of object
            # CC.retrieve_sort('Noun') #Searches for files with the key word 'Noun'
            # print(CC.retrieve_sort())

            # List of the last two elements has been returned
            list = CN.retrieve_sort('win')
            # print(list)
            # Passing releveant files to check content
            CN.compare(retrieve_sort_compare.myPath, list[0], list[1], 'specs')
            # CC.compare('Noun_List.txt', 'Noun_List20190620-131122.txt')

        except Exception as e:

            print(e)




def main():
    r = retrieve_sort_compare()
    r.run()


if __name__ == '__main__':
    main()