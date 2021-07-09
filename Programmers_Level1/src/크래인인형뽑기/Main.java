package 크래인인형뽑기;

import java.util.Stack;

public class Main {

	
	public static void main(String[] args) {

		int board[][]  = {
				{0,0,0,0,0},
				{0,0,1,0,3},
				{0,2,5,0,1},
				{4,2,4,4,2},
				{3,5,1,3,1},
		};
		int moves[]= {1,5,3,5,1,2,1,4};
		Stack<Integer> basket  = new Stack<>();
		int cnt = 0;
		for(int move:moves) {
			for(int j=0;j<board.length;j++)
				if(board[j][move-1]!=0) {
					if(basket.empty()){
						basket.push(board[j][move-1]);
                    }
					else {
						if(basket.peek()==board[j][move-1]) {
							cnt+=2;
							basket.pop();
						}
                        else{
                            basket.push(board[j][move-1]);
                        }
					}
					board[j][move-1]=0;
					break;
				}
			
		}
		System.out.print(cnt);
	}

}
