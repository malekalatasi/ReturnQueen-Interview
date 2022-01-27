import json

def phrasel_search(P, Queries):
    # Write your solution here
    Q = []
    ph = []
    ans = []
    c = 0
    v = []
    qans = ""
    addtoValue = []
    phrases = dict()
    for i in P:
        ph = i.split()
        addtoValue.append(ph[1:])
        if ph[0] in phrases:
            addtoValue = phrases.get(ph[0])
            addtoValue.append(ph[1:])
            phrases[ph[0]] = addtoValue
        phrases[ph[0]] = addtoValue
        addtoValue = []
    for i in Queries:
        Q = i.split()
        ans1=[]
        for j in range(0, len(Q)):
            if Q[j] in phrases:
                error = 1
                allValue = phrases.get(Q[j])
                for a in range(0, len(allValue)):
                    value = allValue[a]
                    c = j+1
                    qans = Q[j]
                    if c < len(Q)-1:
                        for k in range(0, len(value)):
                            if value[k] == Q[c] and error > 0:
                                qans= qans + ' ' + Q[c]
                                c+=1
                            elif value[k] == Q[c] and error == 0:
                                qans= qans + ' ' + Q[c]
                                c+=1
                            elif value[k] != Q[c] and error > 0:
                                qans= qans + ' ' + Q[c]
                                error-=1
                                c+=1
                                if k == len(value)-1:
                                    if value[k] == Q[c]:
                                        qans= qans + ' ' + Q[c]
                            elif value[k] != Q[c] and error == 0:
                                qans = ''
                                break
                        if qans:
                            ans1.append(qans)

        ans.append(ans1)
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
