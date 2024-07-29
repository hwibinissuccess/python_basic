def copy_file(src, dst):
    with open(src_filename, "rb")as src_file:
        content = src_file.read()
    with open(dst_filename, "wb")as dst_file:
        dst_file.write(content)

src_filename = input("복사할 파일 이름: ")
dst_filename = input("복사된 파일의 이름: ")
copy_file(src_filename, dst_filename)