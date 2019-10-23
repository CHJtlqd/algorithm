package bojSolution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 동전1_2293 {
	static int[] dp= new int[10001];
	static int[] coin = new int[101];
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N=Integer.parseInt(st.nextToken());
		int K=Integer.parseInt(st.nextToken());
		
		for(int i=0;i<N;i++)
			coin[i]=Integer.parseInt(br.readLine());
		dp[0]=1;
		for(int i=0;i<N;i++) {
			
			for(int j=coin[i];j<=K;j++) {
				dp[j]+=dp[j-coin[i]];
			}
		}
		System.out.println(dp[K]);
	}
}
