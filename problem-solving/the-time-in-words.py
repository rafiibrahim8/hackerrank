# https://www.hackerrank.com/challenges/the-time-in-words/problem

num2words = {0:"o' clock", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'quarter', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
            19: 'Nineteen', 20: 'Twenty', 21: 'Twenty One', 22: 'Twenty Two', 
            23: 'Twenty Three', 24: 'Twenty Four', 25: 'Twenty Five',
            26: 'Twenty Six', 27: 'Twenty Seven', 28: 'Twenty Eight', 29: 'Twenty Nine', 30:'half' }

def timeInWordsImpl(h, m):
    if(m==0):
        return num2words.get(h)+' '+num2words.get(m)
    if(m<=30):
        return num2words.get(m)+' minute'+('s' if(m>1) else '')+' past '+num2words.get(h)
    elif(m>30):
        return num2words.get(60-m)+' minute'+('s' if(60-m>1) else '')+' to '+num2words.get(h+1)

def timeInWords(h,m):
    time = timeInWordsImpl(h,m).lower()
    if(m%15==0):
        return time.replace('minutes ','')
    return time

if __name__ == '__main__':
    h = int(input())
    m = int(input())
    print(timeInWords(h,m))
