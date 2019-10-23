package bojSolution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 테트로미노_14500 {
	static int N, M;
	static int[][] map;
	static int result;
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
		visited=new boolean[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
//					bfs(i,j);
				visited[i][j]=true;
				dfs(i,j,1,map[i][j],i,j);
				visited[i][j]=false;
			}
		}
		System.out.println(result);

	}

	static int[] dirX = { -1, 1, 0, 0 };
	static int[] dirY = { 0, 0, -1, 1 };
	static boolean[][] visited;
	static void bfs(int x, int y) {
		visited[x][y] = true;
		Queue<Node> queue = new LinkedList<>();
		queue.offer(new Node(x, y, 1, map[x][y]));
		Node temp;
		while (!queue.isEmpty()) {
			temp = queue.poll();
			if (temp.count == 4) {
				result = Math.max(result, temp.sum);
				continue;
			}
			// 凸모양 검사
			if (temp.count == 3) {
				// 오른쪽
				if (temp.y == y + 2) {
					if (temp.x - 1 >= 0) {
						result = Math.max(result, temp.sum + map[temp.x - 1][y + 1]);
					} else if (temp.x + 1 < N) {
						result = Math.max(result, temp.sum + map[temp.x + 1][y + 1]);
					}
				} else if (temp.y == y - 2) {// 왼쪽
					if (temp.x - 1 >= 0) {
						result = Math.max(result, temp.sum + map[temp.x - 1][y - 1]);
					} else if (temp.x + 1 < N) {
						result = Math.max(result, temp.sum + map[temp.x + 1][y - 1]);
					}
				} else if (temp.x == x + 2) {// 아래
					if (temp.y - 1 >= 0) {
						result = Math.max(result, temp.sum + map[x + 1][temp.y - 1]);
					} else if (temp.y + 1 < M) {
						result = Math.max(result, temp.sum + map[x + 1][temp.y + 1]);
					}
				} else if (temp.x == x - 2) {// 위
					if (temp.y - 1 >= 0) {
						result = Math.max(result, temp.sum + map[x - 1][temp.y - 1]);
					} else if (temp.y + 1 < M)
						result = Math.max(result, temp.sum + map[x - 1][temp.y + 1]);
				}
			}

			// 4칸까지 탐색
			for (int i = 0; i < 4; i++) {
				int dx = temp.x + dirX[i];
				int dy = temp.y + dirY[i];
				if (dx < 0 || dy < 0 || dx >= N || dy >= M || visited[dx][dy])
					continue;
				visited[dx][dy] = true;
				queue.offer(new Node(dx, dy, temp.count + 1, temp.sum + map[dx][dy]));
			}
		}
	}
	static void printMap() {
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				System.out.print(visited[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println();
	}
	static void dfs(int x, int y , int depth, int sum, int sx, int sy) {
//		System.out.println(sx+" "+sy+" "+result);
		if(depth==4) {
			result=Math.max(result, sum);
			return;
		}else if(depth==3) {
			if (y == sy + 2) {//오른쪽
//				printMap();
//				System.out.println(sum);
				if (x - 1 >= 0) {
					result = Math.max(result, sum + map[x - 1][sy + 1]);
				}  if (x + 1 < N) {
					result = Math.max(result, sum + map[x + 1][sy + 1]);
				}
			} else if (y == sy - 2) {// 왼쪽
				if (x - 1 >= 0) {
					result = Math.max(result, sum + map[x - 1][sy - 1]);
				}  if (x + 1 < N) {
					result = Math.max(result, sum + map[x + 1][sy - 1]);
				}
			} else if (x == sx + 2) {// 아래
				if (y - 1 >= 0) {
					result = Math.max(result, sum + map[sx + 1][y - 1]);
				}  if (y + 1 < M) {
					result = Math.max(result, sum + map[sx + 1][y + 1]);
				}
			} else if (x == sx - 2) {// 위
				if (y - 1 >= 0) {
					result = Math.max(result, sum + map[sx - 1][y - 1]);
				}  if (y + 1 < M)
					result = Math.max(result, sum + map[sx - 1][y + 1]);
			}
		}
		
		for(int i=0;i<4;i++) {
			int dx = x + dirX[i];
			int dy = y + dirY[i];
			if (dx < 0 || dy < 0 || dx >= N || dy >= M || visited[dx][dy])
				continue;
			visited[dx][dy]=true;
			dfs(dx,dy,depth+1,sum+map[dx][dy],sx,sy);
			visited[dx][dy]=false;
		}
	}

	static class Node {
		int x, y, count, sum;

		Node(int x, int y, int count, int sum) {
			this.x = x;
			this.y = y;
			this.count = count;
			this.sum = sum;
		}
	}
}
