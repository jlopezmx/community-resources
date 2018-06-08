## Software Development Online Resources

* Programming
  * [Code Style Template](#code-style-template)
* Devops
* IT Management
* Professional Advice
* Web Security


## CODE STYLE TEMPLATE
<a name="code-style-template"></a>
This document attempts to explain the basic styles and patterns used in the codebase. 

New code should try to conform to these standards, so it is as easy to maintain as existing code. 

There are exceptions, but it's still important to know the rules.

This article is particularly for those new to the Ajolote's codebase, and in the process of getting their code reviewed. 

Before requesting a review, please read over this document, making sure that your code conforms to recommendations.

### CODING STYLES NAVIGATION

[1. GENERAL PRACTICES](#GENERAL-PRACTICES)

[2. FILE NAMING](#FILE-NAMING)

---

<h4 id="GENERAL-PRACTICES">1. GENERAL PRACTICES</h4>

- Don't put an else right after a return (or a break).
  
  Delete the else, it's unnecessary and increases indentation level.
  

- Don't leave debug information lying around.


- Use Unix-style carriage returns ("\n"), rather than Windows/DOS ones ("\r\n").

  You can convert patches, with DOS newlines to Unix via the 'dos2unix' utility, or your fa vorite text editor.

- Use 4 spaces for indentation.

- When fixing a problem, check to see if the problem occurs elsewhere and fix it everywhere if possible. 

<h4 id="FILE-NAMING">2. FILE NAMING</h4>

- For new files, be sure to use meaningful names.

  Do not use generic names that lead to confusion
  
  ###### NAMING CONVENTION EXAMPLE
  >Do not use test.java. File name is not descriptive on what it is testing. Use testUser.java instead.
  
- Without exception lowercase file extensions.

  Upper case characters in file extensions lead to FILE NOT EXIST errors on case-senstive file systems (e.g Linux AMI)  

#### ABOUT
* Version: 1.0.0 
* [Jaziel Lopez](mailto:juan.jaziel@gmail.com), June 2018 
---

<strong>Contact</strong><br/>
Jaziel Lopez, Software Developer <br/>
<a href="mailto:juan.jaziel@gmail.com">Email</a> | <a href="http://jlopez.mx" target="_new" title="Portfolio">Website</a><br/>
Tijuana Area, Mexico
