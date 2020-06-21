#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:22:15 2020

@author: 
"""

class Comparison:
    
  def __init__(self):
    
        super().__init__()

  #The goal of this function is to execute the models and show the differents results. 
  #It is the function to call when we want to test differents models 
  #with differents values for parameters
  def run_comparison(self, stream, stream_n_features, window = 100, 
                     estimators = 50, anomaly = 0.5, drift_rate = 0.3, 
                     result_folder="Generated", max_sample=100000, n_wait=200,
                     metrics=['accuracy', 'f1', 'kappa', 'kappa_m', 
                              'running_time','model_size']):
    
    from skmultiflow.anomaly_detection import HalfSpaceTrees
    from source.iforestasd_scikitmultiflow import IsolationForestStream
    from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
    
    # Creation f the result csv
    directory_path = 'results/'+str(result_folder)
    self.check_directory(path=directory_path)
    result_file_path = directory_path+'/result_for_WS'+str(window)+'_NE'+str(estimators)+'.csv'
    
    # 2. Prepare for use This function is usefull to have data window by window
    # stream.prepare_for_use() # Deprecated so how to prepare data?
    
    models = [HalfSpaceTrees(n_features=stream_n_features, window_size=window, 
                             n_estimators=estimators, anomaly_threshold=anomaly),
    #IForest ASD use all the window_size for the sample in the training phase
    IsolationForestStream(window_size=window, n_estimators=estimators, 
                          anomaly_threshold=anomaly, drift_threshold=drift_rate)]
    # Setup the evaluator
    evaluator = EvaluatePrequential(pretrain_size=1, max_samples=max_sample, 
                                    show_plot=True, 
                                    metrics=metrics, batch_size=1, 
                                    output_file = result_file_path,
                                    n_wait = n_wait) 
    # 4. Run the evaluation 
    evaluator.evaluate(stream=stream, model=models, model_names=['HSTrees','iForestASD'])
    print("")
    print("Please find evaluation results here "+result_file_path)
    return 
  
  def get_dataset(self, dataset_name="Generator", classification_function=0, 
                  noise_percentage=0.7, random_state=1):
      #Dataset
      #  Name M(#instances) N(#attributes) Anomaly
      #  Threshold
      #  Http 567498 3 0.39%
      #  Smtp 95156 3 0.03%
      #  ForestCover 286048 10 0.96%
      #  Shuttle 49097 9 7.15%
      if dataset_name=="Generator":
         return self.get_data_generated(classification_function, 
                                        noise_percentage, random_state);
      elif dataset_name=="HTTP":
         path = "datasets/HTTP.csv"
         return self.get_file_stream(path);
      elif dataset_name=="ForestCover":
         path = "datasets/ForestCover.csv"
         return self.get_file_stream(path);
      elif dataset_name=="Shuttle":
         path = "datasets/Shuttle.csv"
         return self.get_file_stream(path);
      elif dataset_name=="SMTP":
         path = "datasets/SMTP.csv"
         return self.get_file_stream(path);
      else:
         print("The specified dataset do not exist yet."+ 
               " Try to contact the administrator for any add. "+
               " Or choose between these datasets:['Generator','HTTP','ForestCover','Shuttle','SMTP']");
         return None
          
  def get_file_stream(self, path):
      from skmultiflow.data.file_stream import FileStream
      return FileStream(path, n_targets=1, target_idx=-1)
  
  def get_data_stream(self, path):
      from skmultiflow.data.data_stream import DataStream
      return
  
    
  def get_data_generated(self,classification_function, noise_percentage, random_state):
      from skmultiflow.data import SEAGenerator
      return SEAGenerator(classification_function=classification_function, 
                          noise_percentage=noise_percentage, random_state=random_state)
  
    
  #To transform datasets by replace anomaly label by 1 and normal label by 0
  def prepare_dataset_for_anomaly(self, full_dataset, y_column:int, 
                                  anomaly_label:str='\'Anomaly\'', file_name:str="new"):
      import numpy as np
      import pandas as pd
      
      full_dataset[y_column] = np.where(full_dataset[y_column]==anomaly_label,1,0)
      dataset = pd.DataFrame(full_dataset)
      dataset.drop([0], inplace=True)
      full_file_path = "../datasets/"+file_name+".csv"
      dataset.to_csv(full_file_path, index=None, header=True)
      return dataset
  
  def check_directory(self,path):
      from pathlib import Path
      Path(path).mkdir(parents=True, exist_ok=True) 
      
     
  def merge_file(self, folder_path, output_file = 'output.csv'):
    import os
    import pandas as pd
    result = pd.DataFrame()
    print('List of file merged')
    print()
    no = '.ipynb_checkpoints'
    for file_ in os.listdir(folder_path):
        print(file_)
        #list.append(file_)
        if file_ != no:
            print(file_)
            df = pd.read_csv(folder_path+file_, sep = ',', skiprows=6, header = 0, dtype='unicode', error_bad_lines=False)
            df.at[0,'param'] = str(file_)
            df.at[0,'window'] = df.param.apply(lambda st: st[st.find("WS")+2:st.find("_NE")])[0]
            df.at[0,'estimators']= df.param.apply(lambda st: st[st.find("NE")+2:st.find("_UP")])[0]
            df.at[0,'updates']= df.param.apply(lambda st: st[st.find("UP_")+3:st.find(".csv")])[0]
 
            result = pd.concat([result,df],ignore_index=True)
    #result.sort_values(by = ['window', 'estimators'], inplace= True)
    result.columns=df.columns
    #output_file = 'RESULT_SHUTTLE10K.csv'
    result.to_csv(output_file,index=False)
    
    return result
   
  def data_prep (self, df_forest):
    df_forest.dropna(inplace= True)
    df_forest.sort_values(by = ['window', 'estimators'], inplace= True)
    df_forest.columns = df_forest.columns.str.replace('current_', '')
    df_forest.drop(columns = ['param']).astype(float)
    df_forest=df_forest.drop(columns = ['param']).astype(float)
    df_forest.window = df_forest.window.astype(int)
    df_forest.estimators = df_forest.estimators.astype(int)
    df_forest['Windows_Trees_set_up']='W'+df_forest['window'].astype(str)+'__'+'T'+df_forest['estimators'].astype(str)
    df_forest.columns = df_forest.columns.str.replace('current_', '')
    df_forest.sort_values(by = ['window', 'estimators'], inplace= True)
    
    return df_forest
 