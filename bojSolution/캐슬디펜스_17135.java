package bojSolution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 캐슬디펜스_17135 {
	static int N, M, D;
	static int[][] map;
	static int size;
	static int result = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		map = new int[N + 2][M + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 1) {
					size++;
				}
			}
		}
		int[] arr = new int[3];
		combi(M, 3, 0, arr, 0);
		System.out.println(result);
	}

	static int calcDist(int x1, int y1, int x2, int y2) {
		return Math.abs(x1 - x2) + Math.abs(y1 - y2);
	}

	static void nextTurn(int[][] temp) {
		for (int i = N; i >= 1; i--) {
			for (int j = 1; j <= M; j++) {
				temp[i][j] = temp[i - 1][j];
			}
		}
	}

	static void combi(int n, int r, int idx, int[] player, int target) {
		if (r == 0) {
			result = Math.max(bfs(player), result);
			return;
		}
		if (target >= n)
			return;
		player[idx] = target;
		combi(n, r - 1, idx + 1, player, target + 1);// 뽑는경우
		combi(n, r, idx, player, target + 1);// 안뽑는경우
	}

	static int[] dirX = { -1, 1, 0, 0 };
	static int[] dirY = { 0, 0, -1, 1 };

	static int bfs(int[] player) {
		int[][] temp = new int[N + 2][M + 1];
		copy(temp);
		int count = 0;
		int huntSize = size;
//		System.out.println(Arrays.toString(player));
		
		for (int turn = 0; turn < N; turn++) {
			ArrayList<Node>[] list = new ArrayList[3];
			for(int i=0;i<3;i++)
				list[i]=new ArrayList<Node>();
			boolean[][] visited;
			for(int k=0;k<3;k++) {
				Queue<Node> queue = new LinkedList<>();
				queue.offer(new Node(N+1,player[k]+1,0));
				visited= new boolean[N+2][M+1];
				visited[N+1][player[k]+1]=true;
				Node qtemp;
				while(!queue.isEmpty()) {
					qtemp=queue.poll();
					if(temp[qtemp.x][qtemp.y]==1)
						list[k].add(qtemp);
					if(qtemp.count==D)
						continue;
					for(int i=0;i<4;i++) {
						int dx=qtemp.x+dirX[i];
						int dy = qtemp.y+dirY[i];
						if(dx<=0 || dy<=0 || dx>N || dy>M || visited[dx][dy])
							continue;
						visited[dx][dy]=true;
						queue.offer(new Node(dx,dy,qtemp.count+1));
					}
					
				}
				Collections.sort(list[k]);
			}
			
			for(int i=0;i<3;i++) {
				if(list[i].size()==0)
					continue;
				if(temp[list[i].get(0).x][list[i].get(0).y]==1) {
					count++;
					temp[list[i].get(0).x][list[i].get(0).y]=0;
				}
			}
			
			
			nextTurn(temp);
		}
		return count;
	}

	static void printMap(int[][] temp) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				System.out.print(temp[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}

	static void copy(int[][] temp) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				temp[i][j] = map[i][j];
			}
		}
	}

	static class Node implements Comparable<Node> {
		int x, y, count;

		Node(int x, int y, int count) {
			this.x = x;
			this.y = y;
			this.count = count;
		}

		@Override
		public int compareTo(Node o) {
			// TODO Auto-generated method stub
			return this.count == o.count ? this.y - o.y : this.count - o.count;
		}
	}

}
