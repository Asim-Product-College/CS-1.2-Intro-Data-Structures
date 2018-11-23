# CS 2: Tweet Generator: Text Processing & Probability

## Course Schedule

**Course Dates:** Monday, October 23 – Friday, December 8, 2017 (6 weeks)

**Class Times:** Tuesday & Thursday 2-4pm or 4–6pm (12 class sessions)


| Class |         Date          |                  Topics                  |
|:-----:|:---------------------:|:----------------------------------------:|
|   1   |  Tuesday, October 24  | [Strings & Random Numbers](Class1.md)    |
|   2   | Thursday, October 26  | [Histogram Data Structures](Class2.md)   |
|   3   |  Tuesday, October 31  | [Probability & Sampling](Class3.md)      |
|   4   | Thursday, November 2  | [Flask Web App Development](Class4.md)   |
|   5   |  Tuesday, November 7  | [Application Architecture](Class5.md)    |
|   6   | Thursday, November 9  | [Generating Sentences](Class6.md)        |
|   7   |  Tuesday, November 14 | [Arrays & Linked Lists](Class7.md)       |
|   8   | Thursday, November 16 | [Hash Tables](Class8.md)                 |
|   9   |  Tuesday, November 28 | [Algorithm Analysis](Class9.md)          |
|  10   | Thursday, November 30 | [Higher Order Markov Chains](Class10.md) |
|  11   |  Tuesday, December 5  | [Regular Expressions](Class11.md)        |
|  12   | Thursday, December 7  | Parsing & Tokenization     |


## Repository Setup Instructions

Please follow [these instructions](Setup.md) exactly to set up your fork of this repository.

hash tables- the ultimate data structure
There's usually a hash table implemntation to speden up ur algo
maps keys -> objects
keys are restricted..so u can map something to anythingg(object is anything)
hashtables and maps are not ordered, arrays are not.
For now we'll pretend these things are all the same/

dict() creates a hash table
things in hash table are unordered.
there's no such thing as a first and last in a hash

keys -> buckets
hash function to map them together is not random, it's arbiterry mapping frmo some input to a number
it's deterministic and the same every time.

###hash functions 
variable sized inputs to a fixed size output
same input same outpout

inputs can  be anyhting - string, pointer, custom class

#ideal hash
function range is from 0 to max (4.2 billion...)
*different for cryptographic hash functions
REbeatable, Fast, Unsigned output integer - it's positive or 0
randomly distributes keys among output space.
small differences in input result in large differences in output

which bucket?
assign each key to a speciific lpace in the structure.. how? use built in hash function
in Pyhton - bucket = has(key) % b
has(key) % b this returns the hashcode

imagine b was 10...

#Collisions
what is a hash collisions?
hash collisions? not bc ppl are bad drivers, driving drunk is much worse.
imporrosble to map alll possible input to a fix output space without some inputs generating
the same input.
##differing input genreating the same output is a collision.

nested hash table?
prollem cuz u can't sit on ppls laps iwthout being real clever about it, what if you had stacking
bunk chairs? - #CHAINING these are just linked list!

store key and value together. - use a TUPLE to do this.