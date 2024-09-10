#Day-1 of DSA (10/09/2024)

##Task:

Consider input is s = "leetcode" & k = 3

Now the task is to have substrings from main string based on k value and understand the count of vowels in each substring then return the maximum count of vowels from all substrings

##Output = 2

Explanation: 

    substring1 = "lee" --> 2 Vowels
    substring2 = "tco" --> 1  Vowel
    substring3 = "de"  --> 1 Vowel

So, the max count is 2

##Time Complexity

Loop Over the String:
The loop iterates over each character of the string s, so it runs O(n) times where n is the length of the string s.

Checking for Vowels:
Checking if s[i] is in vowels takes O(1) time because the list vowels has a fixed size of 5.

Appending to the List:
Appending to the list lst inside the loop happens approximately O(n/k) times, where k=3 in this case, making it a linear operation with respect to n.

Calculating the Maximum:
Calculating max(lst) takes O(m) time, where m is the number of elements in lst. Given that there is one element for every k characters in s, this also effectively results in O(n/k) time, which simplifies to O(n).

Overall Time Complexity: The overall time complexity of the function is O(n), where n is the length of the string s.

##Space Complexity

Space for Variables:
count, cnt, and max_vowels use O(1) space.
The list lst stores approximately n/k values, so it takes O(n/k) space, which simplifies to O(n).

Space for Vowels List:
The list vowels is of fixed size (5), so it takes O(1) space.
Overall Space Complexity: The overall space complexity is O(n) due to the list lst.

##Summary
Time Complexity: O(n)
Space Complexity: O(n)