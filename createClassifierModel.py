from pyAudioAnalysis import audioTrainTest as aT


subdirectories = ["amenaza/disparos","amenaza/incendio","amenazas/tala"]

print(subdirectories)
aT.featureAndTrain(subdirectories, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel", False)
