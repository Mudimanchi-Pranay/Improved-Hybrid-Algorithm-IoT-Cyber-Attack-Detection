import os
import unittest
import tempfile
import numpy as np
import pandas as pd
import pickle

from unittest.mock import patch
from keras.models import Model, Sequential
from keras.layers import Input, Dense
from keras import backend as K
from sklearn.decomposition import PCA

# Import the Main.py module (ensure the filename is exactly Main.py)
import Main as main

# --- Helpers for testing --- #

class DummyText:
    """A dummy text replacement for the tk.Text widget."""
    def __init__(self):
        self.content = ""
    def delete(self, start, end):
        self.content = ""
    def insert(self, where, text):
        self.content += text
    def update_idletasks(self):
        pass

class DummyDecisionTree:
    """A dummy decision tree that always predicts 0 (i.e. 'Normal')."""
    def predict(self, X):
        return np.zeros((len(X),), dtype=int)

def dummy_fit(self, X, y, epochs, batch_size, shuffle, validation_data, callbacks, verbose):
    """A dummy version of Model.fit that returns a history with fixed values."""
    class DummyHistory:
        history = {"loss": [0.1], "accuracy": [1.0]}
    return DummyHistory()

# Create a dummy PCA that works like an identity transformer.
class DummyPCA:
    def fit_transform(self, X):
        return X
    def transform(self, X):
        return X

# --- Test Class --- #

