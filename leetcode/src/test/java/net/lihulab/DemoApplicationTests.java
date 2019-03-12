package net.lihulab;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.HashMap;
import java.util.Map;


public class DemoApplicationTests {

	@Test
	public void romanToIntTest() {
		Solution solution = new Solution();
		int num = solution.romanToInt("III");
		System.out.println(num);
	}

}

class Solution {
	public int romanToInt(String s) {
		Map<Character, Integer> romanMap = new HashMap<>();
		romanMap.put('I', 1);
		romanMap.put('V', 5);
		romanMap.put('X', 10);
		romanMap.put('L', 50);
		romanMap.put('C', 100);
		romanMap.put('D', 500);
		romanMap.put('M', 1000);

		int len = s.length();

		int sum = romanMap.get(s.charAt(len-1));
		for (int i = s.length()-2; i > -1 ; i--) {
			if (romanMap.get(s.charAt(i)) < romanMap.get(s.charAt(i+1))) {
				sum -= romanMap.get(s.charAt(i));
			} else {
				sum += romanMap.get(s.charAt(i));
			}
		}

		return sum;
	}
}
