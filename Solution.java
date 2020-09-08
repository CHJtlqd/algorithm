import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static ArrayList<Pos> island;
	static int T, N, res;
	static int[][] map, dx = {{1,0},{-1,0},{0,1},{0,-1}};
	static boolean[][] check;
	static boolean[] chk;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		Queue<Pos> q;
		int si, sj, ei, ej;
		T = Integer.parseInt(br.readLine());
		for(int test = 1; test <= T; test++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			for(int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			check = new boolean[N][N];
			q = new LinkedList<>();
			Pos p;
			island = new ArrayList<>();
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					if(map[i][j] == 1 && !check[i][j]) {
						si = i;
						sj = j;
						ei = 0;
						ej = 0;
						q.offer(new Pos(si, sj, 0, 0));
						check[i][j] = true;
						while(!q.isEmpty()) {
							p = q.poll();
							if(p.si > ei) ei = p.si;
							if(p.sj > ej) ej = p.sj;
							for(int k = 0; k < 4; k++) {
								if(p.si+dx[k][0]>=0&&p.si+dx[k][0]<N
										&&p.sj+dx[k][1]>=0&&p.sj+dx[k][1]<N
										&&!check[p.si+dx[k][0]][p.sj+dx[k][1]]
										&&map[p.si+dx[k][0]][p.sj+dx[k][1]] == 1) {
									check[p.si+dx[k][0]][p.sj+dx[k][1]] = true;
									q.offer(new Pos(p.si+dx[k][0], p.sj+dx[k][1], 0, 0));
								}
							}
						}
						island.add(new Pos(si, sj, ei, ej));
					}
				}
			}
			chk = new boolean[island.size()];
			res = Integer.MAX_VALUE;
			for(int i = 0; i < island.size(); i++) {
				chk[i] = true;
				dfs(i, 0, 0);
				chk[i] = false;
			}
			if(res == Integer.MAX_VALUE) {
				System.out.println("#"+test+" "+-1);
			}
			else {
				System.out.println("#"+test+" "+res);
			}
		}
		br.close();
	}
	static void dfs(int m, int sum, int l){
		if(l == island.size()-1) {
			if(res > sum) res = sum;
			return;
		}
		Pos p, me;
		int dis=0;
		me = island.get(m);
		for(int i = 0; i < island.size(); i++) {
			if(!chk[i]) {
				p = island.get(i);
				if((p.sj <= me.sj && me.sj <= p.ej)||(p.ej >= me.ej && me.ej >= p.sj)) {
					chk[i] = true;
					if(me.si > p.ei) {
						dis = me.si - p.ei - 1;
					}
					else {
						dis = p.si - me.ei - 1;
					}
					dfs(i, sum + dis, l+1);
					dfs(m, sum + dis, l+1);
					chk[i] = false;
				}
				if((p.si <= me.si && me.si <= p.ei)||(p.ei >= me.ei && me.ei >= p.si)) {
					chk[i] = true;
					if(me.sj > p.ej) {
						dis = me.sj - p.ej - 1;
					}
					else {
						dis = p.sj - me.ej - 1;
					}
					dfs(i, sum + dis, l+1);
					dfs(m, sum + dis, l+1);
					chk[i] = false;
				}
			}
		}
	}
	static class Pos{
		int si;
		int sj;
		int ei;
		int ej;
		public Pos(int si, int sj, int ei, int ej) {
			this.si = si;
			this.sj = sj;
			this.ei = ei;
			this.ej = ej;
		}
	}
}
