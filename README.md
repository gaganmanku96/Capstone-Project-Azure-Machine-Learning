# Student Placement Prediction

## Introduction
Placement plays an important role in the life of a student because it usually gives him a moral boost. In this project, we'll predict whether a student will get placed or not based on several factors like gender, section, no of backlogs, whether he applied for placement training or not. This can help the College/University Management to focus on certain students.

## Project Setup

## Dataset
The dataset contains 8 different features that we'll use to make the prediction

The features are
1. Roll_no: The roll number of the student (This is not used in model training as it is unique for every student). 
2. Gender: The gender of the student (M/F).
3. Section: The class section in which the student was present (A/B).
4. SSC_percentage: The percentage student got in Secondary School (10th Standard).
5. Inter_diploma_percentage: The percentage student got in in Inter diploma.
6. Undergraduation_percentage: The percentage he got in his undergraduation.
7. n_backlogs: The number of backlogs he had in his undergraduation.
8. Registered_for_placement_training: Whether he registered for placement training or not.
9. Placement_status: Was he placed or not (Placed or Not placed)

The dataset had some categorical columns which were converted to numerical using lambda fuctions.

Using the first 8 features we were prediction the value of Placement_status (whether the student got placed or not). 

## AutoML
In AutoML, we set the task to 'classification' and the primary_metric was 'Accuracy'. We enabled early stopping and the experiment timeout was set to 30min to reduce the computation cost. The cross_validation parameter was set to 3 and lastly max_concurrent_iterations was set to 3 to run iterations in parallel to improve efficiency.
![AutoML Config](images/automl_config.PNG)

Out of all the different models that were trained using AutoML, VotingEnsemble performed the best with an accuracy of 91.45%.
![VotingEnsemble Model](images/automl_run_completed.PNG)
![VotingEnsemble Model](images/automl_best_model_ui.PNG)

These were the parameters of the best model trained by AutoML.
![Best Model Paramaters](images/automl_best_run_parameters.PNG)

## HyperDrive
