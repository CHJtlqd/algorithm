import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class test {
	static int T, N, res;
	static int[][] mat;
	static int[] people;
	static boolean[] check, xx;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		T = Integer.parseInt(br.readLine());
		for(int test = 1; test <= T; test++) {
			N = Integer.parseInt(br.readLine());
			mat = new int[N][N];
			people = new int[N];
			for(int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j < N; j++) {
					mat[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i < N; i++) {
				people[i] = Integer.parseInt(st.nextToken());
			}
			check = new boolean[N];
			res = Integer.MAX_VALUE;
			dfs(0);
			System.out.println("#"+test+" "+res);
		}//test
		br.close();
	}
	static void dfs(int m) {
		if(m == N) {
			if(chk()) {
				int sum1 = 0, sum2 = 0;
				for(int i = 0; i < N; i++) {
					if(check[i]) {
						sum1 += people[i];
					}
					else {
						sum2 += people[i];
					}
				}
				if(res > Math.abs(sum1 - sum2)) res = Math.abs(sum1 - sum2);
			}
			return;
		}
		check[m] = true;
		dfs(m+1);
		check[m] = false;
		dfs(m+1);
	}
	static boolean chk() {
		xx = new boolean[N];
		ArrayList<Integer> list = new ArrayList<>();
		for(int i = 0; i < N; i++) {
			if(check[i]) {
				list.add(i);
				break;
			}
		}
		if(list.size() == 1) xx[list.get(0)] = true;
		for(int h = 0; h < N; h++) {
			for(int i = 0; i < list.size(); i++) {
				for(int j = 0; j < N; j++) {
					if(mat[list.get(i)][j] == 1 && check[j] && !xx[j]) {
						list.add(j);
						xx[j] = true;
					}
				}
			}
		}
		list = new ArrayList<>();
		for(int i = 0; i < N; i++) {
			if(!check[i]) {
				list.add(i);
				break;
			}
		}
		if(list.size() == 1) {
			xx[list.get(0)] = true;
		}
		for(int h = 0; h < N; h++) {
			for(int i = 0; i < list.size(); i++) {
				for(int j = 0; j < N; j++) {
					if(mat[list.get(i)][j] == 1 && !check[j] && !xx[j]) {
						list.add(j);
						xx[j] = true;
					}
				}
			}
		}
		for(int i = 0; i < N; i++) {
			if(!xx[i]) {
				return false;
			}
		}
		return true;
	}
}
