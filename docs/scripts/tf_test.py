import tensorflow as tf

print("Tensorflow version:", tf.__version__)

print("GPU available:", tf.test.is_gpu_available())
print()

print("GPUs:")
gpus = tf.config.list_physical_devices('GPU')
for gpu in gpus:
    print("Name:", gpu.name, "  Type:", gpu.device_type)
print()

with tf.device('/gpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    print("TNA=", a)
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    print("TNB=", b)
    c = tf.matmul(a, b)
    print("TNAxTNB=", c)
