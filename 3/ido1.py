#!/usr/bin/env python3

import time
start_time=time.time()

def main():
	res=""
	for i in range(1,15+1):
		res+=str(i)
	print(res)

	print("---%s seconds ---" %(time.time()-start_time))

if __name__ == "__main__":
    main()
