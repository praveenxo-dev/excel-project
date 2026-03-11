import requests


def get_excel(url, filename):
    response = requests.get(url)

    content_type = response.headers.get("Content-Type")

    if response.status_code == 200 and "application" in content_type:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"File downloaded successfully: {filename}")
    else:
        print("Download failed or returned HTML instead of Excel")
        print("Content-Type:", content_type)
