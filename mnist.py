from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import sys, getopt

def epochs_of_train(argv):
   result = 5
   try:
      opts, args = getopt.getopt(argv,"he:",["help","epochs="])
   except getopt.GetoptError:
      print ('helper')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('helper')
         sys.exit()
      elif opt in ("-e", "--epochs"):
         result = int(arg)
   return result   

ep = epochs_of_train(sys.argv[1:])
print('run training with epochs ',ep)
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=ep)

model.evaluate(x_test,  y_test, verbose=2)

