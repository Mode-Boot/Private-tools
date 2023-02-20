import string,random,pathlib,sys,argparse,itertools,threading

class password_build:

    def __init__(self):

        self.low = string.ascii_lowercase
        self.upp = string.ascii_uppercase
        self.dig = string.digits
        self.pun = string.punctuation
        self.path_name = "password_list"
        self.cycle = itertools.cycle(r"/-\|")

    def type_word(self,type_text):
        # low upp dig pun
        if type_text == "low":
            return self.low
        if type_text == "upp":
            return self.upp
        if type_text == "dig":
            return self.dig
        if type_text == "pun":
            return self.pun
        else:
            return ""
    
    def random_password_build(self,type_word,file_name,word_line,line_text):
        list_pass = []
        try:
            pathlib.Path(self.path_name).mkdir(exist_ok=True)
            with open(f"{self.path_name}/{file_name}.txt","w+",encoding="utf-8")as f:
                for text in range(int(line_text)):
                    for pass_date in range(int(word_line)):
                        date_text = random.choice(type_word)
                        list_pass.append(date_text)
                    password = "".join(list_pass)
                    list_pass = []
                    sys.stdout.write("\r")
                    sys.stdout.write(f"{password} -- [{next(self.cycle)}]")
                    sys.stdout.flush()
                    f.write(f"{password} \n")

        except KeyboardInterrupt:
            sys.stdout.write("\nFinnsh / Random_Password")
            sys.exit()


    def password_build(self,type_word,file_name,word_line):

        try:
            pathlib.Path(self.path_name).mkdir(exist_ok=True)
            with open(f"{self.path_name}/{file_name}.txt","w+",encoding="utf-8")as f:
                for password_text in itertools.product(type_word,repeat=int(word_line)):
                    password = "".join(password_text)
                    sys.stdout.write("\r")
                    sys.stdout.write(f"{password} -- [{next(self.cycle)}]")
                    sys.stdout.flush()
                    f.write(f"{password}\n")
        except KeyboardInterrupt:
            sys.stdout.write("\nFinnsh / Password_Build!!")
            sys.exit()

def main(password=password_build(),pass_list=[]):
    arg = argparse.ArgumentParser()
    arg.add_argument("-ty",type=str,help="Password_Build<pb> Random_Password_Build<rpb>")
    arg.add_argument("-f",type=str,help="New_File_Name")
    arg.add_argument("-woty",type=str,nargs=4,help="Word_Type low(abc..) upp(ABC..) dig(012..) pun(!@#...) No_Type<n>")
    arg.add_argument("-woli",type=int,help="Word_line [012 : 3 ...]")
    arg.add_argument("-lite",type=int,help="random_password_password mode / No mode 0")
    parse = arg.parse_args()
    for type_word in parse.woty:
        word_date = password.type_word(type_word)
        pass_list.append(word_date)
    word = "".join(pass_list)
    if parse.ty == "pb":
        th = threading.Thread(target=password.password_build,args=(word,parse.f,parse.woli,))
        th.start()
    elif parse.ty == "rpb":
        th = threading.Thread(target=password.random_password_build,args=(word,parse.f,parse.woli,parse.lite,))
        th.start()
    else:
        sys.stdout.write("\nNot_Found_Command")
        sys.exit()
if __name__ == "__main__":
    main()

        
