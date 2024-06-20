**Set 1 - Common Coding Questions**
1.	ASCII Value of a Character
2.	Remove Vowels and Spaces from a String
3.	Remove All Characters Other Than Alphabets
4.	Reverse a String
5.	Sum of Numbers in a String
6.	Capitalize First and Last Character of Each Word
7.	Frequency of Characters in a String
8.	Find Non-Repeating Character
9.	Find Smallest and Largest Word in a String
10.	Check if Strings are Anagrams of Each Other
11.	Sort a String of Characters
12.	Convert Characters of a String to Opposite Case
13.	Count Words in a Given String
14.	Encrypt the String
15.	Remove Duplicates from a Given String
16.	Find Duplicates in the Input String
17.	Find Lexicographically Next String
18.	Remove Brackets from an Algebraic Expression
19.	Check if a String is a Substring of Another
20.	Reverse Words in a Given String

**Set 2 - Array Based Questions**
1.	Find Non-Repeating Element
2.	Program for Array Rotation
3.	Find Equilibrium Index of an Array
4.	Print Array After It Is Right Rotated K Times
5.	Check if an Array is a Subset of Another Array
6.	Find All Symmetric Pairs from a Pair of Arrays
7.	Counting Rock Samples
8.	Reverse an Array or String
9.	Find Mean and Median of an Unsorted Array
10.	Find Smallest and Second Smallest Elements in an Array
11.	Find Largest Element in an Array
12.	Find Second Largest Element in an Array
13.	Count Frequencies of Array Elements
14.	Program for Addition of Two Matrices
15.	Sort a K-Increasing-Decreasing Array
16.	Sum of Elements in a Given Array
17.	Remove Duplicates from a Sorted Array
18.	Program to Check if an Array is Sorted or Not
19.	Remove Duplicates from an Unsorted Array Using Map Data     Structure
20.	Block Swap Algorithm for Array Rotation
21.	Average of an Array (Iterative and Recursive)
22.	Add an Element to an Array
23.	Find Duplicates in O(n) Time and O(1) Extra Space
24.	Find Maximum Possible Stolen Value from Houses
25.	Replace Each Element of the Array with Its Corresponding Rank
26.	Sort Elements by Frequency
27.	Sort an Array According to the Order Defined by Another Array
28.	Find Maximum Product Subarray


**TCS Ninja Questions**
1.	Loops in Python
    ➡️Loops in Python are control flow structures that allow you to execute a block of code repeatedly. There are two main types of loops in Python:

    🍑FOR LOOP
    - Used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object.
    - Syntax: 
        for item in iterable:
            # Code block to be executed
    - Example:
        for i in range(5):
            print(i)
    - This will print numbers from 0 to 4.

    🍑While Loop
    - Continues executing a block of code as long as a condition is true.
    - Syntax:
        while condition:
            # Code block to be executed
    - Example:
        count = 0
        while count < 5:
            print(count)
            count += 1
    - This will print numbers from 0 to 4.

2.	Revoke and Grant in DBMS
    ➡️The GRANT command is used to give specific privileges or permissions to database users or roles.
    -Syntax:
    GRANT privileges ON object TO user;
    -Example:
    GRANT SELECT, INSERT ON employees TO user1;
    -This grants the SELECT and INSERT privileges on the "employees" table to the user named "user1".

    The REVOKE command is used to take away previously granted privileges or permissions from database users or roles.
    -Syntax:
    REVOKE privileges ON object FROM user;
    -Example:
    REVOKE SELECT ON employees FROM user1;
    -This revokes the SELECT privilege on the "employees" table from the user named "user1".

3.	How to Assign an Array in Python
    ➡️In Python, you can assign values to an array using list literals or by creating an array object from the array module. Here's how to do it using list literals:
    -Example:
    my_array = [1, 2, 3, 4, 5]

**TCS Digital Questions**
1.	Where is the Synchronization Keyword Used?
    ➡️In multithreading or parallel programming, multiple threads or processes often access shared resources like variables, data structures, or files concurrently. Without proper synchronization mechanisms, this can lead to race conditions, where the outcome of the program becomes dependent on the timing or interleaving of thread execution, potentially causing unpredictable behavior or data corruption.

    Synchronization keywords or constructs provide a way to coordinate the execution of threads or processes to ensure orderly access to shared resources. They typically involve acquiring locks, semaphores, or other synchronization primitives to enforce mutual exclusion or coordination among threads.

    For example, in Java, the "synchronized" keyword can be used to mark methods or blocks of code, ensuring that only one thread can execute them at a time, thus preventing concurrent access to shared data. In C#, the "lock" keyword is used similarly to synchronize access to critical sections of code. In C or C++, synchronization primitives like mutexes or semaphores are commonly used for achieving thread safety.

    By using synchronization constructs effectively, developers can write concurrent programs that are correct, reliable, and free from race conditions or data corruption issues.

2.	What are Tuples in Python?
    ➡️In Python, tuples are immutable sequences, similar to lists, but with one key difference: once created, tuples cannot be modified. They are defined by enclosing comma-separated values within parentheses `()`.

    Here's a simple example of a tuple:

    my_tuple = (1, 2, 3, 'a', 'b', 'c')

    Tuples can contain elements of different data types, including numbers, strings, and even other tuples or lists.

    You can access elements of a tuple using indexing, just like with lists:

    print(my_tuple[0])  # Output: 1
    print(my_tuple[3])  # Output: 'a'

    Tuples are commonly used for representing fixed collections of items, such as coordinates, database records, or function arguments. They're also often returned by functions to represent multiple values.

    One of the main advantages of tuples over lists is that they are immutable, meaning you can't change the values once they are set. This immutability makes tuples suitable for situations where you want to ensure data integrity or when dealing with data that shouldn't be modified accidentally.

3.	Why Do We Use SQL?
    ➡️SQL is widely used for:
    Retrieving and manipulating data in databases.
    Defining database structure and relationships.
    Enforcing data integrity and security.
    Analyzing and generating reports from data.
    Offering scalability and standardization across different database systems.

4.	Commands in Git
5.	Questions on Project (Video Demo)
6.	Tree and B+ Tree
    ➡️A tree is a hierarchical data structure consisting of nodes connected by edges.
    It consists of a root node, which is the topmost node, and zero or more child nodes connected to it.
    Each node may have zero or more child nodes, forming a tree-like structure.
    Trees are commonly used for organizing hierarchical data, such as directory structures, family trees, and organization charts.
    In computer science, various types of trees are used, including binary trees, AVL trees, red-black trees, and more.
    
    B+ tree is a balanced tree data structure optimized for storing and retrieving large amounts of data efficiently.
    It is similar to a binary search tree but with additional properties that make it suitable for disk-based storage and indexing in databases and file systems.
    In a B+ tree, each node typically contains multiple keys and pointers to child nodes.
    Keys are stored in sorted order within each node, allowing for efficient search and retrieval operations.
    B+ trees maintain balance by ensuring that all leaf nodes are at the same level, which helps in maintaining consistent performance for various operations.
    B+ trees are commonly used for implementing database indexes, where they enable fast access to data based on indexed columns.