import pandas as pd


data = ''','First_Name,Last_Name,Company_Name,Address,City,Country,Postal,Phone_1,Email
0,Aleshia,Tomkiewicz,Alan D Rosenburg Cpa Pc,14 Taylor St,St. Stephens Ward,Kent,CT2 7PP,01835-703597,atomkiewicz@hotmail.com
1,Evan,Zigomalas,Cap Gemini America,5 Binney St,Abbey Ward,Buckinghamshire,HP11 2AX,01937-864715,evan.zigomalas@gmail.com
2,France,Andrade,"Elliott, John W Esq",8 Moor Place,East Southbourne and Tuckton W,Bournemouth,BH6 3BE,01347-368222,france.andrade@hotmail.com
3,Ulysses,Mcwalters,"Mcmahan, Ben L",505 Exeter Rd,Hawerby cum Beesby,Lincolnshire,DN36 5RP,01912-771311,ulysses@hotmail.com'''

new = data.split(",")
print(new)
new.append("add this inside the list")
print(new)