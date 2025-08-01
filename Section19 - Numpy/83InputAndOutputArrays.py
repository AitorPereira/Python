#Input and Output Arrays
import numpy as np

array1 = np.arange(6)
print (array1)

#To save an array file we will use np.save + filename + array
np.save('array1s',array1)
#To load an array file we will use np.load + filename.npy
np.load('array1s.npy')


array1 = np.arange(6)
print (array1)
array2 = np.arange(8)
print (array2)

#We saved the two different arrays (array1 and array2) in the variable 'arrays'
np.savez('arrays',x=array1,y=array2)

#To load the array saved we will use np.load(filename.npz)
recover_array = np.load('arrays.npz')
#Now to be able to access to the first array or x array
recover_array['x']
#[0 1 2 3 4 5] - It will show the first array
#To recover the second array or y array
recover_array['y']
#[0 1 2 3 4 5 6 7] - It will show the second array


#We also can save the array into a TXT File by using np.savetxt
np.savetxt('myarrayfile.txt', array2, delimiter = ',') #Delimiter is good to declare how the numbers are separated

#To load this TXT File we proceed with np.loadtxt
np.loadtxt('myarrayfile.txt',delimiter=',')
#[0. 1. 2. 3. 4. 5. 6. 7.] - This will return our txtfile as float numbers