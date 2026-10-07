from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import os
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import webbrowser
import pickle
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
import keras
from keras import layers
from keras.models import model_from_json
from keras.utils.np_utils import to_categorical
from keras.models import Model
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import to_categorical
import os
import pickle
from sklearn.model_selection import train_test_split

global filename, autoencoder, decision_tree, dnn, encoder_model, pca
global X,Y
global dataset
global accuracy, precision, recall, fscore, vector
global X_train, X_test, y_train, y_test, scaler
labels = ['Normal', 'Naive Malicious Response Injection (NMRI)', 'Complex Malicious', 'Response Injection (CMRI)', 'Malicious State Command Injection (MSCI)',
          'Malicious Parameter Command Injection (MPCI)', 'Malicious Function Code Injection (MFCI)', 'Denial of Service (DoS)']

main = tkinter.Tk()
main.title(" Cyber Attack Detection  ") #designing main screen
main.geometry("1300x1200")

 
#fucntion to upload dataset
def uploadDataset():
    global filename, dataset
    text.delete('1.0', END)
    filename = filedialog.askopenfilename(initialdir="Dataset") #upload dataset file
    text.insert(END,filename+" loaded\n\n")
    dataset = pd.read_csv(filename) #read dataset from uploaded file
    text.insert(END,"Dataset Values\n\n")
    text.insert(END,str(dataset.head()))
    text.update_idletasks()
    unique, count = np.unique(dataset['result'], return_counts=True)

    height = count
    bars = labels
    print(height)
    print(bars)
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.xticks(rotation=90)
    plt.title("Various Cyber-Attacks Found in Dataset") #plot graph with various attacks
    plt.show()
    
    
def preprocessing():
    text.delete('1.0', END)
    global dataset, scaler, X, Y, X_train, X_test, y_train, y_test
    dataset.fillna(0, inplace=True)
    scaler = MinMaxScaler()
    
    # Fit and save new scaler to avoid version mismatch issues
    X = dataset.iloc[:, :-1].values
    scaler.fit(X)
    with open('model/minmax.txt', 'wb') as file:
        pickle.dump(scaler, file)
    
    Y = dataset.iloc[:, -1].values
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    X, Y = X[indices], Y[indices]
    Y = to_categorical(Y)
    X = scaler.transform(X)
    
    text.insert(END, "Dataset after features normalization\n\n")
    text.insert(END, str(X) + "\n\n")
    text.insert(END, "Total records found in dataset : " + str(X.shape[0]) + "\n")
    text.insert(END, "Total features found in dataset: " + str(X.shape[1]) + "\n\n")
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

def calculateMetrics(algorithm, predict, y_test):
    a = accuracy_score(y_test,predict)*100
    p = precision_score(y_test, predict,average='macro') * 100
    r = recall_score(y_test, predict,average='macro') * 100
    f = f1_score(y_test, predict,average='macro') * 100
    accuracy.append(a)
    precision.append(p)
    recall.append(r)
    fscore.append(f)
    text.insert(END,algorithm+" Accuracy  :  "+str(a)+"\n")
    text.insert(END,algorithm+" Precision : "+str(p)+"\n")
    text.insert(END,algorithm+" Recall    : "+str(r)+"\n")
    text.insert(END,algorithm+" FScore    : "+str(f)+"\n\n")

def runAutoEncoder():
    text.delete('1.0', END)
    global X_train, X_test, y_train, y_test, X, Y
    global autoencoder
    global accuracy, precision, recall, fscore
    accuracy = []
    precision = []
    recall = []
    fscore = []
    if os.path.exists("model/encoder_model.json"):
        with open('model/encoder_model.json', "r") as json_file:
            loaded_model_json = json_file.read()
            autoencoder = model_from_json(loaded_model_json)
        json_file.close()
        autoencoder.load_weights("model/encoder_model_weights.h5")
        autoencoder._make_predict_function()
    else:
        encoding_dim = 256 # encoding dimesnion is 32 which means each row will be filtered 32 times to get important features from dataset
        input_size = keras.Input(shape=(X.shape[1],)) #we are taking input size
        encoded = layers.Dense(encoding_dim, activation='relu')(input_size) #creating dense layer to start filtering dataset with given 32 filter dimension
        decoded = layers.Dense(y_train.shape[1], activation='softmax')(encoded) #creating another layer with input size as 784 for encoding
        autoencoder = keras.Model(input_size, decoded) #creating decoded layer to get prediction result
        encoder = keras.Model(input_size, encoded)#creating encoder object with encoded and input images
        encoded_input = keras.Input(shape=(encoding_dim,))#creating another layer for same input dimension
        decoder_layer = autoencoder.layers[-1] #holding last layer
        decoder = keras.Model(encoded_input, decoder_layer(encoded_input))#merging last layer with encoded input layer
        autoencoder.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])#compiling model
        hist = autoencoder.fit(X_train, y_train, epochs=300, batch_size=16, shuffle=True, validation_data=(X_test, y_test))#now start generating model with given Xtrain as input 
        autoencoder.save_weights('model/encoder_model_weights.h5')#above line for creating model will take 100 iterations            
        model_json = autoencoder.to_json() #saving model
        with open("model/encoder_model.json", "w") as json_file:
            json_file.write(model_json)
        json_file.close
    print(autoencoder.summary())#printing model summary
    predict = autoencoder.predict(X_test)
    predict = np.argmax(predict, axis=1)
    testY = np.argmax(y_test, axis=1)
    calculateMetrics("AutoEncoder", predict, testY)
    
