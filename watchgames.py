import requests                                                                                                               
import json                                                                                                                   
import time                                                                                                                   
import datetime                                                                                                               
import urllib                                                                                                                 
import pyharmony                                                                                                              
import os                                                                                                                     
import logging                                                                                                                
import pyharmony_client                                                                                                       
                                                                                                                              
def main():                                                                                                                   
    default_activity = "watchtv" # Set to the slug for your Harmony activity to watch TV                                      
    harmony_hub_ip = "192.168.2.235" # IP address for harmony hub device                                                      
    harmony_port = "5222" # Port for harmony hub device default 5222                                                          
                                                                                                                              
    '''                                                                                                                       
    if (is_off):                                                                                                              
        print(watch_tv())                                                                                                     
        time.sleep(5)                                                                                                         
                                                                                                                              
    while current_activity != default_activity: # perform loop while current activity is not set to default_activity          
        print(watch_tv()) # turn on default activity                                                                          
        time.sleep(5)                                                                                                         
        is_off, current_status, current_activity = get_current_status() # refresh current_status                              
        if current_activity == default_activity: # check if default_activity is active now and break loop                     
            break                                                                                                             
    '''                                                                                                                       
                                                                                                                              
    token = pyharmony_client.get_token(harmony_hub_ip, harmony_port)                                                          
                                                                                                                              
    config = pyharmony_client.get_config(token, harmony_hub_ip, harmony_port)                                                 
                                                                                                                              
    print(pyharmony_client.get_current_activity(token, config, harmony_hub_ip, harmony_port))                                 
                                                                                                                              
    print(pyharmony_client.start_activity(token, harmony_hub_ip, harmony_port, config, default_activity))                     
                                                                                                                              
    print(pyharmony_client.change_channel(token, harmony_hub_ip, harmony_port, '576'))                                        
                                                                                                                              
if __name__ == "__main__":                                                                                                    
    main()                                                                                                                    
