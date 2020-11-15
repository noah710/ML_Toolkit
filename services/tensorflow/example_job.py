import tensorflow as tf

print("defining tensor constants")
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(5)

print("\n\ndoing some operations")
add = tf.add(a, b)
sub = tf.subtract(a, b)
mul = tf.multiply(a, b)
div = tf.divide(a, b)

print("\nPrinting operation results")
print("add =", add.numpy())
print("sub =", sub.numpy())
print("mul =", mul.numpy())
print("div =", div.numpy())

print("\ndo some reduce operations")
mean = tf.reduce_mean([a, b, c])
sum = tf.reduce_sum([a, b, c])

print("\nPrint reduce operation results")
print("mean =", mean.numpy())
print("sum =", sum.numpy())


print("\nDo some matrix multiplications")
matrix1 = tf.constant([[1., 2.], [3., 4.]])
matrix2 = tf.constant([[5., 6.], [7., 8.]])

product = tf.matmul(matrix1, matrix2)
print("\nPrint matrix operation result")
print(product)
