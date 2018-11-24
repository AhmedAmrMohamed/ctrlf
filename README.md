# ctrlf
A better solution to find files/directories on your computer uesing their name or regular expression

# Install
`pip install ctrlf`
# Simplest usage
an example for the simplest usage is `ctrfl -o "jpg"`.  
this will open a text file with the name of every file/directory that has the word jpg in it and where it's located.  
also you can use regular expression as a patter to search for.  

# even more
 1. you can specify from what directory you want the search to begin.
 2. you can set which pattern to neglect during the search.

    
      `ctrlf -o <match_pattern> <path> `   
      :: find all that matches a <match_pattern> in <path> if <path> is not given the current directory is used


      `ctrlf -d <match_pattern> <reject_pattern <path>`  
      :: find all that matches a <match_pattern> in <path> and doesnot match  
         <reject_pattern> if <path> is not given the current directory is

      `ctrlf -h`  
      :: show this help message
