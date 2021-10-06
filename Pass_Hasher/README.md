Execute
python pass_hasher.py <password> [-t {sha256,sha512,md5}]
※Default hash-type is sha256

Example
$ python pass_hasher.py banana
< hash-type : sha256 >

$ python pass_hasher.py banana -t sha512
< hash-type : sha512 >
