import pathlib,sys,random,shutil,os,string
from cryptography.fernet import Fernet

class Cry_Test:

    def __init__(self,list_box=[]):

        word_date = string.ascii_lowercase + string.ascii_uppercase + string.digits
        for word in range(20):
            list_box.append(random.choice(word_date))
        self.word = "".join(list_box)
        self.path_name,self.file_name = "test_target","test_file_"
        self.key_path,self.key_file = "key_date","key_target.key"
        
    def test_target(self,file_list=10):

        pathlib.Path(self.path_name).mkdir(exist_ok=True)
        for file_number in range(int(file_list)):
            with open(f"{self.path_name}/{self.file_name}{file_number}.txt","w+",encoding="utf-8")as build_file:
                build_file.write(self.word)
        return self.path_name

    def target_encrypt(self,target_path):

        key_date = Fernet.generate_key()
        pathlib.Path(self.key_path).mkdir(exist_ok=True)
        with open(f"{self.key_path}/{self.key_file}","wb+")as key_file:
            key_file.write(key_date)
        key = Fernet(key_date)
        for target_file in pathlib.Path(target_path).glob("*"):
            tf = open(target_file,"r",encoding="utf-8").read()
            encode_text = key.encrypt(tf.encode())
            file_sf = pathlib.Path(target_file).stem
            os.remove(target_file)
            with open(f"{target_path}/{file_sf}.dat","wb+")as encode_tf:
                encode_tf.write(encode_text)

    def target_decrypt(self,target_path):

        key_file = open(f"{self.key_path}/{self.key_file}","rb")
        key = Fernet(key_file.read())
        for target_file in pathlib.Path(target_path).glob("*"):
            tf = open(target_file,"rb").read()
            decode_text = key.decrypt(tf).decode()
            file_sf = pathlib.Path(target_file).stem
            os.remove(target_file)
            with open(f"{target_path}/{file_sf}.txt","w+",encoding="utf-8")as decode_tf:
                decode_tf.write(decode_text)
        
    def main(self):

        cry_test = Cry_Test()
        target_path = cry_test.test_target()
        cry_test.target_encrypt(target_path)
        cry_test.target_decrypt(target_path)

if __name__ == "__main__":

    Cry_Test().main()

