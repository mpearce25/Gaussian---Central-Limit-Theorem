import random
mean = float(input("Type the Mean and then press enter"))
SD = float(input("Type the Standard Deviation and then press enter"))
sampleSize = float(input("Type the Size of each Sample and then press enter"))
sampleNumber = int(input("Type the Number of Samples and then press enter"))

overallSum = 0
for i in range(0,sampleNumber):
    tempSum = 0;
    for k in range(0,5):
        tempSum += random.gauss(mean,SD)
    overallSum += (tempSum / sampleSize)
    print(tempSum / sampleSize);

print("\n\nThe mean of these samples is:" , overallSum / sampleNumber)
print("This is" , mean- (overallSum / sampleNumber)   , "away fromt the actual mean of" , mean)
          
    
