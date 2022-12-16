# 1. Library imports

import streamlit as st
from pydantic import Field, BaseModel
import streamlit_pydantic as sp

st.title("Collatz Conjecture")
st.subheader('Simplest or Hardest Mathematical Conjecture? 最簡單或者是最困難的數學猜測?')
st.markdown(" Start from a randomly selected integer; and divided by 2 or multiples 3 and adds 1. Continue this step until being 1.  It is always being 1. 任取一個整數，如果是偶數則除以 2，如果是奇數 x3+1 ，持續這個步驟，直到直到最後為一才結束. 結果總是為一.")

def collatz_conjecture(num,print='all'):
   #num = int(input('Enter a number: '))
   sequence = [num]
   while(num != 1):
       if((num%2)==0):
           num = num // 2 
       else:
           num = (num*3) + 1
       sequence.append(num)
   if print=='all':
       return sequence
   else:
     output=[sequence[i] for i in range(5)]
     output.append('...')
     for i in range(5):
         output.append(sequence[i-5])
     return output

class ExampleModel(BaseModel):
      seed_number: int = Field(
        234,
        description="Input an integer",
    )

data = sp.pydantic_form(key="my_form", model=ExampleModel)
if data:
    result = data.dict()
    seed = result["seed_number"]
    flow = collatz_conjecture(seed)
    st.write(f'{flow}')