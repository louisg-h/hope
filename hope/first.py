'''
Created on 21 Feb 2018

@author: Louis
'''
import platform

def cpu():
    proc = platform.processor()
    return proc

def os():
    plat = platform.platform()
    return plat

if __name__ == '__main__':
    pass

