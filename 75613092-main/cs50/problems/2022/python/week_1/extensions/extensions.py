def main():
    file_name = input("File Name: ").lower().strip().split(".")
    image = [
        "jpeg",
        "gif",
        "jpg",
        "jpeg",
        "png",
        ]
    application = [
        "pdf",
        "zip"
    ]


    status = ""
    for i in file_name:
        found = False
        if i in image:
            status = i
        elif i in application:
            status = i
        else:
            status = i

    if status == "jpg":
        status = "jpeg"

    if status in image:
        print(f"image/{status}")
    elif status in application:
        print(f"application/{status}")
    elif "txt" in file_name:
        status = "txt"
        print("text/plain")

    else:
        print("application/octet-stream")
main()