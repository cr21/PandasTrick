"""
Let’s say you’re given a dataframe of standardized test scores from high schoolers from grades 9 to 12 called df_grades.

Given the dataset, write code function in Pandas called bucket_test_scores to return the cumulative percentage of students that received scores within the buckets of <50, <75, <90, <100.

Example:

Input:

print(df_grades)
user_id	grade	test score
1	10	85
2	10	60
3	11	90
4	10	30
5	11	99
Output:

def bucket_test_scores(df_grades) ->
grade	test score	percentage
10	<50	33%
10	<75	66%
10	<90	100%
10	<100	100%
11	<50	0%
11	<75	0%
11	<90	50%
11	<100	100%


TEST DF

def test_seniors_low_scores():
    import pandas as pd  
    
    data = {'user_id':  [1,2,3,4,5,6,7,8,9,10,11,12],
        'grade': [10,10,11,10,11,11,11,10,12,12,12,12],
        'test score': [20,15,100,99,1,3,4,33,4,4,4,4]
        }

    df = pd.DataFrame(data,columns = ['user_id' ,  'grade' , 'test score'] )
    true_output ={'grade': {0: 10, 1: 10, 2: 10, 3: 10, 4: 11, 5: 11, 6: 11, 7: 11, 8: 12, 9: 12, 10: 12, 11: 12}, 'test score': {0: '<50', 1: '<75', 2: '<90', 3: '<100', 4: '<50', 5: '<75', 6: '<90', 7: '<100', 8: '<50', 9: '<75', 10: '<90', 11: '<100'}, 'percentage': {0: '75%', 1: '75%', 2: '75%', 3: '100%', 4: '75%', 5: '75%', 6: '75%', 7: '100%', 8: '100%', 9: '100%', 10: '100%', 11: '100%'}}

    test_output = pd.DataFrame.to_dict(bucket_test_scores(df))

    assert true_output == test_output

"""

import pandas as pd
def bucket_test_scores(df):
    bins=[0,50,75,90,100]
    labels =['<50','<75','<90','<100']
    df['test score'] = pd.cut(df['test score'],bins,labels= labels)
    # DataFrame Status
        #     user_id  grade test score
        # 0        1     10        <90
        # 1        2     10        <75
        # 2        3     11        <90
        # 3        4     10        <50
        # 4        5     11       <100

    
    
    numerator = df.groupby(['grade','test score'])['user_id'].count()
    # Numerator Status

        #         grade  test score
        # 10     <50           1
        #     <75           1
        #     <90           1
        #     <100          0
        # 11     <50           0
        #     <75           0
        #     <90           1
        #     <100          1

    denomerator = df.groupby('grade')['user_id'].count()
    # Denomenator Status
        #     grade
        # 10    3
        # 11    2

    df = numerator/denomerator
    df = df.reset_index()
    # Data Frame Status
        #     grade test score   user_id
        # 0     10        <50  0.333333
        # 1     10        <75  0.333333
        # 2     10        <90  0.333333
        # 3     10       <100  0.000000
        # 4     11        <50  0.000000
        # 5     11        <75  0.000000
        # 6     11        <90  0.500000
        # 7     11       <100  0.500000
    
    df['percentage']=(df.groupby(['grade'])['user_id'].cumsum()*100).astype(int).astype('str')+"%"
    # Percentage cummulative

    df=df[['grade','test score','percentage']]
        #     grade test score   user_id percentage
        # 0     10        <50  0.333333        33%
        # 1     10        <75  0.333333        66%
        # 2     10        <90  0.333333       100%
        # 3     10       <100  0.000000       100%
        # 4     11        <50  0.000000         0%
        # 5     11        <75  0.000000         0%
        # 6     11        <90  0.500000        50%
        # 7     11       <100  0.500000       100%
    return df
    
    
