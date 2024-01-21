option nodate nonumber;

***********************************************************************;
* Program title:  ImportEventEyeglanceData_v1_2.sas			  	      *;
* Date of creation: 07.29.2010              						  *;
* Author: J. Sudweeks                        						  *;
* Inputs: 100CarEventEyeglanceData_v1_2.txt		                      *;
* Outputs: 1) SAS dataset sum_eyeglance_v1_2 						  *;
*		   2) SAS dataset exp_eyeglance_v1_2						  *;
* Synopsis: Import of 100-car Event Eyeglance Data V1_2.  User 	      *;
*			supplies filepath to tab delited text file.               *;
*			For example if file is located on the C drive             *;
*			replace the PUT FILEPATH HERE text with c: to produce     *;
*			the  following:				         					  *; 
*			c:\SAS\100CarEventEyeglanceData_v1_2.txt				  *;
***********************************************************************;


filename d_in 'PUT FILEPATH HERE\100CarEventEyeglanceData_v1_2.txt';


/*	SUMMARIZED GLANCES	*/

data sum_eyeglance_v1_2;
	infile d_in dlm = '09'x;
	length 	webfile_id 4.
			begin_sync 4.
			end_sync 4.
			glance_duration 4.
			glance_location $18.;
  	input webfile_id begin_sync end_sync glance_duration  glance_location $;
run;

proc sort data = sum_eyeglance_v1;
	by webfile_id begin_sync;
run;


/*	EXPANDED GLANCES	*/

data exp_eyeglance_v1_2 (keep = webfile_id sync glance_location);
	set sum_eyeglance_v1;
	by webfile_id begin_sync;

	do i = begin_sync to end_sync;
		sync = i;
		output;
	end;
run;
