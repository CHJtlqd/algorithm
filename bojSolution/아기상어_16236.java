package bojSolution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 아기상어_16236 {
	static int N;
	static int[][] map;
	static Shark baby;
	static ArrayList<Shark> pq = new ArrayList<>();
	static int eatCount=2;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N+10][N+10];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if(map[i][j]==9) {
					baby=new Shark(i,j,2);
				}else if(map[i][j]!=0) {
					pq.add(new Shark(i,j,map[i][j]));
				}
			}
		}
		len=N*N;
		Collections.sort(pq);
		int result=0;
		int size=pq.size();
		while(true) {
			boolean eat=false;
			for(int i=0;i<pq.size();i++) {
				Shark temp=pq.get(i);
				if(temp.size>=baby.size) {
					continue;
				}else {
					int nLen=temp.dist();
					if(nLen==N*N)
						continue;
					result+=nLen;
					map[baby.x][baby.y]=0;
					eatCount--;
					if(eatCount==0) {
						baby.size+=1;
						eatCount=baby.size;
					}
					map[temp.x][temp.y]=9;
					baby.x=temp.x;
					baby.y=temp.y;
					pq.remove(i);
					Collections.sort(pq);
					eat=true;
					break;
				}
				
			}
			if(!eat)
				break;
			
//			printMap();
		}
		System.out.println(result);
	}

	static int[] dirX = { -1, 1, 0, 0 };
	static int[] dirY = { 0, 0, -1, 1 };
	static void printMap() {
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				System.out.print(map[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println();
	}
	static int len;
	static class Shark implements Comparable<Shark>{
		int x, y;
		int size;
		int idx;
		int count;

		Shark(int x, int y, int size) {
			this.x = x;
			this.y = y;
			this.size = size;
		
		}

		int dist() {
			if (this.size >= baby.size)
				return N * N;
			Queue<Shark> queue = new LinkedList<>();
			boolean[][] visited = new boolean[N][N];
			visited[baby.x][baby.y] = true;
			queue.offer(new Shark(baby.x, baby.y, baby.size));
			queue.peek().count=0;
			Shark temp;
			while (!queue.isEmpty()) {
				temp = queue.poll();
				if(temp.x==this.x && temp.y==this.y) {
					return temp.count;
				}
				
				for(int i=0;i<4;i++) {
					int dx = temp.x+dirX[i];
					int dy = temp.y+dirY[i];
					if(dx<0 || dy<0 || dx>=N || dy>=N || visited[dx][dy] ||map[dx][dy]>baby.size)
						continue;
					visited[dx][dy]=true;
					Shark t = new Shark(dx,dy,temp.size);
					t.count=temp.count+1;
					queue.offer(t);
				}
			}
			return N * N;
		}

		@Override
		public int compareTo(Shark o) {
			// TODO Auto-generated method stub
			
			return this.dist()==o.dist()?(this.x==o.x?this.y-o.y:this.x-o.x):this.dist()-o.dist();
		}
	}
}
