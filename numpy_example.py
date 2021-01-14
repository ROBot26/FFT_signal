from matplotlib.pyplot import *
import numpy as np
from time import sleep
from random import random
#------------------ Define parameters of three tone pulse

Fs=1000 #sample rate
N=10000 # Number of datapoints

A1=2.        #amplitude
freq1=300.   #freq in Hz
w1=2*np.pi*freq1 #Freq in rad/s

A2=5.        #amplitude
freq2=10.   #freq in Hz
w2=2*np.pi*freq2 #Freq in rad/s

A3=3       #amplitude
freq3=70.   #freq in Hz
w3=2*np.pi*freq3 #Freq in rad/s

#------------------ Create signal to be analyzed
t=np.zeros(N) #time data array
x=np.zeros(N) #amplitude data array

for i in range(N):# generate time waveform
	t[i]=i/Fs #calculate time step
	x[i]=A1*np.sin(w1*t[i])+A2*np.sin(w2*t[i])+A3*np.sin(w3*t[i])+A1*2*random() #3 tone function with noise

data_ex=np.stack([t,x]) #combine arrays
data_ex=data_ex.T # Transpose arrays to run vertically
s=data_ex.shape # Verify shape of array
print(s)

np.savetxt('test_data_np.txt',data_ex) #Create txt file with 3 tone sine function time data

#------------------ Plot data in python

fig=figure() # Create figure for plot comparison

subplot(2,1,1) # Create subplot for original sine data

plot(t,x,'b-') #plot data in subplot
title('Original data from python')

#------------------ Reload text data, plot, and verify

file2=np.loadtxt('test_data_np.txt') # load in previously created file 
print(file2.shape)  #Verify shape of figure 2

subplot(2,1,2) # Create subplot frame for original sine data
plot(file2[:,0],file2[:,1],'r--') #plot data
title('Reloaded data from txt file')
xlabel('Time (s)')

savefig('example_plot_time.png') # Save figure
show() #Show figure in completed format

#------------------ Perform FFT on both sets of data
fig2=figure()


# ----------for data in python
sp = np.fft.fft(x)/len(x) #create FFT. Must be divided by length of input array
end_i=int(len(x)/2) # find end of positive frequency data
sp1=sp[0:end_i]*2 # convert to positive only fft (must be multiplied by 2
freq = np.fft.fftfreq(t.shape[-1],np.absolute(t[1]-t[0])) #create frequency array using time step and array size
freq1=freq[0:end_i] #grab positive frequencies

plot(freq1,np.absolute(sp1),'b-') #plot data in subplot
title('Original data from python') # add title to subplot


# -----------for data from text file
sp = np.fft.fft(file2[:,1])/len(file2[:,1])
end_i=int(len(file2[:,1])/2)
sp2=sp[0:end_i]*2
F_s = np.round(1/(file2[1,0]-file2[0,0]))

freq = np.fft.fftfreq(len(file2[:,0]),np.absolute(t[1]-t[0]))
freq2=freq[0:end_i]

plot(freq2,np.absolute(sp2),'r--') #plot data in subplot
title('Comparison of FFT of python and text file signals')
xlabel('Frequency (Hz)')

legend(['Python','Text file'])
savefig('example_plot_freq.png') # Save figure
show() #Show figure in completed format



