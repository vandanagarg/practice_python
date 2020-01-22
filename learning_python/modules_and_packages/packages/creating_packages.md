#Creating our own modules and packages

* modules are just .py scripts that we call in another .py script.
* packages are a collection of modules.

**There is a \_\_init\_\_.py script that needs to be placed inside a folder so that python know that this collection of .py scripts needs to be treated as an entire package.**

* Whenever we need to use a file as package we must have \_\_init\_\_.py script inside the folder. This is a empty file.
* While calling a subpackage we need top use (.) dot operator.

* Also below is a very useful and important condition which is used in most of the programs. 

  It can be used as per the requirement but it checks if a program is run directly or is imported and then run.
  
  By default python assigns a string `__main__` in inbuilt variable `__name__` whenever we run a python file.

 `if __name__ == "__main__" : ` -- if true, means a python file is run directly.
 
    