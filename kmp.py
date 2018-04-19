class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0] 
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial(P), [], 0
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = 0
        return ret
		
k = KMP()
s = 'aababcabcdabcdeabcdef'
n = 'abcdeab'
next = k.partial(n)
status = k.search(s,n)
print next
print status

void getNext(char a[], int n, int next[]){
	int i, j;
	i = 0;
	next[0] = -1;#首元跳转值为-1
	j = -1;
	#递推得到next表中剩余值
	while(i < n){
		if(j == -1 || a[i] == a[j]){
			++i;
			++j;
			next[i] = j;
		}
		else{
			j = next[j];
		}
	}
}

def p(str):
	s = str
	length = len(str)
	k = -1 
	j = 0
	next = [0]*length
	next[0] = -1
	while j <length -1:
		if s[j] == s[k] or k == -1:
			if s[j=j+1] == s[k=k+1]:
				next[j] = next[k]
			else:
				next[j] = k
		else:
			k = next[k]
	return next
ss = 'abcdeab'
print p(ss)

 

		

		