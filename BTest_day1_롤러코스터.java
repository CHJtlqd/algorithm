import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class BTest_day1_롤러코스터 {
	static int N;
	static long mod=1000000007;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for(int tc=1;tc<=T;tc++) {
			StringBuffer sb = new StringBuffer();
			sb.append("#").append(tc).append(" ");
			N=Integer.parseInt(br.readLine());
			ArrayList<Node> list = new ArrayList<>();
			for(int i=0;i<N;i++) {
				st=new StringTokenizer(br.readLine());
				int a=Integer.parseInt(st.nextToken());
				int b=Integer.parseInt(st.nextToken());
				list.add(new Node(a,b));
			}
			Collections.sort(list);
			long result=1;
			for(int i=0;i<N;i++) {
				if(result>1000000007) {
					
				}
			}
			System.out.println(sb.toString());
		}
	}
	
	static class Node implements Comparable<Node>{
		int a,b;
		Node(int a,int b){
			this.a=a;
			this.b=b;
		}
		@Override
		public int compareTo(Node o) {
			// TODO Auto-generated method stub
			return (o.a-1)*b<(a-1)*o.b?1:-1;
		}
	}
}
