# @Time    : 4/6/2023 1:03 PM
# @Author  : Pronob Barman
# @FileName: health_literacy.py
# @Software: PyCharm

'''
This script is about making a health literacy score for the participants from  the survey questions Q88 to Q91.
Health literacy Score (Index?) --> no knowledge (0) to Very knowledgeable(12)
help from someone in reading (Q88) - always (1), 2, 3, 4, never (5)
self-confidence level- (Q89) - not at all (1), 2, 3, 4, extremely (5)
Difficulty of understanding written information (Q90) - always (1), 2, 3, 4, never (5)
Difficulty of understanding medical terms in speaking (Q91) - always (1), 2, 3, 4, never (5)
'''

# import libraries
import pandas as pd
data = pd.read_csv('data.csv, sep='\t', header=0)

#Read in survey results file
with open(d + f, 'r') as infile:
    dataDictList = []
    head = 'DistributionChannel	First Language	Q84#4_2	Q84#4_3	Q84#4_1	Student Status	RaceAnalysis	Q84#4_4	Q81_5_TEXT	Q70_5_TEXT	RecipientLastName	Q84#6_4	Progress	Q84#6_1	Q84#6_2	Q84#6_3	Q51	Q50	Q53	Q52	Q54	Q57	Q56	Q59	Q58	Q84#2_1	Q84#2_2	Q84#2_3	Q84#2_4	Q87_6_TEXT	IPAddress	Q20_2cat	Q94_4cat	prolificID	Q84#3_1	Q84#3_3	Q84#3_2	Q84#3_4	Q79_8_TEXT	Nationality	Employment Status	Q13_mod	LearnedNum	Q46	Q47	Q45	Q42	Q43	Q40	Q41	Q6Q7	Q48	Q49	Q92_4cat	Ethnicity (Simplified)	Q70	ExternalReference	Q52_5_TEXT	Q84#5_2	Q84#5_1	Race/EthnicityAnalysis	Q84#5_4	LocationLatitude	Q11_norm	Q84#1_4	Q84#1_3	Q84#1_2	Q84#1_1	Country of Birth	Q33	Q32	Q31	Q30	Q37	Q36	Q35	Q34	Q76_3_TEXT	Q39	Q38	Current Country of Residence	Q77_6_TEXT	Q62_5_TEXT	RecipientFirstName	Q11_cat	QID1	Q23_4_TEXT	Q13_7_TEXT	Q99_3cat	Q22_7_TEXT	Q20	Q21	Q22	Q23	Q24	Q37_9_TEXT	Q26	Q27	Q29	Q84#5_3	completed_date_time	Q91	Q97_5_TEXT	Q100	Q14_mod	reviewed_at_datetime	Status	StartDate	Q99	Q98	RecipientEmail	Q95	Q94	Q97	Q96	ResponseId	Q90	Q93	Q92	Q15	Q14	Q17	Q16	Q11	Q13	Q12	ageCat1	Q19	Q42_5_TEXT	Q30_7_TEXT	Q59_6_TEXT	Q82	Q83	Q80	Q81	Q86	Q87	Q85	Q88	Q89	LocationLongitude	Q32_5_TEXT	Q50_8_TEXT	Sex	RecordedDate	HealthLitCat	Q12_5_TEXT	Q16_6_TEXT	Q5	Q4	Q7	Q6	Q8	session_id	EthnicityAnalysis	EndDate	Q61_5_TEXT	num_rejections	num_approvals	Finished	Q79	Q78	Q77	Q76	Q75	Q74	Q73	Q48_7_TEXT	Q71	Q25	status	Q65_9_TEXT	Duration (in seconds)	HealthLitSum	started_datetime	Q100_5cat	prolific_score	Q57_6_TEXT	time_taken	Q67	Q33_6_TEXT	entered_code	Q13_3cat	Q60	age	Q98_9_TEXT	Q25_5_TEXT	Q68	Q69	Q64	Q65	Q66	UserLanguage	Q34_5_TEXT	Q61	Q62	Q63'
    headList = head.split('\t')
    inDict = csv.DictReader(infile)
    for row in inDict:
        dataDictList.append(row)

print(dataDictList[3])