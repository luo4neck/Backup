title: 3Body
date: 2014-12-07 21:13:41
category: tech==技术
tags: tech
---

3Body is an independent program aims to simulate 3-body motion. This article will record the progress and fun points of the program. 

The structure of the program is Python but the simulation part is written in C++ to speed up. As a python beginner, hope this program could be a good practice. Following blocks are useful links on different topics, which I am planning to improve my ability in. 


/* ===================== Makefile Related Links ===================== */


/* ===================== Py<->C++ Related Links ===================== */

The default return variable from C function to python is int, if what we want to return is double or something else, where wont show any warning but the result should be wrong. To change this, we have to do something like:

xx.restype = ctypes.c_double // for return value..
xx.argtype = ctypes.c_int // for input argument..
xx.argtypes = ctypes.c_int, ctypes.c_double // for input arguments..

Another point is that the support of long double of Python is poor, I have not actually meet any problem about long double but note this here to keep this in mind.

/* =====================  const   Related Links ===================== */

http://www.cnblogs.com/yc_sunniwell/archive/2010/07/14/1777416.html


/* ===================== C++ file Related Links ===================== */


/* ==================== hexo blog Related Links ===================== */

http://zipperary.com/2013/05/30/hexo-guide-4/


I am still learning how to use hexo lol.

2014 Winter, @Dublin
