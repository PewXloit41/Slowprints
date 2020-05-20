
import sys
import time

def slow(s):
	for i in s:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(10. / 100) # jika typing nya kurang cepat, kamu bisa merubahnya pada angka 10

slow("""Teksnya Kamu Tulis Disini
""")
