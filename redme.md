# Project for Distributed systems


## How to run the project

1) virtualenv env
2) source env/bin/activate
3) pip install -r requirements.txt



## A simple Blockchain

We will see a simple implementation of blockchain, in a local way, without the help of a database, then it will simply be working with an object and the moment the program stops running, the information is deleted.


## Test its operation
It will work with three simple routes, for those who want to try, it would be like this from some HTTP client like insomnia:

http://192.168.1.125:5001/break_chain

http://192.168.1.125:5001/is_valid

http://192.168.1.125:5001/get_chain

http://192.168.1.125:5001/mine_block

### Creditos
- create by Carlos Andres Moreno Alvarez
- in based to Eric el Nomada