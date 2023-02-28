• A constructor to initialize a vector from a list of values (default to the vector [0,0,0])
• An overloaded str() operator that will format the vector as a list. e.g.,: [v1, v2, v3, ... , vn]
• An accessor method named getValues that will return the vector elements as a list.
• A mutator method named setValues that will take a list argument and update the vector elements
• A method named magnitude that returns a floating-point value representing the magnitude of the vector. The vector magnitude is computed as:
• An overloaded addition (+) operator, __add__, that will return a vector object representing the sum of two vectors. The sum of two vectors is the sum of their respective elements. For example, given two vectors: [a1, a2, a3, ... , an] and [b1, b2, b3, ... , bn] , the sum is: [ a1+b1, a2+b2, a3+b3, ... , an+bn ] If the two vector operands have different sizes, return a vector equal in size to the smaller of the two.  • An overloaded multiplication (*) operator, __mul__, that will return the product of a vector times a scalar value. The product is a vector formed by multiplying each element of the vector argument by the scalar value. Please note that for this problem, the vector must be at the left side of the multiplication (i.e. vector * 3, where 3 is the scalar3, where 3 is the scalar value). 
 → Test your code by creating vector objects. Test all of your functions.

 • An overloaded multiplication (*) operator, __mul__, that will return the product of a vector times a scalar value.
