A "LookAndSay" sequence generator in python

In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... (sequence A005150 in the OEIS).
To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.
The look-and-say sequence was introduced and analyzed by John Conway.

The idea of the look-and-say sequence is similar to that of run-length encoding.

If we start with any digit d from 0 to 9 then d will remain indefinitely as the last digit of the sequence. For d different from 1, the sequence starts as follows:

d, 1d, 111d, 311d, 13211d, 111312211d, 31131122211d, …

expected output:

print lookandsay(1) --> 1
      
print lookandsay(2) --> 11

print lookandsay(3) --> 21

print lookandsay(4) --> 1211

print lookandsay(5) --> 111221

print lookandsay(4,6) --> 3116
