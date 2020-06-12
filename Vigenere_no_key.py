def get_ic(s):
    n=len(s)
    ic=0
    if n-1:ic=(1/(float(n)*(n-1)))*(sum([s.count(a)*(s.count(a)-1) for a in set(s)]))
    return ic

def get_possible_key_ls(avg_ic_arr):
    cpy=avg_ic_arr.copy()
    avg_ic_arr.sort(reverse=True)
    key_ls=[cpy.index(avg_ic_arr[0])+2,cpy.index(avg_ic_arr[1])+2]
    return key_ls

def get_key_len(c,max_guess):
    avg_ic_arr=[]
    for n in range(2,max_guess+1):
        ic_sum=0.0
        avg_ic=0.0
        for i in range(n):
            s=""
            for j in range(0,len(c[i:]),n):
                s+=(c[i:][j])
            ic=get_ic(s)
            ic_sum+=ic
        avg_ic=ic_sum/n
        avg_ic_arr.append(avg_ic)
    pos_key_ls=get_possible_key_ls(avg_ic_arr)
    print("Best two ossible key lengths:",pos_key_ls)
    key_l=int(input("Enter the choice:"))
    if key_l in pos_key_ls: return key_l
    else:
        print("Invalid input !")
        exit()    

def get_chi_square(s):
        s=s.lower()
        e_frq= [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
        expct_count={}
        for each in set(s):
            q=ord(each)-97
            expct_count[each]=e_frq[q]*len(s)
        chi_sqr=sum(((s.count(a)-expct_count[a])**2)/expct_count[a] for a in set(s))
        return chi_sqr

def get_key(c,key_l):
    c=c.lower()
    k_string=""
    for l in range(key_l):
        s=""
        for i in range(l,len(c),key_l):
            s+=c[i]
        pos_sets=[]
        for i in range(26):
            pos_sets.append("".join([chr(((ord(each)-97-i)%26)+97) for each in s]).upper())
        chi_sqr_vals=[]
        for i in range(len(pos_sets)):
            chi_sqr_vals.append(get_chi_square(pos_sets[i]))
        k=chr(chi_sqr_vals.index(min(chi_sqr_vals))+97)
        k_string+=k
    return k_string

def decrypt(k,c):
    k_code=[(ord(a)-97) for a in k]
    dcr_msg_code=[]
    for i in range(len(c)):
        dcr_msg_code.append(((ord(c[i])-97)-k_code[i%len(k)])%26)
    dcr_msg=[chr(a+97) for a in dcr_msg_code]
    return "".join(dcr_msg)

def main():
    f=open('cipherNoKey.txt','r')
    c=f.read().replace(" ","").lower()

    max_guess=int(input("Guess the maximum key length:"))
    while (max_guess>len(c)):
        print("Invalid Guess ! Please try again.")
        max_guess=int(input("Guess the maximum key length:"))
    
    key_l=get_key_len(c,max_guess)
    print("Key length:",key_l)
    
    k=get_key(c,key_l)
    print("Key :",k.upper())
    
    d_opt=input("Do you want to decrypt the message? (y/n)")
    while (d_opt!='y' and d_opt!='n'):
        print("Invalid input ! Please try again.")
        d_opt=input("Do you want to decrypt the message? (y/n)")
    
    if d_opt=='y':
        msg=decrypt(k,c)
        print("Decrypted message:",msg)
    else:
        exit()

if __name__ == '__main__':
    main()
