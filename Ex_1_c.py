#!/usr/bin/env python

set_password = input('Set your password')
read_password = input('Tell the password you set')

if(set_password != read_password):
    print('Wrong password')
else:
    print('Accept')