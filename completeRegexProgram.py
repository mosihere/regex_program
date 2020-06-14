
import re
# TODO: Create a Regex for phone Numbers
phoneRegex = re.compile(r'\d{11}')


# TODO: Create a Regex for Email Adresses
emailRegex = re.compile(r'''
# Some.+_thing@(\d{2,5}))?.com

[a-zA-Z-0-9_.+]+        # name  part
@        # @ symbol
[a-zA-Z-0-9_.+]+        # domain name part
''',re.VERBOSE)


# TODO: Copy Your Main Text here
text = '''Hello, My name is Mostafa.
I'm educated in PR I love to coding, ofcourse In python
I have a lil exprience in JavaScript too and also HTML and CSS
So if u need any help please send me an email: mostafakhoshhal@yahoo.com
or call me 09121122345

Hello, My name is Mostafa.
I'm educated in PR I love to coding, ofcourse In Java
I have a lil exprience in Swift too and also HTML and CSS
So if u need any help please send me an email: farolmorris@gmail.com
or call me 09377632357

Hello, My name is Mostafa.
I'm educated in PR I love to coding, ofcourse In Swift
I have a lil exprience in PHP too and also HTML and CSS
So if u need any help please send me an email: keivanmorris@yahoo.com
or call me 09116533457

Hello, My name is Ali.
I'm educated in CS I love to coding, ofcourse In PHP
I have a lil exprience in Python too and also HTML and CSS
So if u need any help please send me an email: aliyari@gmail.com
or call me 09123234334
'''

# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print('\n'.join(extractedPhone))  # Use join and new line for each string to make it beautiful and each number and each email in a single line
print()
print('\n'.join(extractedEmail))

