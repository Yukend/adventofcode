------------part1----------------
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the 
dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping 
paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also 
need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of 
slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of 
slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

------------part2----------------
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or 
nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or
 aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or
 even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one
 letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the
 letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?