s1 = set(map(int, input().split(' ')))
s2 = set(map(int, input().split(' ')))
s = s1 & s2
ns = list(s)
ns.sort()
sns = str(ns)
sns = sns.replace('[', '')
sns = sns.replace(']', '')
sns = sns.replace(',', '')
print(sns)

    