class TestMainFunctions(unittest.TestCase):
    
    def setUp(self):
        # Replace the GUI text widget with our dummy so that text output is captured.
        main.text = DummyText()
        
        # Create a dummy dataset (e.g., 20 samples, 5 feature columns plus a label column).
        # The code in Main.py expects the last column to be used as labels.
        n_samples = 20
        n_features = 5
        # Random features in [0,1]
        X_dummy = np.random.rand(n_samples, n_features)
        # Dummy labels: 0 or 1 (for simplicity)
        y_dummy = np.random.randint(0, 2, size=(n_samples, 1))
        # Create a DataFrame similar to what your upload expects.
        # (If you need a column name for the plotting function, make sure the label column name is "result")
        columns = [f"f{i}" for i in range(n_features)] + ['result']
        self.dummy_df = pd.DataFrame(np.hstack((X_dummy, y_dummy)), columns=columns)
        
        # Save the dummy dataset temporarily (needed for functions that use filedialog)
        self.temp_csv = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        self.dummy_df.to_csv(self.temp_csv.name, index=False)
        self.temp_csv.close()
        
        # Also inject the dummy dataset into the global variable to simulate that a file was already uploaded.
        main.dataset = self.dummy_df.copy()
        
        # For later tests using preprocessing, call the preprocessing function to generate X, Y, and splits.
        main.preprocessing()
    
    def tearDown(self):
        # Clean up any temporary files created.
        os.remove(self.temp_csv.name)
        # Optionally, remove any model files created by the functions.
        if os.path.exists("model/encoder_model.json"):
            os.remove("model/encoder_model.json")
        if os.path.exists("model/encoder_model_weights.h5"):
            os.remove("model/encoder_model_weights.h5")
        if os.path.exists("model/lstm_weights.hdf5"):
            os.remove("model/lstm_weights.hdf5")
        if os.path.exists("table.html"):
            os.remove("table.html")
    
    def test_preprocessing(self):
        """Test that preprocessing sets the global variables and normalizes data."""
        # After setUp(), main.preprocessing() has been called.
        self.assertIsNotNone(main.X, "Global variable X should be set by preprocessing.")
        self.assertIsNotNone(main.Y, "Global variable Y should be set by preprocessing.")
        self.assertEqual(main.X.shape[0], self.dummy_df.shape[0], "Number of samples in X must equal the dataset rows.")
        self.assertIn("Total records found", main.text.content, "Preprocessed output should be logged to text widget.")
    
    def test_calculateMetrics(self):
        """Test calculateMetrics appends metric values."""
        # Reset globals
        main.accuracy = []
        main.precision = []
        main.recall = []
        main.fscore = []
        # Dummy true labels and predictions:
        y_true = np.array([0, 1, 0, 0])
        y_pred = np.array([0, 0, 0, 1])
        main.calculateMetrics("TestAlgo", y_pred, y_true)
        
        self.assertEqual(len(main.accuracy), 1, "Accuracy list should have one element after one call.")
        self.assertTrue(isinstance(main.accuracy[0], float), "Metric should be float.")
        self.assertIn("TestAlgo Accuracy", main.text.content, "Text widget should log the algorithm metrics.")
    
    @patch("tensorflow.keras.models.Model.fit", new=dummy_fit)
    def test_runAutoEncoder(self):
        """Test runAutoEncoder flows through and appends metrics.
           Here we monkey-patch the Model.fit to avoid long training."""
        # Force the branch to build a new autoencoder (simulate that no saved model exists)
        with patch("os.path.exists", return_value=False):
            # Ensure globals X_train, y_train, etc are available from preprocessing()
            main.runAutoEncoder()
        # Check that metrics for AutoEncoder have been appended.
        self.assertGreater(len(main.accuracy), 0, "Metrics should be appended by runAutoEncoder.")
        self.assertIsNotNone(main.autoencoder, "Autoencoder model should be set by runAutoEncoder.")
    
    def test_runDecisionTree(self):
        """Test runDecisionTree using a dummy autoencoder.
           We create a dummy autoencoder that simply passes input through."""
        # Create a dummy autoencoder that acts as an identity mapping.
        input_dim = main.X.shape[1]
        inp = Input(shape=(input_dim,))
        out = Dense(main.Y.shape[1], activation='softmax')(inp)
        dummy_autoencoder = Model(inputs=inp, outputs=out)
        main.autoencoder = dummy_autoencoder
        
        # Run Decision Tree training (this uses the autoencoder to extract features, then PCA)
        main.runDecisionTree()
        self.assertIsNotNone(main.decision_tree, "Decision tree should be created in runDecisionTree.")
        # Also, check that some metrics have been printed.
        self.assertIn("Decision Tree Trained", main.text.content, "Decision tree run should log output.")
    
    @patch("tensorflow.keras.models.Model.fit", new=dummy_fit)
    def test_runLSTM(self):
        """Test runLSTM’s flow by ensuring metrics are appended.
           We simulate a dummy decision tree and vector data."""
        # Prepare a dummy global vector (simulate features after PCA)
        # For example, let vector be our normalized X from preprocessing reduced to 7 features.
        n_samples = main.X.shape[0]
        main.vector = np.random.rand(n_samples, 7)
        # Set decision_tree to a dummy tree that always predicts 0.
        main.decision_tree = DummyDecisionTree()
        # Run LSTM training and prediction.
        main.runLSTM()
        # Check that metrics for CNN-LSTM have been appended.
        self.assertGreater(len(main.accuracy), 0, "Metrics should be appended by runLSTM.")
    
    def test_attackAttributeDetection(self):
        """Test attackAttributeDetection with dummy models.
           We simulate encoder_model, PCA, scaler, and decision_tree so that prediction always yields 0."""
        # Create a dummy encoder_model that returns its input.
        input_dim = main.X.shape[1]
        inp = Input(shape=(input_dim,))
        dummy_out = Dense(input_dim, activation='linear')(inp)
        dummy_encoder = Model(inputs=inp, outputs=dummy_out)
        main.encoder_model = dummy_encoder
        
        # Create a dummy scaler that acts as identity
        class DummyScaler:
            def transform(self, data):
                return data
        main.scaler = DummyScaler()
        
        # Use our DummyPCA (which acts as an identity transformer)
        main.pca = DummyPCA()
        
        # Set decision_tree to always predict 0.
        main.decision_tree = DummyDecisionTree()
        
        # Patch filedialog.askopenfilename so that it returns our temporary CSV file.
        with patch("tkinter.filedialog.askopenfilename", return_value=self.temp_csv.name):
            main.attackAttributeDetection()
        
        # Since DummyDecisionTree always predicts 0, check that the text widget has "NO CYBER ATTACK DETECTED"
        self.assertIn("NO CYBER ATTACK DETECTED", main.text.content,
                      "attackAttributeDetection should report no attack for predicted label 0.")
    
    @patch("matplotlib.pyplot.show")
    @patch("webbrowser.open")
    def test_comparisonTable(self, mock_webbrowser_open, mock_plt_show):
        """Test that comparisonTable writes an HTML file and attempts to open it."""
        # First, we set global metrics to dummy values.
        main.accuracy = [90.0, 85.0, 80.0]
        main.precision = [91.0, 86.0, 81.0]
        main.recall = [92.0, 87.0, 82.0]
        main.fscore = [93.0, 88.0, 83.0]
        
        main.comparisonTable()
        # Check that the file table.html was created.
        self.assertTrue(os.path.exists("table.html"), "Comparison table HTML file should be created.")
        with open("table.html", "r") as f:
            content = f.read()
            self.assertIn("Algorithm Name", content, "Table HTML file should contain header information.")
        # Check that webbrowser.open() was called.
        mock_webbrowser_open.assert_called_once()

if __name__ == '__main__':
    unittest.main()