def runDecisionTree():
    global autoencoder, decision_tree, encoder_model, vector
    global X_train, X_test, y_train, y_test, X, Y, pca

    encoder_model = Model(autoencoder.inputs, autoencoder.layers[-1].output)#creating autoencoder model
    vector = encoder_model.predict(X)  #extracting features using autoencoder
    pca = PCA(n_components = 7) #applying PCA for features reduction
    vector = pca.fit_transform(vector)
    Y1 = np.argmax(Y, axis=1)
    X_train, X_test, y_train, y_test = train_test_split(vector, Y1, test_size=0.2)
    decision_tree = DecisionTreeClassifier() #defining decision tree
    decision_tree.fit(vector, Y1) #training with decision tree
    predict = decision_tree.predict(X_test)
    text.insert(END,"Decision Tree Trained on New Features Extracted from AutoEncoder\n")
    calculateMetrics("Decision Tree", predict, y_test)


def runMLP():
    global autoencoder, decision_tree, encoder_model, dnn, vector
    global X_train, X_test, y_train, y_test, X, Y
    attack_type = []
    for i in range(len(vector)):
        temp = []
        temp.append(vector[i])
        attack = decision_tree.predict(np.asarray(temp)) #using decision tree we are predicting attack type
        attack_type.append(attack[0])
    attack_type = np.asarray(attack_type)
    X_train, X_test, y_train, y_test = train_test_split(vector, attack_type, test_size=0.2)
    dnn= KNeighborsClassifier()
    #dnn = MLPClassifier() #defining DNN algorithm
    dnn.fit(vector, attack_type) #train DNN with various attack type
    predict = dnn.predict(X_test) #predict label forr unknown attack
    text.insert(END,"Attack Prediction using DNN\n")
    calculateMetrics("MLP", predict, y_test)


def runLSTM():
    global vector, decision_tree,lstm_model
    attack_type = []
    for i in range(len(vector)):
        temp = []
        temp.append(vector[i])
        attack = decision_tree.predict(np.asarray(temp))  # Predict attack type using decision tree
        attack_type.append(attack[0])
    
    attack_type = np.asarray(attack_type)
    X_train, X_test, y_train, y_test = train_test_split(vector, attack_type, test_size=0.2)
    
    # Reshape input data for LSTM
    X_train1 = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test1 = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    y_train1 = to_categorical(y_train)
    y_test1 = to_categorical(y_test)
    
    # Define LSTM model
    cnnlstm_model = Sequential()
    cnnlstm_model.add(LSTM(32, input_shape=(X_train1.shape[1], X_train1.shape[2])))
    cnnlstm_model.add(Dropout(0.2))
    cnnlstm_model.add(Dense(32, activation='relu'))
    cnnlstm_model.add(Dense(y_train1.shape[1], activation='softmax'))
    
    cnnlstm_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # Train and save the model
    if not os.path.exists("model/lstm_weights.hdf5"):
        model_check_point = ModelCheckpoint(filepath='model/lstm_weights.hdf5', verbose=1, save_best_only=True)
        hist = cnnlstm_model.fit(X_train1, y_train1, batch_size=16, epochs=2, validation_data=(X_test1, y_test1), callbacks=[model_check_point], verbose=1)
        
        with open('model/lstm_history.pckl', 'wb') as f:
            pickle.dump(hist.history, f)
    else:
        cnnlstm_model.load_weights("model/lstm_weights.hdf5")
    
    # Perform prediction on test data    
    predict = cnnlstm_model.predict(X_test1)
    predict = np.argmax(predict, axis=1)
    y_test1 = np.argmax(y_test1, axis=1)
    
    # Call this function to calculate accuracy and other metrics
    calculateMetrics("CNN-LSTM", predict, y_test)


