#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n,k;
    cin>>n>>k;
    int a[n];
    multiset <int> s,s1,s2;
    for(int i=0;i<n;i++){
        cin>>a[i];
        if(i<k){
            s.insert(a[i]);
        }
    }
    //cout<<"%";
    if(k==1){
        for(int i=0;i<n;i++){
            cout<<a[i]<<" ";
        }
        return 0;
    }
    /*
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }*/
    
    int val = (n + 1)/2;
    int c=1;
    for(auto it : s){
        if(c<=val){
            s1.insert(it);
        }else{
            s2.insert(it);
        }
        c++;
    }
    //cout<<"#";
    cout<<*s1.end()<<" ";
    /*
    for(auto it: s1){
        cout<<it<<" ";
    }
    for(auto it : s2){
        cout<<it<<" ";
    }
    */
    
    
    
    for(int i=k;i<n;i++){
        
        
        if(s1.find(a[i-k])!=s1.end()){
            
            
            s1.erase(s1.find(a[i-k]));
            //s1.insert(a[i]);
            
            if(*s2.begin()>=a[i]){
                s1.insert(a[i]);
            }else{
                
                int val1 = *s2.begin();
                s1.insert(val1);
                s2.erase(s2.find(val1));
                s2.insert(a[i]);
                
            }
            
            
        }
        
        
        else if(s2.find(a[i-k])!=s2.end()){
            
            s2.erase(s2.find(a[i-k]));
            //s2.insert(a[i]);
            
            if(*s1.end()<=a[i]){
                s2.insert(a[i]);
            }else{
                
                int val1 = *s1.end();
                s2.insert(val1);
                s1.erase(s1.find(val1));
                s1.insert(a[i]);
                
            }
            
            
        }
        
        
        cout<<*s1.end()<<" ";
        
    }
    
    
    return 0;
}