option nodate nonumber;

***********************************************************************;
* Program title:  Import100CarEventReducedData_v1_2.sas		  	      *;
* Date of creation: 03.25.2010              						  *;
* Author: J. Sudweeks                        						  *;
* Inputs: 100CarEventReducedVideoData_v1_2.txt                        *;
* Outputs: SAS dataset v1_2dat    									  *;
* Synopsis: Import of 100-car Event Reduced Data v1.2.  User supplies *;
*           filepath to tab delited text file. For example if file is *; 
*			located on the C drive replace the PUT FILEPATH HERE text *;
*			with c: to produced the following:				          *; 
*			c:\100CarEventReducedVideoData_v1_2.txt				      *;
***********************************************************************;


filename v1_2_in 'PUT FILEPATH HERE\100CarEventVideoReducedData_v1_2.txt';

data v1_2dat;
	infile v1_2_in dlm = '09'x firstobs = 2 lrecl = 1190 missover dsd;
	length webfileid 4. vehicle_webid 3. event_start 4. event_end  4. event_severity $10.
		   subject_webid 4. age 3. gender $1.
		   event_nature $78. incident_type $49.
		   pre_incident_maneuver $49. maneuver_judgment $18. precipitating_event $69. driver_reaction $32.
		   post_maneuver_control $25.
	   	   driver_behavior_1 $87. driver_behavior_2 $87. driver_behavior_3 $87.
		   di_drowsy $3. di_ill $3. di_angry $3. di_other_emotion $3. di_medication $3. di_alcohol $3. 
		   di_other_illicit_drugs $3. di_wheelchair $3. di_prev_injury $3. di_deaf $3. di_distracted $3. 
		   di_other $3. di_unknown $3. di_no_analyzed_data $3.
		   infrastructure $22.
		   distraction_1 $50. distraction_1_start_sync 4. distraction_1_end_sync 4. distraction_1_outcome $19.
		   distraction_2 $50. distraction_2_start_sync 4. distraction_2_end_sync 4. distraction_2_outcome $19.
		   distraction_3 $50. distraction_3_start_sync 4. distraction_3_end_sync 4. distraction_3_outcome $19.
		   hands_on_wheel $15.
		   vehicle_contributing_factors $18.
		   visual_obstructions $68. surface_condition $16. traffic_flow $33. travel_lanes $16. traffic_density $110.
		   traffic_control $22.
		   relation_to_junction $28. alignment $21. locality $30. lighting $21. weather $16.
		   driver_seatbelt_use $17.
		   number_of_other_vehicles 3. fault $14.
		   vehicle_2_location $85. vehicle_2_type $46. vehicle_2_maneuver $77. vehicle_2_driver_reaction $32.
		   vehicle_3_location $85. vehicle_3_type $46. vehicle_3_maneuver $77. vehicle_3_driver_reaction $32.;

	input webfileid vehicle_webid Event_Start Event_End	Event_Severity $ 
		  subject_webid Age Gender $	
		  Event_Nature $ Incident_Type $
		  Pre_Incident_Maneuver $ Maneuver_Judgment $ Precipitating_Event $ Driver_Reaction $ Post_Maneuver_Control $	
		  Driver_Behavior_1	$ Driver_Behavior_2 $ Driver_Behavior_3 $	
		  di_drowsy $ di_ill $ di_angry $ di_other_emotion $ di_medication $ di_alcohol $ di_other_illicit_drugs $ di_wheelchair $ 
		  di_prev_injury $ di_deaf $ di_distracted $ di_other $ di_unknown $ di_no_analyzed_data
		  Infrastructure $
		  Distraction_1	$ Distraction_1_Start_Sync Distraction_1_End_Sync $ Distraction_1_Outcome $
		  Distraction_2	$ Distraction_2_Start_Sync Distraction_2_End_Sync Distraction_2_Outcome $
		  Distraction_3	$ Distraction_3_Start_Sync Distraction_3_End_Sync Distraction_3_outcome $
		  Hands_on_Wheel $	
		  Vehicle_Contributing_Factors $	
		  Visual_Obstructions $ Surface_Condition $ Traffic_Flow $ Travel_Lanes	$ Traffic_Density $ Traffic_Control $
		  Relation_to_Junction $ Alignment $ Locality $ Lighting $ Weather $	
		  Driver_Seatbelt_Use $	
		  Number_of_Other_Vehicles Fault $	
		  Vehicle_2_Location $ Vehicle_2_Type $ Vehicle_2_Maneuver $ Vehicle_2_Driver_Reaction $	
		  Vehicle_3_Location $ Vehicle_3_Type $ Vehicle_3_Maneuver $ Vehicle_3_Driver_Reaction $;
run;
