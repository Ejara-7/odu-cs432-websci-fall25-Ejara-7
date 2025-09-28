Name: Ejara
Class: CS 432 Web Science
Assignment: HW2 – Ranking Webpages
Date: 28 september 2025

# Introduction
This assignment ranks webpages for a query. I collect HTML for 500 URIs from HW1, remove boilerplate, and prepare plain text for ranking.

# Q1.  How many of your 500 URIs produced useful text? If that number was less than 500, did that surprise you?
- Processed text files: 500  
- Non-empty processed files: 424  
- Percent non-empty: 84.8%

  it did not really. Several pages yielded little or no extractable text because they were JS-rendered, paywalled/consent-gated, mostly navigation/templates, or returned errors/redirects. Boilerplate removal also discards pages without a dense content block, so fewer than 500 non-empty files is expected.

# Q2  Rank with TF-IDF

 I chose the query term “research.”
This word appeared frequently in my processed documents and was meaningful in the context of academic and informational content, but it was not a stop word (like “the” or “and”). It was also present in many English-language documents from different domains, which made it a strong candidate for TF-IDF analysis.

DF Value from Google

To estimate the document frequency (DF) of “research” on the web, I searched "research" in Google. The search returned about 2,530,000,000 results (≈2.53 billion).
For the total web size, I used the estimate of 40 billion pages (as given in the assignment instructions).

So:

DF_web = 2,530,000,000

Web size = 40,000,000,000

How TF, IDF, and TF-IDF Were Calculated

TF (Term Frequency): number of times “research” appears in a given processed document divided by the total number of words in that document.

IDF (Inverse Document Frequency): calculated with

IDF=log2​(2,530,000,000/40,000,000,000​) = 3.983


TF-IDF: product of TF and IDF.
The top 10 documents ranked by TF-IDF are shown in the table below:
tfidf,tf,idf,term_count,total_words,uri,domain,hash
0.5194944404305796,0.13043478260869565,3.982790709967777,3,23,https://www.odu.edu/research/compliance,www.odu.edu,ebc626a3599999bb60bad601e3bda766
0.39827907099677773,0.1,3.982790709967777,1,10,https://www.catalyzex.com/,www.catalyzex.com,aaac9fd7490854991f26d351e41a772d
0.3017265689369528,0.07575757575757576,3.982790709967777,5,66,https://weiglemc.github.io/schedule/,weiglemc.github.io,efb1f8986c511e32694a7afe8a6a9167
0.17316481347685986,0.043478260869565216,3.982790709967777,6,138,https://vmasc.org/,vmasc.org,13760ff548562c74e4fde68b2d53e842
0.1681389217928349,0.04221635883905013,3.982790709967777,16,379,https://oducsreu.github.io/,oducsreu.github.io,0b264cfb3d135b115c17904f1a23f353
0.1679490058420147,0.04216867469879518,3.982790709967777,7,166,https://ws-dl.blogspot.com/,ws-dl.blogspot.com,1b93e44d4ed9c72553b183ebbf90cc30
0.1587344123537882,0.03985507246376811,3.982790709967777,22,552,https://www.ssrc.org/our-work/,www.ssrc.org,46288f248213c1599b032eefa2ea2514
0.14224252535599202,0.03571428571428571,3.982790709967777,1,28,https://www.cornell.edu/,www.cornell.edu,e801c1834bca3bc5d1999849f649f919
0.1298736101076449,0.03260869565217391,3.982790709967777,30,920,https://www.txyz.ai:443/,www.txyz.ai,cf7fd38edd7b18f59d6d0530712f8856
0.12446220968649303,0.03125,3.982790709967777,6,192,https://www.cs.odu.edu/~mweigle/CS800-S20/,www.cs.odu.edu,d4854e4c84ae901c374d526804464c52
