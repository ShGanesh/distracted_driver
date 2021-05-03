# HOW TO HANDLE AND PREPARE THE DATABASE THE EASIER WAY  
For such a large amount of of files, it is difficult to physically identify and separate them. Luckily, the source has been magnanimous enough to label the pictures for us.  
This file is for us noobs who are new to such things. I hope to make your lives easier.  

The images were taken from [MRL Eye Dataset](http://mrl.cs.vsb.cz/eyedataset).   

**DISCLAIMER: For ease I only used s0001-s0014, But I will explain the process for all s0001 to s0036.**  
*directory == folder*


## Step 1:  
After unzipping the data we can see that htere are 36 folders which have many .png images. Lets transfer all those images into a single folder.  
Let's make a directory called pics/  
```
mkdir pics  
```

Now, instead of going to ALL the directories one by one, we shall use one single line of bash code:  

```
mv ./s00{1..36}/* ./pics
```
Explanation:  
> `mv source destination`: Moves files from _Source_ to _Destination_  
> `./s00{01..14}/* ./pics`:   
> > Source:       All ( \* ) files from directory s0001/ to s0036/    
> > Destination:  The pics/ directory we created before  

Now that the pics/ directory is full and the original picture holders are empty (u can check using `ls`), we can delete the original directories.
```
rmdir s00*
```

## Step 2  
Now that the pictures are in one place, we can go ahead and start bifurcating them into opened eye and closed eye.  
These magnanimous people have labelled each image such with parameters that correspond to gender, glasses, eye state, reflection, light conditions, sensor type. (availible in annotation.txt)   
For us, only the "eye state" is important, but you can play with the others too if you want.  
Now, we need to bifurcate these pics according to eye state i.e open and closed.  
Let's make two new directoriess:  
```
mkdir open closed
```   
> `mkdir`: Makes directories named after whatever is written after that. Here, 2 strings were written so 2 directories were made.  

```
```
