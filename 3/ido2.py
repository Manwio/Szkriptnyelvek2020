#!/usr/bin/env python3

import time
start_time=time.time()

def main():
	parts=[]
	for i in range(1,15+1):
		parts.append(str(i))

	res="".join(parts)
	print(res)

	print("---%s seconds ---" %(time.time()-start_time))

if __name__ == "__main__":
    main()
