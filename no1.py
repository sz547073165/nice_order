import pandas as pd
import numpy as np

action_data = pd.read_csv('data_set/action_train.csv')
#action_data.info()

user_list = action_data['userid'].unique()

user_action = pd.DataFrame(index=user_list)

#操作类型总次数
action_data_groupby_1 = action_data.groupby(['userid', 'actionType']).count().unstack()
for x in np.arange(9):
    temp = pd.DataFrame(data=action_data_groupby_1.iloc[:,x])
    temp.columns = ['%s_总次数' % (x + 1)]
    user_action = pd.merge(user_action,temp,left_index=True,right_index=True)
user_action.fillna(0,inplace=True)

#操作类型占比
action_data_groupby_2 = action_data.groupby('userid').count()
for x in np.arange(9):
    user_action['%s_占比' % (x + 1)] = user_action['%s_总次数' % (x + 1)] / action_data_groupby_2.iloc[:,0]

user_action = pd.merge(user_action,pd.DataFrame(action_data_groupby_2.iloc[:,0]),left_index=True,right_index=True)
user_action.rename(columns={'actionType':'操作总数'},inplace=True)


print()