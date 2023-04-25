str="hello komal"
print(str.islower())   #output-True...it retun True if all character in given string are lowercase ,else it return False
str="Gita hii"
print(str.islower())   #output-False

str="i want to invite you for Diwali party "
print(str.isprintable())   #output-True..if all values within the given string are printable,else False.
str1="I want to invite you for diwali \n party"
print(str1.isprintable())   #output-false...all values are not printable \n


str="   "       #only if White space will be by using SPACEBAR
print(str.isspace())   #Output-True...else False
str="       "   #only if White space will be by using TAB
print(str.isspace())   #output-True...else False

str="World Health Organisation"
print(str.istitle())   #output-True...if first letter of each word os string is capitalise,else False
str2="Bird is Beautiful"
print(str2.istitle())  #output False

str="KOMAL"
print(str.isupper())   #output-True...if given string is uppercase,else False

str="Ram is a boy."
print(str.replace("Ram", "Gita"))   #it replace the value/word

str="Krishna is a player"
print(str.startswith("Krishna"))    #output-True..if value start with given value,else false

str="Meena is a dancer"
print(str.swapcase())               #conver upeercase to lowercase,vise-versa

str="Rama is god"
print(str.title())                  #capitalise each letter...convert in titlecase

