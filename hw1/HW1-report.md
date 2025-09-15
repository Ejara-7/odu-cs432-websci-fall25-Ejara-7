
# Homework 1 Report - Web Science Intro
Name: Ejara  
Class:CS 432  
Assignment:HW1 - Web Science Intro  
Date: September 14, 2025  


Q1
<img width="521" height="485" alt="image" src="https://github.com/user-attachments/assets/e52eef98-1b27-420d-8e1e-f7688388da60" />


- SCC (Strongly Connected Component): {A, B, C, D, G}  
  These nodes form the “core” where each page can reach every other page.  
- IN: {E, F, M}  
  Nodes that feed into the SCC but are not reachable from it.  
- OUT: {H, L}  
  Nodes reachable from the SCC but that do not link back.  
- Tendrils: {J, N, O}  
  Pages dangling off the structure, not connected directly to the SCC.  
- Tubes: None.  
- Disconnected: {K, I}  
  Nodes that do not connect to the SCC at all.

  
Q2

<img width="1395" height="272" alt="image" src="https://github.com/user-attachments/assets/4e286ace-0001-424b-9402-01c79914db5a" />

B. <img width="1457" height="637" alt="image" src="https://github.com/user-attachments/assets/2e28f047-c4e4-4139-b592-83bfe502978c" />

C. <img width="1471" height="689" alt="image" src="https://github.com/user-attachments/assets/a00ed599-9e31-4280-9486-017d23ba34cb" />

D. <img width="1913" height="919" alt="image" src="https://github.com/user-attachments/assets/bd80375e-c03f-4eed-8bba-07f86995dd31" />

Q3
<img width="1669" height="936" alt="image" src="https://github.com/user-attachments/assets/26d1adb1-4488-4eda-b64b-665e5d7c4760" />

I wrote a single-threaded Python crawler (requests + BeautifulSoup) that does a queue-based BFS with occasional reseeding: 
Start with a seed URL in the queue

Fetch each URL with a 5s timeout and a custom User-Agent ('CS432-collector/1.0 (Ejara-7)'), allowing redirects.

Filter pages: accept only responses whose `Content-Type` includes `text/html` and whose size is **> 1000 bytes** (use `Content-Length` when present, otherwise the actual body length).

Record the final URI** (after any redirects) when a page qualifies.

Extract links** from `<a href>` elements, convert to absolute URLs, normalize (drop `#fragments`, lowercase host, ensure a path), and add unseen links to the BFS queue.

Deduplicate** with a `seen` set; **reseeding**: when the queue gets thin, push a random already-accepted page to keep discovering new sites.

Continue until **500 unique** qualifying URIs are collected; write them to `hw1/collected-uris.txt`.



Refernce:
https://docs.google.com/presentation/d/178GkNtFAPB5fzs1D-wdCnlOdbcTyhpAIz_wKxVUaHVk/edit#slide=id.ga9773ac230_0_799
https://apidog.com/blog/curl-options-request/
https://realpython.com/python-web-scraping-practical-introduction/
https://chatgpt.com/

https://stackoverflow.com/questions/5724985/c-or-python-bruteforcing-to-find-text-in-many-webpages
