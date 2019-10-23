package bojSolution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class 게리맨더링_17471 {
	static int N;
	static int[] peopleCount;
	static int[][] map;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[] B = {5,4,4};
		List<int[]> list = new ArrayList<>(Arrays.asList(B));
		System.out.println(list.get(0)[0]);
		N=Integer.parseInt(br.readLine());
		st=new StringTokenizer(br.readLine());
		peopleCount=new int[N];
		for(int i=0;i<N;i++)
			peopleCount[i]=Integer.parseInt(st.nextToken());
		map=new int[N][N];
		
		for(int i=0;i<N;i++) {
			st=new StringTokenizer(br.readLine());
			int num=Integer.parseInt(st.nextToken());
			for(int j=0;j<num;j++) {
				int t=Integer.parseInt(st.nextToken());
				map[i][t-1]=1;
			}
		}
		
		int size = 1<<N;
		int result=Integer.MAX_VALUE;
		for(int i=1;i<size-1;i++) {
			ArrayList<Integer> teamA = new ArrayList<>();
			ArrayList<Integer> teamB = new ArrayList<>();
			for(int j=0;j<N;j++) {
				int reg = (1<<j)&i;
				if(reg>0) {
					teamA.add(j);
				}else {
					teamB.add(j);
				}
			}
//			printMap(teamA);
//			printMap(teamB);
			int resultA=checkEdge(teamA);
			int resultB=checkEdge(teamB);
//			System.out.println(resultA+" "+resultB);
			if(resultA!=-1 && resultB!=-1)
				result=Math.min(result,Math.abs(resultA-resultB));
			
		}
		
		if(result==Integer.MAX_VALUE)
			result=-1;
		System.out.println(result);
		
		
	}
	static void printMap(ArrayList<Integer> temp) {
		for(int i: temp)
			System.out.print(i+" ");
		System.out.println();
	}
	
	static int checkEdge(ArrayList<Integer> temp) {
		boolean[] visit=new boolean[N];
		int line=0;
		if(temp.size()==1)
			return peopleCount[temp.get(0)];
		for(int i=0;i<temp.size();i++) {
			int[] arr=map[temp.get(i)];
//			for(int j=0;j<N;j++) {
//				if(temp.contains(j) && arr[j]==1) {
//					visit[j]=true;
//				}
//			}
			for(int j=0;j<temp.size();j++) {
				if(i==j)
					continue;
				if(arr[temp.get(j)]==1) {
					visit[temp.get(j)]=true;
					line++;
				}
			}
		}
		
		if(line<(temp.size()-1)*2)
			return -1;
//		System.out.println(Arrays.toString(visit));
		int count=0;
		for(int i=0;i<temp.size();i++) {
			if(!visit[temp.get(i)])
				return -1;
			count+=peopleCount[temp.get(i)];
			
		}
		
		
		return count;
	}
	
	
	class Node implements Comparable<Node>{

		@Override
		public int compareTo(Node o) {
			// TODO Auto-generated method stub
			return 0;
		}
		
	}
}
