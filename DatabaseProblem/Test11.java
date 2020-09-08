package DatabaseProblem;

import java.util.ArrayList;

public class Test11 {
	public static void main(String[] args) {
		int[] arr = {1,1,3,3,0,1,1};
		ArrayList<Integer> answer = new ArrayList<>();
        answer.add(arr[0]);
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        // System.out.println("Hello Java");
        System.out.println(answer.get(0));
        for(int i=1;i<arr.length;i++){
//        	System.out.println(i-1 +" "+i);
            if(answer.get(answer.size()-1)!=arr[i]){
                answer.add(arr[i]);
            }
        }
//        
        int[] ans=new int[answer.size()];
        for(int i=0;i<answer.size();i++) {
        	ans[i]=answer.get(i);
        }
        
        System.out.println(ans);
	}
}
