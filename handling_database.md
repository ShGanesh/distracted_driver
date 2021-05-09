# HOW TO HANDLE AND PREPARE THE DATABASE THE EASIER WAY (explanation)  
For such a large amount of of files, it is difficult to physically identify and separate them. Luckily, the source has been magnanimous enough to label the pictures for us.  
This file is for us noobs who are new to such things. I hope to make your lives easier.  
The following explanation is for [handling_database.sh](./handling_database.sh). Keep it on hand.  
For my Python homies the code is in [handling_database.py](./handling_database.py). No extra explanation there, so read this first.  

The images were taken from [MRL Eye Dataset](http://mrl.cs.vsb.cz/eyedataset). Kudos to them.   

**DISCLAIMER: For ease I only used s0001-s0014, But I will explain the process for all s0001 to s0036.**  
*directory == folder*   
The bash file is to be created in the directory where all files have been extracted.

## Step 1:  
After unzipping the data we can see that htere are 36 folders which have many .png images each. Lets transfer all those images into a single folder.  

#### Make new directory
Let's make a directory called pics/  
` line 4 `  

#### Move files  
Now, instead of parsing through ALL the directories one by one and cut-pasteing, we shall use one single line of bash code:   
`line 5`  

Explanation:  
> `mv source destination`: Moves files from _Source_ to _Destination_  
> `./s00{01..14}/* ./pics`:   
> > Source:       All ( \* ) files from directory s0001/ to s0036/    
> > Destination:  The pics/ directory we created before  

#### Delete unused stuff
Now that the pics/ directory is full and the original picture holders are empty (u can check using `ls`), we can delete the original directories.  
`line 6`

## Step 2  
Now that the pictures are in one place, we can go ahead and start bifurcating them into opened eye and closed eye.  
These magnanimous people have labelled each image such with parameters that correspond to gender, glasses, eye state, reflection, light conditions, sensor type. (availible in annotation.txt)   
For us, only the "eye state" is important, but you can play with the others too if you want.  
Now, we need to bifurcate these pics according to eye state i.e open and closed.  
#### Make new directory and go to required directory
Let's make two new directoriess:    
`line 7`   
> `mkdir`: Makes directories named after whatever is written after that. Here, 2 strings were written so 2 directories were made.  

GOTO directory pics  
`line 8`

#### Get required pics  
We shall access all images by creating an array of their names  
`line 10`  
> Use the ls command and encapsulate the whole output in ( ). This shall create an array. It can be printed using `echo ${var[@]}`, where 'var' is variable name and '@' means all arguments.  

#### Shift through all pics wrt eye state and move them into respective directories  
`lines 12 to 21`  
>  for image in array:  
>> if 16th character of string(image) == "0": move image to directory closed/  
>> else, if 16th character of string(image) == "1": move image to directory open/  

Now All images with open eyes are in directory open/ and the closed ones are in closed/ .  
Yay!
