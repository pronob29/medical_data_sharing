# -*- coding: utf-8 -*-
import csv
import pandas as pd
# C:\Users\prono\Downloads
d = 'C:/Users/prono/Downloads/'
f = 'PatientPerceptionsSurveyResponses+ProlificData+NewVariables.csv'
data = pd.read_csv(d + f, sep='\t', header=0)

#Read in survey results file
with open(d + f, 'r') as infile:
    dataDictList = []
    head = 'DistributionChannel	First Language	Q84#4_2	Q84#4_3	Q84#4_1	Student Status	RaceAnalysis	Q84#4_4	Q81_5_TEXT	Q70_5_TEXT	RecipientLastName	Q84#6_4	Progress	Q84#6_1	Q84#6_2	Q84#6_3	Q51	Q50	Q53	Q52	Q54	Q57	Q56	Q59	Q58	Q84#2_1	Q84#2_2	Q84#2_3	Q84#2_4	Q87_6_TEXT	IPAddress	Q20_2cat	Q94_4cat	prolificID	Q84#3_1	Q84#3_3	Q84#3_2	Q84#3_4	Q79_8_TEXT	Nationality	Employment Status	Q13_mod	LearnedNum	Q46	Q47	Q45	Q42	Q43	Q40	Q41	Q6Q7	Q48	Q49	Q92_4cat	Ethnicity (Simplified)	Q70	ExternalReference	Q52_5_TEXT	Q84#5_2	Q84#5_1	Race/EthnicityAnalysis	Q84#5_4	LocationLatitude	Q11_norm	Q84#1_4	Q84#1_3	Q84#1_2	Q84#1_1	Country of Birth	Q33	Q32	Q31	Q30	Q37	Q36	Q35	Q34	Q76_3_TEXT	Q39	Q38	Current Country of Residence	Q77_6_TEXT	Q62_5_TEXT	RecipientFirstName	Q11_cat	QID1	Q23_4_TEXT	Q13_7_TEXT	Q99_3cat	Q22_7_TEXT	Q20	Q21	Q22	Q23	Q24	Q37_9_TEXT	Q26	Q27	Q29	Q84#5_3	completed_date_time	Q91	Q97_5_TEXT	Q100	Q14_mod	reviewed_at_datetime	Status	StartDate	Q99	Q98	RecipientEmail	Q95	Q94	Q97	Q96	ResponseId	Q90	Q93	Q92	Q15	Q14	Q17	Q16	Q11	Q13	Q12	ageCat1	Q19	Q42_5_TEXT	Q30_7_TEXT	Q59_6_TEXT	Q82	Q83	Q80	Q81	Q86	Q87	Q85	Q88	Q89	LocationLongitude	Q32_5_TEXT	Q50_8_TEXT	Sex	RecordedDate	HealthLitCat	Q12_5_TEXT	Q16_6_TEXT	Q5	Q4	Q7	Q6	Q8	session_id	EthnicityAnalysis	EndDate	Q61_5_TEXT	num_rejections	num_approvals	Finished	Q79	Q78	Q77	Q76	Q75	Q74	Q73	Q48_7_TEXT	Q71	Q25	status	Q65_9_TEXT	Duration (in seconds)	HealthLitSum	started_datetime	Q100_5cat	prolific_score	Q57_6_TEXT	time_taken	Q67	Q33_6_TEXT	entered_code	Q13_3cat	Q60	age	Q98_9_TEXT	Q25_5_TEXT	Q68	Q69	Q64	Q65	Q66	UserLanguage	Q34_5_TEXT	Q61	Q62	Q63'
    headList = head.split('\t')
    inDict = csv.DictReader(infile)
    for row in inDict:
        dataDictList.append(row)

print(dataDictList[3])

