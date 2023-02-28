##Write a Python program that will allow a user to type in a message (at most a sentence with no punctuation) and convert it into Morse code. Your program must use a dictionary to represent and implement the code. The letters in Morse code are encoded as follows: 
## A . - 
## B -. . . C - . - . D - . . E . F . .  - . G -- . H . . . . I . . J . --- 
## K - . - L . - . . M – <Space>   / 
## N - . O --- P . -- . Q --. - R . - . S . . . T - U . . - V . . . - W . -- 
## X - . . - Y - . -- 
## Z -- . . 
## 
## 
##You may copy and paste the dictionary below. Note that only the first 22 letters have been filled out.  Fill in the rest of the letters. 
## 
##morseDictionary={' ': '/','A': '.-', 'B': '-...','C': '-.-.', 'D': '-..',    'E': '.',  'F': '..-.', 'G': '--.', 'H': '....' 'I': '..', 'J': '.--','K': '-.-','L': '.-..', 'M': '--','N': '-.', 'O': '---', 'P': '.--.',   'Q': '--.-', 'R': '.-.', 'S': '...','T': '-', 'U': '..-','V': '...-'} 
## Example: 
## 
## 
##>>> Enter a message: My TAs are amazing 
## -- -.--  / - .- ... / .- .-. . / .- -- .- --.. .. -. --. 
## 
## 
##Notice that the message is case-insensitive. Like in the example, you may use spaces to separate each letter for readability and recall that you may also need end=' ' to print the message onto a single line.

  

def getMorse(message):
    
    morseDict={' ': '/','A': '.-', 'B': '-...','C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.--','K': '-.-','L': '.-..', 'M': '--','N': '-.', 'O': '---', 'P': '.--.',   'Q': '--.-', 'R': '.-.', 'S': '...','T': '-', 'U': '..-','V': '...-', 'W': '. --', 'X': '- . . -', 'Y': '- . --', 'Z': '-- . .'}
   
    keystring = ' '
    for x in message:
        
        keystring += morseDict[x] + " "
     
     
    return keystring
     

     

def main():
      
        message = input('Enter a message:  ').upper()
     
        print(getMorse(message))

        
main()


