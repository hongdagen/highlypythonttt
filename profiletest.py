import cProfile
import hashlib


def main():
    list_test = []
    for i in range(10000):
        list_test.append(i)


# cProfile.run('main()')

# str1 = '123'
# sha = hashlib.sha1()
# sha.update(str1.encode())
# sha_password = sha.hexdigest()
#
# print(sha_password)

print(sum(0.1 for i in range(10)))