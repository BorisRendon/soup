#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json
import datetime
import sys

def todos():
	paso1()
	paso2()
	paso3()
	paso4()
	
def paso1():
	from paginas import pages
	pages()
	
def paso2():
	from Estudios import estuds
	estuds()
	
def paso3():
	from CS import compsci
	compsci()

def paso4():
	from Directorio import directory
	directory()


def main(args):
    print(args)
    if len(args) == 0:
           todos()
    elif args.__contains__("1"):
        paso1()
    elif args.__contains__("2"):
        paso2() 
    elif args.__contains__("3"):
        paso3()
    elif args.__contains__("4"):
        paso4()

		
if __name__ == "__main__":
    main(sys.argv[1:])



