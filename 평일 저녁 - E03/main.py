import mymath  # 모듈이면 파일
import mypkg   # 팩키지이면 디렉토리/__init__.py
from mypkg.mymodule import mymultiply
from mypkg import mymultiply

print(mymath.mysum(1, 2))
print(mymultiply(1, 2))

