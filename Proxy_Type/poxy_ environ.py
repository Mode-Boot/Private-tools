import requests,pathlib,os,random,json,sys
from bs4 import BeautifulSoup
#textarea
#target_url = "https://free-proxy-list.net/"
def install_date():
    os.system("python3 -m pip install --upgrade pip")
    os.system("pip3 install requests")
    os.system("pip3 install bs4")

def request_web(target_url="https://free-proxy-list.net/"):
    path_name,file_name = "html_proxy","proxy.html"
    res = requests.get(target_url,timeout=10)
    pathlib.Path(path_name).mkdir(exist_ok=True)
    with open(f"{path_name}/{file_name}","w+",encoding="utf-8")as html_proxy:
        html_proxy.write(res.text)
    return f"{path_name}/{file_name}"

def html_proxy(file_path,list_date=[]):
    path_name,new_file_name = "html_proxy","proxy_date.txt"
    proxy_text = open(file_path,"r",encoding="utf-8")
    html_soup = BeautifulSoup(proxy_text,"html.parser")
    with open(f"{path_name}/{new_file_name}","w+",encoding="utf-8")as proxy_list:
        proxy_list.write(html_soup.textarea.text)
    f = open(f"{path_name}/{new_file_name}","r",encoding="utf-8")
    for proxy_html in f.readlines():
        list_date.append(proxy_html)
    del list_date[0:3]
    with open(f"{path_name}/{new_file_name}","w+",encoding="utf-8")as proxy_date:
        key = {"proxy_list":list_date}
        proxy_date.write(json.dumps(key))
    return f"{path_name}/{new_file_name}"

def main():
    install_date()
    file_path = html_proxy(request_web())
    f = open(file_path,"r",encoding="utf-8")
    proxy_file = json.loads(f.read())
    proxy = random.choice(proxy_file["proxy_list"])
    os.environ["http"] = proxy.strip("\n")
    os.environ["https"] = proxy.strip("\n")
    sys.stdout.write("Set_Environ_HTTP : " + os.environ["http"])
    sys.stdout.write("Set_Environ_HTTPS : " + os.environ["https"])

if __name__ == "__main__":
    main()


