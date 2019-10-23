import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BDay3 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb;
		String s,p;
		int T=Integer.parseInt(br.readLine());
		for(int tc=1;tc<=T;tc++) {
			sb=new StringBuffer();
			sb.append("#"+tc).append(" ");
			s=br.readLine();
			p=br.readLine();
			int result=KMP(s.toCharArray(),p.toCharArray());
			sb.append(result);
			System.out.println(sb.toString());
		}
	}
	
	static int KMP(char[] orin,char[] pattern) {
		int count=0;
		int[] pi=getPi(pattern);
		int strSize=orin.length;
		int j=0,n=pattern.length;
		
		for(int i=0;i<strSize;i++) {
			while(j>0 && orin[i]!=pattern[j])
				j=pi[j-1];
			
			if(orin[i]==pattern[j]) {
				if(j==n-1) {
					count++;
					j=pi[j];
				}
				else {
					j++;
				}
			}
		}
		
		
		
		return count;
	}
	
	static int[] getPi(char[] p) {
		int size=p.length;
		int[] pi=new int[size];
		int j=0;
		for(int i=1;i<size;i++) {
			while(j>0 && p[i]!= p[j])
				j=pi[j-1];
			if(p[i]==p[j])
				pi[i]=++j;
		}
		
		
		return pi;
	}
}
