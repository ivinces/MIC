from pyAudioAnalysis import audioTrainTest as aT

aT.featureAndTrain("./Audios/Bosque/",1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "randomforest", "Forest", True)
aT.featureAndTrain("./Audios/Personas/",1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "personas", "Personas", True)
aT.featureAndTrain("./Audios/Amenazas/",1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "AmenazasBP", "Amenazas", True)
