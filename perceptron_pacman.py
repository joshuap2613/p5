# perceptron_pacman.py
# --------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Perceptron implementation for apprenticeship learning
import util
from perceptron import PerceptronClassifier
from pacman import GameState

PRINT = True


class PerceptronClassifierPacman(PerceptronClassifier):
    def __init__(self, legalLabels, maxIterations):
        PerceptronClassifier.__init__(self, legalLabels, maxIterations)
        self.weights = util.Counter()

    def classify(self, data ):
        """
        Data contains a list of (datum, legal moves)

        Datum is a Counter representing the features of each GameState.
        legalMoves is a list of legal moves for that GameState.
        """
        guesses = []
        for datum, legalMoves in data:
            vectors = util.Counter()
            for l in legalMoves:
                vectors[l] = self.weights * datum[l] #changed from datum to datum[l]
            guesses.append(vectors.argMax())
        return guesses


    def train(self, trainingData, trainingLabels, validationData, validationLabels ):
        self.features = trainingData[0][0]['Stop'].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        """
        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."

            for i in range(len(trainingData)):
                "*** YOUR CODE HERE ***"
                util.raiseNotDefined()
        """
        #print(self.legalLabels)
        #print(self.weights)
        #print("features", self.features)
        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."
            for i in range(len(trainingData)):
                max_score = -1000000000000
                max_arg = None
                for action in trainingData[i][0]:
                    sa = (tuple([trainingData[i][0][action][feature] for feature in self.features]), action)
                    fsa = trainingData[i][0][action]
                    #print("fsa", fsa)
                    score = self.weights*fsa
                    if score > max_score:
                        max_score = score
                        max_arg = action
                    #print("sa is", sa)

                #print("max_score",int(max_score))
                #print("max_arg",max_arg)
                #print("traininglabels",trainingLabels[0])
                #break
                self.weights -= fsa
                self.weights += trainingData[i][0][trainingLabels[i]]
                """
                if max_arg != trainingLabels[i]:
                    for arg in self.weights:
                        if arg == max_arg:
                            self.weights[arg] -= sample
                        elif arg == trainingLabels[i]:
                            self.weights[arg] += sample
                """
