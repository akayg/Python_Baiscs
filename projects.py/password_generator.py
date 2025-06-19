import random
import string

try :
    print("Welcome to Random password Generator\n")
    opt1=int(input("Please enter length for your password\n"))
    opt2=input("Do you want to add specical character (yes or no)\n")
    opt3=input("DO you want to add digits (yes or no)\n")
    yeswd=['yes','Yes',"y","YES"]

    if opt1<8:
        print("Password length should be 8 or above")

    elif opt2 in yeswd and opt3 in yeswd:
        spcl=random.choices(string.punctuation,k=int(opt1/4))
        
        nums=random.choices(string.digits,k=int(opt1/3))
        alph=random.choices(string.ascii_letters,k = opt1 - len(nums) -len(spcl))
        all_char=alph + spcl + nums
        random.shuffle(all_char)  # so password isn't predictable like SSSNNNaaa
        print("".join(all_char))

except Exception:
    print("Something went wrong")





# '''| Constant                 | Description                                                            | Example Output                                           |        |
# | ------------------------ | ---------------------------------------------------------------------- | -------------------------------------------------------- | ------ |
# | `string.ascii_lowercase` | All lowercase letters (a–z)                                            | `'abcdefghijklmnopqrstuvwxyz'`                           |        |
# | `string.ascii_uppercase` | All uppercase letters (A–Z)                                            | `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`                           |        |
# | `string.ascii_letters`   | All letters (uppercase + lowercase)                                    | `'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'` |        |
# | `string.digits`          | All digit characters                                                   | `'0123456789'`                                           |        |
# | `string.punctuation`     | All special characters/punctuation                                     | `'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{                        | }\~'\` |
# | `string.hexdigits`       | Hexadecimal digits (0-9, a-f, A-F)                                     | `'0123456789abcdefABCDEF'`                               |        |
# | `string.octdigits`       | Octal digits (0-7)                                                     | `'01234567'`                                             |        |
# | `string.printable`       | All printable characters (digits + letters + punctuation + whitespace) | Letters, digits, punctuation, space                      |        |
# | `string.whitespace`      | All whitespace characters                                              | `' \t\n\r\x0b\x0c'`                                      |        |
# '''
