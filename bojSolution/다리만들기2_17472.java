package bojSolution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 다리만들기2_17472 {
	static int N, M;
	static int[][] map;
	static boolean[][] visited;
	static int[] dirX = { -1, 1, 0, 0 };
	static int[] dirY = { 0, 0, -1, 1 };
	static ArrayList<bridge> bri = new ArrayList<>();
	static int landCount;
	static boolean[] visitLand;
	static int[] arr;
	static ArrayList<bridge> mst= new ArrayList<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		 N = Integer.parseInt(st.nextToken());
		 M = Integer.parseInt(st.nextToken());

		map = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		visited = new boolean[N][M];
		landCount=0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 1 && !visited[i][j]) {
					bfs(i,j,++landCount);
				}
			}
		}
		arr=new int[landCount];
		for(int i=0;i<landCount;i++)
			arr[i]=i;
//		printLand();
		
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				if(map[i][j]!=0) {
					bridgeInsert(i,j,map[i][j]);
				}
			}
		}

		if(bri.size()==0) {
			System.out.println(-1);
			return;
		}
		Collections.sort(bri);
		while(mst.size() < (landCount-1)) {  
			if(bri.size()==0) {
				System.out.println("-1");
				return;
			}
				
			//V개의 정점을 연결하기 위한 최소간선 갯수는 V-1개인데 아직 그게 안됐으면 계속 하기
				
            bridge edge = bri.get(0);
            bri.remove(0);
//            System.out.println("111111");
            if(edge == null) {
                System.out.println("-1");
                return;
            }
            if(find(edge.startLand-1)!=find(edge.endLand-1)) {
//                System.out.println("22222");
                mst.add(edge);
                union(edge.startLand-1,edge.endLand-1);
            }
        }
		
		int result=0;
		for(int i=0;i<mst.size();i++) 
			result+=mst.get(i).length;
		System.out.println(result);
		

	}
	
	static int find(int n) { // n이속한 집합의 대표를 반환하는 함수
        if (n == arr[n]) {
            return n;
        } else {
            int p = find(arr[n]);
            arr[n]=p;                    //너무많은 재귀호출을 피하기 위해서 최종대표를 저장한다.
            return p;
        }
    }

    static void union(int n1, int n2) { // n1이 속한 집합과 n2가 속한 집합을 통합하는 함수(뒤에놈이 대표가 된다)
        int p1 = find(n1);
        int p2 = find(n2);

        if (p1 != p2) {
            arr[p1]= p2;
        }
    }

	
	static boolean landBri() {
		for(int i=0;i<landCount;i++)
			if(!visitLand[i])
				return false;
		return true;
	}
	
	static void printLand() {
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				System.out.print(map[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println();
	}

	static void bfs(int x, int y, int idx) {
		Queue<Node> queue = new LinkedList<>();
		visited[x][y] = true;
		map[x][y]=idx;
		queue.offer(new Node(x, y,0));
		Node temp;
		while (!queue.isEmpty()) {
			temp = queue.poll();
			for (int i = 0; i < 4; i++) {
				int dx = dirX[i] + temp.x;
				int dy = dirY[i] + temp.y;
				if(dx<0 || dy<0 || dx>=N || dy>=M || visited[dx][dy] || map[dx][dy]==0 )
					continue;
				visited[dx][dy]=true;
				map[dx][dy]=idx;
				queue.offer(new Node(dx,dy,0));
			}
		}
		
	}
	
	static void bridgeInsert(int x,int y,int start) {
		
		for(int i=0;i<4;i++) {
			int dx=x;
			int dy=y;
			int count=0;
			boolean checkOut = false;
			while(true) {
				dx+=dirX[i];
				dy+=dirY[i];
				if(dx<0 || dy<0 || dx>=N || dy>=M || map[dx][dy]==start) {
					checkOut = true;
					break;
				}
				if(map[dx][dy]!=0 )
					break;
				count++;
			}
			if(count>1 && !checkOut) {
				bri.add(new bridge(start, map[dx][dy], count));
			}
			
				
		}
		
	}

	static class Node {
		int x, y,count;

		Node(int x, int y,int count) {
			this.x = x;
			this.y = y;
			this.count=count;
		}

	}
	
	static class bridge implements Comparable<bridge>{
		int startLand,endLand;
		int length;
		
		bridge(int start, int end, int length){
			this.startLand=start;
			this.endLand=end;
			this.length=length;
		}

		@Override
		public int compareTo(bridge o) {
			// TODO Auto-generated method stub
			return this.length-o.length;
		}
	}
}
