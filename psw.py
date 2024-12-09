import random
def gen_pass(long):

    caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    psw_generada = ''
    for i in range(long):
        psw_generada += random.choice(caract)
     

    return psw_generada






