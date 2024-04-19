# Basic Markov Model (achieved through matrix multiplication with numpy)

"""
steps/pseudocode:

define adjacent matrix
define weighted matrix (input pi)
matrix multiplication function definition
    function input: number of steps and requested output probability
    function output: probability distribution over steps and specific entity
print matrix multiplication over each step
"""
import numpy as np

x_input = np.array([0.4, 0.3, 0.3])

A = np.array([[0.7, 0.2, 0.1],
              [0.3, 0.5, 0.2],
              [0.1, 0.4, 0.5]])

steps = int(input("Number of steps: "))
# state = int(input("Chosen State (0-2): "))
num_iter = 0

def mult_matrix(x):
    global num_iter  # Declare num_iter as a global variable

    # Check if matrix multiplication is valid
    if x.shape[0] != A.shape[1]:  # Fix the condition here
        raise ValueError("Matrix multiplication is not valid for the given matrices.")
    
    # Initialize the product matrix Y
    Y = x @ A 

    num_iter += 1

    if num_iter == steps:
        print(Y)
        return

    mult_matrix(Y)

mult_matrix(x_input)