#Create list of dictionaries with [{pid: {PP:1, miPHR: 0, thirdParty: 2, HealthSelfTracking: 1}}, ...]
#PP: Q6Q7 - No account == 0, One account == 1,
#           Two+ accounts == 2
#miPHR: if Q31 == 'Yes' or Q58 == 'Yes': miPHR = 1,
#           else miPHR = 0
#otherPHR (Q87): Checked/Unchecked = 1/0
#           --> Probably want to create 1 PHR variable that takes into account response to miPHR questions + other PHR (i.e., if using both = 2, if using one or the other = 1, if neither = 0)
#thirdParty: Q86 (select all that apply)
#           --> Number of third party apps reported
#healthSelfTracking (Q87): Checked/Unchecked = 1/0
#wearableDevice (Q87): Checked/Unchecked = 1/0
#homebasedMedicalDevice (Q87): Checked/Unchecked = 1/0
for d in dataDictList:
    techDict = {}
    if d['Q6Q7'] == 'No account':
        techDict['PP'] = 0
    elif d['Q6Q7'] == 'One account':
        techDict['PP'] = 1
    else:
        techDict['PP'] = 2
    if d['Q31'] == 'Yes' or d['Q58'] == 'Yes':
        techDict['miPHR'] = 1
    else:
        techDict['miPHR'] = 0
    if 'Another personal health record app (for example, Tidy Health PHR, Capzule)' in d['Q87']:
        techDict['otherPHR'] = 1
    else:
        techDict['otherPHR'] = 0
    if d['Q86'] == '':
        techDict['thirdParty'] = 0
    else:
        thirdPartyList = d['Q86'].split(',')
        techDict['thirdParty'] = len(thirdPartyList)
    if 'Health self-tracking app (for example, WaterMinder, Sleep Cycle, iFertracker, MyFitnessPal, Fitbit)' in d['Q87']:
        techDict['selfTrackingApp'] = 1
    else:
        techDict['selfTrackingApp'] = 0
    if 'Wearable device (for example, Apple watch, Fitbit, Upright Go 2 posture trainer)' in d['Q87']:
        techDict['wearable'] = 1
    else:
        techDict['wearable'] = 0
    if 'Home-based medical device (for example, smart blood pressure monitor, such as Withings BPM Connect Wi-Fi; smart blood glucose monitor)' in d['Q87']:
        techDict['homeMedDevice'] = 1
    else:
        techDict['homeMedDevice'] = 0
    # print techDict
    d['techEcosystem'] = techDict
    techScore = sum(techDict.values())
    # print techScore
    d['techScore'] = techScore


#Health Complexity Score (Index?) --> Not complex (0) to Very complex (12)
#Self-described health status (Q92) - Poor (4), Fair (3), Good (2), Very Good (1), Excellent (0)
#Chronic condition (Q93) - Yes (1), No (0)
#How often see a healthcare provider (Q94) - More than once a month (6), Once a month (5), Eight to eleven times per year (4), Five to seven times per year (3), Two to four times per year (2), Once a year (1), Less than once a year (0)
#Receive care from more than one healthcare org? (Q95) - Yes (1), No (0)
#prolificID
for dict in dataDictList:
    score = 0
    if dict['Q92'] == 'Prefer not to disclose' or dict['Q93'] == 'Prefer not to disclose' or dict['Q94'] == 'Prefer not to disclose' or dict['Q95'] == 'Prefer not to disclose':
        score = 'NA'
    else:
        if dict['Q92'] == 'Poor':
            score += 4
        elif dict['Q92'] == 'Fair':
            score += 3
        elif dict['Q92'] == 'Good':
            score += 2
        elif dict['Q92'] == 'Very Good':
            score += 1
        if dict['Q93'] == 'Yes':
            score += 1
        if dict['Q94'] == 'More than once a month':
            score += 6
        elif dict['Q94'] == 'Once a month':
            score += 5
        elif dict['Q94'] == 'Eight to eleven times per year':
            score += 4
        elif dict['Q94'] == 'Five to seven times per year':
            score += 3
        elif dict['Q94'] == 'Two to four times per year':
            score += 2
        elif dict['Q94'] == 'Once a year':
            score += 1
        if dict['Q95'] == 'Yes':
            score += 1
    dict['complexScore'] = score
    # print dict['prolificID'] + ': ' + str(score)
    if score == 'NA':
        scoreCat = 'NA'
    elif score <= 2:
        scoreCat = 'Low complexity'
    elif score > 2 and score <= 4:
        scoreCat = 'Medium-low complexity'
    elif score > 4 and score <= 7:
        scoreCat = 'Medium-high complexity'
    else:
        scoreCat = 'High complexity'
    dict['complexScoreCat'] = scoreCat


###WRITE OUT CSV FILE WITH NEW VARIABLES ONCE ALL CREATED###
with open('/Users/terareynolds/Documents/UMBC/Research/PatientPerceptionsofNewMechanismofClinicalDataAccess/SurveyResults/PatientPerceptionsSurveyResponses+ProlificData+NewVariablesEcosystem.csv', 'w') as csvfile:
    fieldnames = []
    for k in dataDictList[0].keys():
        fieldnames.append(k)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for fdict in dataDictList:
        writer.writerow(fdict)


###WRITE OUT CSV FILE WITH JUST ECOSYSTEM VARIABLES###
with open('/Users/terareynolds/Documents/UMBC/Research/PatientPerceptionsofNewMechanismofClinicalDataAccess/SurveyResults/PatientPerceptionsSurveyResponsesEcosystemVarsONLY.csv', 'w') as csvfile2:
    fieldnames = []
    for k2 in dataDictList[0]['techEcosystem'].keys():
        fieldnames.append(k2)
    writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
    writer.writeheader()
    for fdict2 in dataDictList:
        writer.writerow(fdict2['techEcosystem'])