package DatabaseProblem;


class UserSolution implements Field{
	
	
	
	void InitDB() {
		
	}
	
	void Add(char[] name, char[] number, char[] birthday, char[] email, char[] memo) {
		
	}
	
	int Delete(Field field, char[] str) {
		
		
		
		return 0;
	}
	
	int Change(Field field, char[] str, Field changefield, char[] changestr) {
		
		return 0;
	}
	
	RESULT Search(Field field, char[] str, Field returnfield) {
		return null;
		
	}
	
	
}

class RESULT{
	int count;
	Field field;
	RESULT(int count ,Field field){
		this.count=count;
		this.field=field;
	}
}