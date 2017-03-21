## Set up TensorFlow

### Set up TensorFlow on Windows Machines

The following steps have been tested on Windows 10 computers. 


### 1. Install Anaconda (Python 3.5)

As of March 21, 2017, the most updated Python 3 version is Python 3.6. However, TensorFlow only works directly on Python 3.5. You need to download and install Anaconda (Anaconda3-4.2.0 is for Python 3.5) from the [Anaconda Installer Archive](https://repo.continuum.io/archive/Anaconda3-4.2.0-Windows-x86_64.exe). 

### 2. Run the following command to install TensorFlow

This instruction is based on a thread in [stackoverflow](http://stackoverflow.com/questions/42755129/installing-tensorfow-not-supported-wheel).

		conda create --name tensorflow python=3.5
		activate tensorflow
		conda install jupyter
		conda install scipy
		pip install tensorflow #if you want to run TensorFlow on CPU machines
		# or, run the following command if you want to run TensorFlow on GPU machines
		# pip install tensorflow-gpu

### 3. (Optional) Launch Jupyter Notebook server
	
If you would like to use Jupyter Notebooks to develop your Python scripts, you can launch your Jupyter Notebook server by running the following commands:

		# make a directory to be your home directory of your Jupyter Notebooks
		mkdir C:\DeepLearning
		cd C:\DeepLearning
		<path to your Anaconda3 installation>\Scripts\jupyter notebook

Then, you can access your Jupyter Notebook via a browser using the following url: _**localhost:8888**_

### 4. Test whether your TensorFlow is installed successfully

Run the following Python scripts to test whether your TensorFlow is installed successfully.
 
		import tensorflow as tf
		hello = tf.constant('Hello Hang, Welcome to TensorFlow!')
		sess = tf.Session()
		print(sess.run(hello))

If you see _**b'Hello Hang, Welcome to TensorFlow!'**_ in result, that means your TensorFlow is installed properly. When you run these scripts for the first time, there will be some warnings in your Python console like the following image. No need to worry about them.  

![1](../../media/tensorflow-warning.png)	


