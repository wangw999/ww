import sys
import django
import djongo
import pytz

print(sys.path)

print(django.get_version())

print(djongo.__version__)

print(pytz.VERSION)


def client_is_modern(self):
    print("Environ:", self.environ)  # 添加这行进行调试
    return self.environ['SERVER_PROTOCOL'].upper() != 'HTTP/0.9'
