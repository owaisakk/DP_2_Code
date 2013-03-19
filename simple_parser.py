import struct
import sys

if __name__ == '__main__':
	zero_count = 0
	with open(sys.argv[1],'r') as f:
		f.seek(0)
		while True:
			c = f.read(1)
			if c == '\0':
				zero_count += 1
			else:
				zero_count = 0
			if zero_count == 4:
				break
	
		while True:
			buff = f.read(4)
			if len(buff) != 4:
				break
			fl = struct.unpack_from('<f', bytes(buff))[0]
			print(hex(struct.unpack_from('<I', bytes(buff))[0]))
			print(fl)