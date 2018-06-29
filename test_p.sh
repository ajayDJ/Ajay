#!/bin/bash 

declare -a recod=('/home/matchpoint/Downloads/testingdj/Hindi_Song_Ringtone_Download-1530167558.wav' '/home/matchpoint/Downloads/testingdj/Mujhko_Farebi_-_Heart_Broken_Hindi_Song_Ringtone_Download-1530167644.wav' '/home/matchpoint/Downloads/testingdj/Romantic_Version_By_Neha_Kakkar-1530167607.wav');


for rep in ${recod[@]}
do
	play $rep
done
