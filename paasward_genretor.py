import random
print ' Welcome to the password generator'
print " Which kind of passward you need "
print " 1. Week (easy to remember but risky), 2. Strong (little hard to rember but safer) 3. Vary strong (Hard to rember but full safty of your account and data) "
inp = input(' chose as 1, 2 or 3 ')
numb_var = random.randrange(1,10000, 1)
print numb_var
char_list = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char_chos = random.randrange( 0, 25, 1)
char_var = char_list[char_chos]
sym_list = ['~','`','!','@',"#",'$','%','^','&','*','(',')','_','-','+','=','|',';',':','<','>','/','?']
sym_chose = random.randrange(0, 24, 1)
sym_var = sym_list[sym_chose]
char_chos = random.randrange( 0, 25, 1)
char_var1 = char_list[char_chos]
char_chos = random.randrange( 0, 25, 1)
char_var2 = char_list[char_chos]
char_chos = random.randrange( 0, 25, 1)
char_var3 = char_list[char_chos]
char_chos = random.randrange( 0, 25, 1)
char_var4 = char_list[char_chos]
char_chos = random.randrange( 0, 25, 1)
char_var5 = char_list[char_chos]
char_chos = random.randrange( 0, 25, 1)
char_var6 = char_list[char_chos]
sym_chose = random.randrange(0, 24, 1)
sym_var1 = sym_list[sym_chose]
sym_chose = random.randrange(0, 24, 1)
sym_var2 = sym_list[sym_chose]
sym_chose = random.randrange(0, 24, 1)
sym_var3 = sym_list[sym_chose]
sym_chose = random.randrange(0, 24, 1)
sym_var4 = sym_list[sym_chose]
sym_chose = random.randrange(0, 24, 1)
sym_var5 = sym_list[sym_chose]
sym_chose = random.randrange(0, 24, 1)
sym_var6 = sym_list[sym_chose]
print char_var4 + char_var5 + sym_var2 + sym_var6 + str(numb_var) + char_var + sym_var + char_var1 + char_var2 + char_var3 + char_var4 + char_var5 + char_var6 + sym_var1 + sym_var2 + sym_var3 + sym_var4 + sym_var5 + sym_var6
