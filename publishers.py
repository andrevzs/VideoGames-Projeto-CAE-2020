import pandas as pd

csv = pd.read_csv('VideoGames.csv', sep=',')

pubs = []

for i in range(len(csv)):
    linha = csv.iloc[i]
    p = linha['Publisher']

    if p in pubs:
        pass
    else:
        pubs.append(p)

pubs = list(set(pubs))

print(*pubs, sep='\n')
