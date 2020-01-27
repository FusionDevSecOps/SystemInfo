class oS:


    def command1(command):
        try:
            import subprocess

            output = subprocess.check_output(command, universal_newlines=True)
            return output

        except Exception as e:
            print(e)


    def command2(command):
        try:
            import subprocess
            # with open('winSys_info_' + timeStr + '.csv', "a") as myFile:
            #     myFile.write("\n\nThe command that was run was\n" + command + " with output" + "\n\n")

            output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,
                                      shell=True)
            out, err = output.communicate()
            if out == '':
                return err
            else:
                return out
            return out

        except Exception as e:
            print(e)
            return err
            raise Exception


    def commandWin(command):
        try:
            import subprocess
            # with open('winSys_info_' + timeStr + '.csv', "a") as myFile:
            #     myFile.write("\n\nThe command that was run was\n" + command + " with output" + "\n\n")

            output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=False)
            out, err = output.communicate()
            if out == '':
                return err
            else:
                return out
            return out

        except Exception as e:
            print(e)
            return err
            raise Exception

    def commandLinux(command):
        try:
            import subprocess
            p = subprocess.Popen(command, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
            out, err = p.communicate()
            print(out)
            return out, err

        except Exception as e:
            print(e)