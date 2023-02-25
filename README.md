# identityNet2john
Convert standard ASP.Net Identity password hash to crackable by John the ripper

## Examples :
```
$ cat hashtest 
ADTl90+e1OJ5mKcUuhzyaXsm9HZewu2gNz6Uxhs78qhAvKB1mUx1qOp6osDG869jsA==
TestV2:AO7kszlVq1gUsEN6eEwH9WcbppmJlG0qtZpmG65xdklCa89AalTbiA+uXXCOVjzDXw==
TESTv3sha1:AQAAAAAAACcQAAAAEK2sBNc2W0yMEU5Aught4EdkZYUdDop9KaFktpSTzn4h8NRKhNxHAenfMXjDWVbt4Q==
TestV3Sha256:AQAAAAEAACcQAAAAEFWLthQDW2xiWaS3vLgY4ItJdModbW0kzKtb8IVuXBY3fFaIntkbbdqTj8mTXH4mmA==
TestV3Sha256-2:AQAAAAEAACcQAAAAEHD5SVVd00ddYjSXKKfqYnaFHtXMGTzzmblrjFUnJhOaezGt9X+gNmoKfGb06nsriA==
TestV3Sha512:AQAAAAAAACcQAAAAEBk2RpYUWwZiQVEZkm6L0JYMme+0GSinh5HmYD0kbOCRpetfCdSyz099wp5HjRxu/g==

$ john --wordlist=dic hash 
Created directory: /home/kali/.john
Warning: detected hash type "PBKDF2-HMAC-SHA1", but the string is also recognized as "HMAC-SHA256"
Use the "--format=HMAC-SHA256" option to force loading these as that type instead
Warning: detected hash type "PBKDF2-HMAC-SHA1", but the string is also recognized as "HMAC-SHA384"
Use the "--format=HMAC-SHA384" option to force loading these as that type instead
Warning: only loading hashes of type "PBKDF2-HMAC-SHA1", but also saw type "PBKDF2-HMAC-SHA256"
Use the "--format=PBKDF2-HMAC-SHA256" option to force loading hashes of that type instead
Using default input encoding: UTF-8
Loaded 4 password hashes with 4 different salts (PBKDF2-HMAC-SHA1 [PBKDF2-SHA1 256/256 AVX2 8x])
Loaded hashes with cost 1 (iteration count) varying from 1000 to 10000
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 9 candidates left, minimum 16 needed for performance.
TestV3 Sha512    (TestV3Sha512)     
TestV3 Sha1      (TESTv3sha1)     
password         (?)     
test             (TestV2)     
4g 0:00:00:00 DONE (2023-02-25 20:15) 40.00g/s 90.00p/s 360.0c/s 360.0C/s root
Use the "--show --format=PBKDF2-HMAC-SHA1" options to display all of the cracked passwords reliably
Session completed. 
                                                                                                                                                                               $ john --wordlist=dic --format=PBKDF2-HMAC-SHA256 hash 
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (PBKDF2-HMAC-SHA256 [PBKDF2-SHA256 256/256 AVX2 8x])
Cost 1 (iteration count) is 10000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 9 candidates left, minimum 16 needed for performance.
cutecats         (TestV3Sha256)     
TestV3 Sha256    (TestV3Sha256-2)     
2g 0:00:00:00 DONE (2023-02-25 20:16) 28.57g/s 128.5p/s 257.1c/s 257.1C/s root
Use the "--show --format=PBKDF2-HMAC-SHA256" options to display all of the cracked passwords reliably
Session completed. 
```

