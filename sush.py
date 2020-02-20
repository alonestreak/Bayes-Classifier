import pandas as pd

def get_subtable(df, node,value):
  return df[df[node] == value].reset_index(drop=True)
 
def Byee(df):
    pred=[]
    for i in df.columns:
        pred.append(i)
    #print(pred)



    ques=[]
    for i in range(len(df.columns)-1):
        ques.append(input(pred[i]))



    Class = df.keys()[-1] 
    target_variables = df[Class].unique()
    print(target_variables)
    #Output variales needs to be changed here 
    Yes="Yes"
    No="No"
    #print(target_variables)



    seriesObj = df.apply(lambda x: True if x[Class] ==Yes else False , axis=1)
    numOfRows = len(seriesObj[seriesObj == True].index)
    print(numOfRows)
    pos_prob=numOfRows/len(df)
    neg_prob=(len(df)-numOfRows)/len(df)
    #print(pos_prob)
    #print(neg_prob)




    ans_pos=[]
    ans_neg=[]
    pos_frame=get_subtable(df,Class,Yes)
    neg_frame=get_subtable(df,Class,No)
    print(pos_frame)
    print(neg_frame)
    c=0
    for i in ques:


        #calculating the probalility of attributes which belongs to class 'YES'
        #print(pred[c])
        seriesObj1 = pos_frame.apply(lambda x: True if x[pred[c]] == ques[c] else False , axis=1)
        numOfRows1 = len(seriesObj1[seriesObj1 == True].index)
        #print(numOfRows1)
        if numOfRows1==0 :#laplace correction 
            ans_pos.append(numOfRows1+1/(len(pos_frame)+1))
        else:
            ans_pos.append(numOfRows1/len(pos_frame))




         #calculating the probalility of attributes which belongs to class 'YES'
        seriesObj2 = neg_frame.apply(lambda x: True if x[pred[c]] == ques[c] else False , axis=1)
        numOfRows2 = len(seriesObj2[seriesObj2 == True].index)
        #print(numOfRows2)
        if numOfRows2==0 :
            ans_neg.append(numOfRows2+1/(len(neg_frame)+1))
        else:
            ans_neg.append(numOfRows2/len(neg_frame))
        c+=1



    #multiplying by probalility of YES and NO    
    final_pos=1
    final_neg=1
    for i in ans_pos:
        final_pos=final_pos*i
    for i in ans_neg:
        final_neg=final_neg*i

    final_pos= final_pos*pos_prob
    final_neg=final_neg*neg_prob
    print("probalility of positive"+str(final_pos))
    print("probalility of negative"+str(final_neg))



    if (final_neg>final_pos):
        return "Negative"
    else:
        return "Positive"



df = pd.read_csv('dataset.csv')
#print(df)
Bye=Byee(df)
print("Sample assigned to given instance is "+str(Bye))