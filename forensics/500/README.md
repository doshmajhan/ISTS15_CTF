# Nested

There are 2 password protected zip files which give you access to the final 3rd directory.

The first folder is a password protected zip file and a `A_poem_for_you.txt` file. To get the password from the file you need to use the first letter of every line (it's capitalized and referenced by the zip file name).

In the next folder there is another password protected zip called `Alternative_files` and a `neat.txt` file. To get the password from the `neat.txt` file you need to examine the alternative data stream to find the name of the "hidden" file. This can be accomplished with a simple `DIR /R`.

In the final folder there is a memory dump and a pdf file. There is a TrueCrypt container appended to the PDF file which should be fairly obvious as the PDF is 1GB, and if they check what is running from the memory dump they should see TrueCrypt.

1. They need to extract the TrueCrypt passphrase from the memory dump. This can be done in Volatility with the `truecryptpassphrase` plugin. 

2. Extract the container from the PDF file. Pretty much need to figure out where the PDF file ends (%%EOF) and copy that data to a new folder. (sed '1,/%%EOF/d' top_secret.pdf.bak3 > container11.tc)

3. They will need to load that container with TrueCrypt and unlock it with the password

