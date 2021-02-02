import requests

def main():
    response = requests.get("https://afara.my.id/api/v3/ebook", data = '{"q": "Matematika"}', headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer r50kG-iqHDw-TD4cg-I19uS"
    }).json()
    print(response)

if __name__ == "__main__":
    main()
