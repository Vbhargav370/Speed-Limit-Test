"""
Speed Limit Test
Alice is driving from her home to her office which is A kilometers away and will take her X hours to reach.
Bob is driving from his home to his office which is B kilometers away and will take him Y hours to reach.

Determine who is driving faster. If they are both driving at the same speed, print EQUAL.

Input Format
The first line will contain T, the number of test cases.
The following T lines each contain four integers:
A, X, B, Y, where:
A: Distance Alice travels (in kilometers).
X: Time Alice takes (in hours).
B: Distance Bob travels (in kilometers).
Y: Time Bob takes (in hours).
Output Format
For each test case:

Print ALICE if Alice is faster.
Print BOB if Bob is faster.
Print EQUAL if both are driving at the same speed.
You can print the strings in uppercase or lowercase (for example, equal, EQUAL, eQuAl will all be treated as the same).
"""

for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    print('alice' if a*y > b*x else ('bob' if a*y < b*x else 'equal'))
