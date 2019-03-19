import sys
stdout = open('stdout.txt','w',encoding='utf-8')
stderr = open('stderr.txt','w',encoding='utf-8')
sys.stdout = stdout
sys.stderr = stderr
print("hello world")
stdout.close()
stderr.close()
