class Solution:
    def numberToWords(self, num: int) -> str:
        
        def to_words(num:int):
            under_twenty =              ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
            tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
            chunk = ['Thousand','Million','Billion']
            if num < 20:return [under_twenty[num]]
            if num < 100: return [tens[num // 10]] + to_words(num % 10)
            if num < 1000: 
                quotient, remainder = num // 100, num % 100
                return [under_twenty[quotient]] + ['Hundred'] + to_words(remainder)
            for power, chunk in enumerate(chunk,1):
                if num < 1000 ** (power + 1):
                    quotient,remainder = num // 1000 ** power , num  % 1000 ** power
                    return to_words(quotient) + [chunk] + to_words(remainder)
        return " ".join(res for res in to_words(num) if res  != "") or 'Zero'