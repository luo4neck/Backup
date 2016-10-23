title: "Scala Learning Note 1: JVM, JDK, JRE"
date: 2015-06-21 22:16:11
categories: tech==技术
tags: [tech,Scala,Java]
---

Scala is a very powerful and complex language base on JVM. In my previous post ‘Life As Developer’ I mentioned my plan of learning a functional programming language, so Scala is my decision. 

Scala has been installed in Ubuntu in virtual machine, but the study progress is not that perfect. I met some environment setting issues about JDK and JRE (I have no experience about Java, JVM, Eclipse, JDK and JRE), so this post will record the basic concepts about Java environment. 

The graph below shows the relation about the concepts: 
![](/img/jdk01.png)

Java Development Kit (JDK) is an implementation of either one of the Java SE, Java EE or Java ME platforms released by Oracle Corporation in the form of a binary product aimed at Java developers on Solaris, Linux, Mac OS X or Windows. [From Wiki]

Open Java Development Kit (OpenJDK) is a free and open source implementation of the Java Platform, Standard Edition (Java SE). It is the result of an effort Sun Microsystems began in 2006. [From Wiki]

Java virtual machine (JVM) is an abstract computing machine. JVM has its complete virtual hardware structure like processor, stack, heap and register. JVM covers all the details about the OS to run one bytecode on different platforms.
![](/img/jvm01.png)

Java Runtime Environment (JRE) released by Oracle is a software distribution containing a stand-alone Java VM (HotSpot), browser plugin, Java standard libraries and a configuration tool. It is the most common Java environment installed on Windows computers. It is freely available for download at the website java.com. [From Wiki]

HotSpot, released as the "Java HotSpot Performance Engine" is a Java virtual machine for desktops and servers, maintained and distributed by Oracle Corporation. It features techniques such as just-in-time compilation and adaptive optimization designed to improve performance. [From Wiki]