def attackAttributeDetection():
    text.delete('1.0', END)
    global autoencoder, decision_tree, encoder_model, dnn, pca
    filename = filedialog.askopenfilename(initialdir="Dataset")
    dataset = pd.read_csv(filename)
    dataset.fillna(0, inplace = True)
    values = dataset.values
    temp = dataset.values
    temp = scaler.transform(temp)
    test_vector = encoder_model.predict(temp)  #extracting features using autoencoder
    test_vector = pca.transform(test_vector)
    print(test_vector.shape)
    predict = decision_tree.predict(test_vector)
    for i in range(len(predict)):
        if predict[i] == 0:
            text.insert(END,"New Test Data : "+str(values[i])+" ====> NO CYBER ATTACK DETECTED\n\n")
        else:
            text.insert(END,"New Test Data : "+str(values[i])+" ====> CYBER ATTACK DETECTED Attribution Label : "+str(labels[predict[i]])+"\n\n")                     
    

def graph():       
    df = pd.DataFrame([['AutoEncoder','Precision',precision[0]],['AutoEncoder','Recall',recall[0]],['AutoEncoder','F1 Score',fscore[0]],['AutoEncoder','Accuracy',accuracy[0]],
                       ['Decision Tree with PCA','Precision',precision[1]],['Decision Tree with PCA','Recall',recall[1]],['Decision Tree with PCA','F1 Score',fscore[1]],['Decision Tree with PCA','Accuracy',accuracy[1]],
                       ['CNNLSTM','Precision',precision[2]],['CNNLSTM','Recall',recall[2]],['CNNLSTM','F1 Score',fscore[2]],['CNNLSTM','Accuracy',accuracy[2]],
                      ],columns=['Algorithms','Performance Output','Value'])
    df.pivot("Algorithms", "Performance Output", "Value").plot(kind='bar')
    plt.show()


def comparisonTable():
    output = "<html><body><table align=center border=1><tr><th>Algorithm Name</th><th>Accuracy</th><th>Precision</th><th>Recall</th>"
    output+="<th>FSCORE</th></tr>"
    output+="<tr><td>AutoEncoder</td><td>"+str(accuracy[0])+"</td><td>"+str(precision[0])+"</td><td>"+str(recall[0])+"</td><td>"+str(fscore[0])+"</td></tr>"
    output+="<tr><td>Decision Tree with PCA</td><td>"+str(accuracy[1])+"</td><td>"+str(precision[1])+"</td><td>"+str(recall[1])+"</td><td>"+str(fscore[1])+"</td></tr>"
    output+="<tr><td>CNNLSTM</td><td>"+str(accuracy[2])+"</td><td>"+str(precision[2])+"</td><td>"+str(recall[2])+"</td><td>"+str(fscore[2])+"</td></tr>"
    output+="</table></body></html>"
    f = open("table.html", "w")
    f.write(output)
    f.close()
    webbrowser.open("table.html",new=2)
    

font = ('times', 16, 'bold')
title = Label(main, text='An improved Hybrid Algorithm for Cyber Attack Detection from IOT Environment')
title.config(bg='greenyellow', fg='dodger blue')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 12, 'bold')
text=Text(main,height=20,width=80)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=300,y=120)
text.config(font=font1)


font1 = ('times', 13, 'bold')
uploadButton = Button(main, text="Upload IOT Dataset", command=uploadDataset)
uploadButton.place(x=50,y=100)
uploadButton.config(font=font1)  

processButton = Button(main, text="Preprocess Dataset", command=preprocessing)
processButton.place(x=50,y=150)
processButton.config(font=font1) 

autoButton = Button(main, text="Run AutoEncoder Algorithm", command=runAutoEncoder)
autoButton.place(x=50,y=200)
autoButton.config(font=font1)

dtButton = Button(main, text="Run Decision Tree with PCA", command=runDecisionTree)
dtButton.place(x=50,y=250)
dtButton.config(font=font1)


dnnButton = Button(main, text="Run CNN-LSTM Algorithm", command=runLSTM)
dnnButton.place(x=50,y=300)
dnnButton.config(font=font1)

attributeButton = Button(main, text="Detection of Attack Type", command=attackAttributeDetection)
attributeButton.place(x=50,y=350)
attributeButton.config(font=font1) 

graphButton = Button(main, text="Comparison Graph",command=graph)
graphButton.place(x=50,y=400)
graphButton.config(font=font1)

tableButton = Button(main, text="Comparison Table", command=comparisonTable)
tableButton.place(x=50,y=450)
tableButton.config(font=font1)




main.config(bg='MistyRose')
main.mainloop()
