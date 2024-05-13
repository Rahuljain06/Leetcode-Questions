class Solution:
    def reachNumber(self, target: int) -> int:
        #1 Step : pehle ham  simple loop lagakar tab tak aage badenge jba tak ham target tak na pahoch jaye ya usse aage nikal na jaye
        #2 fir hame sum-target ko even karna hai tab hi ham koi no. flip kar payenge
        # for eg: target is 5
        # to ham 1+2+3=6 tak gaye par ham isme koi no.flip karenge to ans nhi aaygega for eg
        # Ist Case:  agar ham 1 ko flip karte hai to 6-(2*1)=4 
        #hamne 2 se multiply esiliye kiya kyunki ek baar vo add ho chuka hai and usse hame -ve value ki tarah add karna hai to -1+2+3=4 to iske liye agar ham curr sum i.e 6 me se (2*1) subtract kar denge to ans 4 aa jayega.
        # IInd Case: agar ham 2 ko flip karte hai to 6-(2*2)=2 => 1-2+3=2
        # 3rd Case: agar ham 3 ko flip karte hai to 6-(2*3)=0 => 1+2-3=0
        # TO hamne dekha ki flip karne se ans nhi aaya kyunki sum-target=> 6-5 =>1 odd tha
        # par ham agar sum-target ko even karle to ans aa jayega to esiliye tab tak aage badenge tab tak sum-target = even na ho jaaye
        #for eg: 1+2+3+4=10 abhi bhi 10-5= 5 odd hai..to ham nhi pahoch sakte
        # 1+2+3+4+5 =15 ab 15-5=10 even hai ab ham pahoch sakte agar ham 5 ko flip kar de 15-2*5=5
        # 1+2+3+4-5=5 ...to hame isse hi code karn hai
        
        
        csum=0
        steps=0
        target=abs(target)
        while (csum<target):
            steps+=1
            csum+=steps
        
        while (csum-target)%2!=0:
            steps+=1
            csum+=steps
            
        return steps
        
        
        

 