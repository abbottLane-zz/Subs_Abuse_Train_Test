# Query result field titles
SOC_HISTORIES = 'SocialHistories'
ROWS = 'rows'
CREATED_BY = 'CreatedBy'
MODIFIED_BY = 'ModifiedBy'
FIELD_ID = 'FieldResultId'
FIELD_NAME = 'Field'
VALUE = 'Value'
START_POS = 'StartPosition'
STOP_POS = 'StopPosition'
REPORT_ID = 'ReportId'
MRN = 'MRN'
DOC_ID = 'ReportNo'
REPORT_JOB_ID = 'ReportId/JobRunId'
JOB_ID = "JobRunId"

TRAIN_JOB_IDS = {95, 98, 99, 100, 101, 104, 105, 120, 121, 122, 135, 145, 147, 170, 171, 169}
TEST_JOB_IDS = {153,154,155}
IAA_JOB_IDS = {95, 96, 97}
JOB_IDS = TRAIN_JOB_IDS.union(TEST_JOB_IDS)