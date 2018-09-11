import tensorflow as tf

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([4.0, 1.0], name='a')

result = a + b

session = tf.Session()
print(session.run(result))
