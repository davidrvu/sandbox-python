

import tensorflow as tf 
import os

dir_path = os.path.dirname(__file__) #<-- absolute dir the script is in
exported_path= os.path.join(dir_path,  "1515811472")

def main():
    with tf.Session() as sess:
     #load the saved model
     tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING], exported_path)
     #Prepare model input, the model expects a float array to be passed to x
     # check line 28 serving_input_receiver_fn
     #model_input= tf.train.Example(features=tf.train.Features( feature={'x': tf.train.Feature(float_list=tf.train.FloatList(value=[6.4, 3.2, 4.5, 1.5])) })) 

     #model_input= tf.train.Example(features=tf.train.Features( feature={'x': tf.train.Feature(float_list=tf.train.FloatList(value=[5.5,  2.5, 4,   1.3])) })) # output 2 
     model_input= tf.train.Example(features=tf.train.Features( feature={'x': tf.train.Feature(float_list=tf.train.FloatList(value=[6.3,  2.8, 5.1, 1.5])) })) # output 2 


                  #serialized_tf_example = tf.placeholder(dtype=tf.string, shape=[None], name='input_tensors')
                  #receiver_tensors = {'inputs': serialized_tf_example}
                  #feature_spec = {'x': tf.FixedLenFeature([4],tf.float32)}
                  #features = tf.parse_example(serialized_tf_example, feature_spec)
                  #return tf.estimator.export.ServingInputReceiver(features, receiver_tensors)




     #get the predictor , refer tf.contrib.predicdtor
     predictor= tf.contrib.predictor.from_saved_model(exported_path)

     #get the input_tensor tensor from the model graph
     # name is input_tensor defined in input_receiver function refer to tf.dnn.classifier
     #input_tensor=tf.get_default_graph().get_tensor_by_name("input_tensors:0")
     # get the output dict
     # do not forget [] around model_input or else it will complain shape() for Tensor shape(?,) since its of shape(?,) when we trained it
     model_input=model_input.SerializeToString()
     output_dict= predictor({"inputs":[model_input]})
     print(" output_dict = ")
     print(output_dict)
     print(" prediction is " , output_dict['scores'])


if __name__ == "__main__":
    main()