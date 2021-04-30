# have not tested 

import bcrypt
import sys

password = sys.argv[1].encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print('password hash generated')
    print(hashed)
else:
    print('password has generation failed')