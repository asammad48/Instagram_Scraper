#!/usr/bin/env python
# coding: utf-8

# 

# In[ ]:


from tkinter import *
from selenium import webdriver   
import time  
import tkinter as tk


def Insta_Follower_HashTag():
    Search=Label(root,text="HashTag Search").grid(row=2,column=3)
    Search_Hashtag.grid(row=2,column=4)
    Submit_Search=Button(root,text="Submit Search For Followers with HashTag",command=Submit_Followers_HashTag).grid(row=3,column=3)
def Submit_Followers_HashTag():
    Instagarm_HashTag_Search(Search_Hashtag.get(),Page_Name_Entry.get(),Password_Entry.get())

    
def Instagarm_HashTag_Search(Search_Hashtag,getusername,getpassword):
    post_link=[]
    python_page_list=[]
    driver = webdriver.Firefox()  
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    name=driver.find_element_by_name('username')
    name.send_keys(getusername)
    time.sleep(2)
    password=driver.find_element_by_name('password')
    password.send_keys(getpassword)
    time.sleep(2)
    login=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
    login.click()
    time.sleep(8)
    search=driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys('#'+Search_Hashtag)
    time.sleep(10)
    page_list=driver.find_elements_by_class_name('yCE8d')
    time.sleep(3)
    print(len(page_list))
    for i in range(len(page_list)):
        adrs=page_list[i].get_attribute('href')
        python_page_list.append(adrs)
    for i in range(len(python_page_list)):
        time.sleep(5)
        print(python_page_list[i])
        driver.get(python_page_list[i])
        time.sleep(5)
        top_post=driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div')
        num_of_columns=top_post.find_elements_by_class_name('Nnq7C')
        time.sleep(3)
        column_element=num_of_columns[0].find_elements_by_class_name('v1Nh3')
        column_element[0].find_elements_by_class_name('_9AhH0')[0].click()
        time.sleep(4)
        count_follow=0
        try:
            while 1:
                time.sleep(2)
                button=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
                if button.get_attribute('innerHTML')=='Follow':
                    button.click()
                    count_follow=count_follow+1
                time.sleep(2) 
                driver.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
                if count_follow>200:
                    break
        except:
            print('error aya hai')




def Del_Following():
    Delete_Following(Page_Name_Entry.get(),Password_Entry.get())

def Delete_Following(getusername,getpassword):
    driver = webdriver.Firefox()  
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    name=driver.find_element_by_name('username')
    name.send_keys(getusername)
    time.sleep(2)
    password=driver.find_element_by_name('password')
    password.send_keys(getpassword)
    time.sleep(2)
    login=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
    login.click()
    time.sleep(5)
    account_address=driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
    account_address.click()
    time.sleep(3)
    click_account=driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]')
    click_account.click()
    time.sleep(5)
    page_url=driver.current_url
    scroll_length=0
    time.sleep(4)
    following=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
    following.click()
    time.sleep(4)
    popup=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    for i in range(0,100):
        #driver.get(page_url)
        time.sleep(4)
        for j in range(0,10):
            time.sleep(1)
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)
            time.sleep(2)
            followings_people=driver.find_elements_by_class_name('sqdOP')
        print(len(followings_people))
        for k in range(scroll_length,len(followings_people)):
            time.sleep(1)
            Delete_it(followings_people[k],driver)
        scroll_length=len(followings_people)
def Delete_it(followings_people,driver):
    try:
        followings_people.click()
        time.sleep(2)
        driver.find_element_by_class_name('aOOlW').click()
    except:
        time.sleep(2)
        driver.execute_script('el = document.elementFromPoint(47, 457); el.click();')
        time.sleep(2)





def Submit_Followers():
    Instagram_Followers(Search_Entry.get(),Page_Name_Entry.get(),Password_Entry.get())
    

#This is Instagram Followers Code without HashTag
total=0
def follow_gain(page_name,driver):
    
    driver.get(page_name)
    time.sleep(3)
    try:
        followers_list=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers_list.click()
        time.sleep(2)
        follower_pop(driver)
        return 0
    except:
        try:
            time.sleep(3)
            Report=driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[1]')
            Button_Name=Report.get_attribute('innerHTML')
            if Button_Name=='Report a Problem':
                print("Report a Problem")
                return 1
        except:
            print("error")
            return 0
def follower_pop(driver):
    count=0
    global total
    follower_popup=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    for i in range(0,10):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',follower_popup)
        time.sleep(1)
    followers_button=driver.find_elements_by_class_name('sqdOP')
    for i in range(len(followers_button)):
        name=followers_button[i].get_attribute('innerHTML')
        if name=='Follow':
            count=count+1
            followers_button[i].click()
            time.sleep(3)
            total=total+1
            if count==50:
                break
        print(name+"   "+str(total))
    if count<50:
        follower_pop()
def Instagram_Followers(getSearch,getusername,getpassword):
    python_page_list=[]
    driver = webdriver.Firefox()  
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    name=driver.find_element_by_name('username')
    name.send_keys(getusername)
    time.sleep(2)
    password=driver.find_element_by_name('password')
    password.send_keys(getpassword)
    time.sleep(2)
    login=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
    login.click()
    time.sleep(8)
    search=driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys(getSearch)
    time.sleep(3)
    page_list=driver.find_elements_by_class_name('yCE8d')
    print(len(page_list))
    for i in range(len(page_list)):
        adrs=page_list[i].get_attribute('href')
        python_page_list.append(adrs)
    for i in range(len(python_page_list)):
        print(python_page_list[i])
        return1=follow_gain(python_page_list[i],driver)
        if return1==1:
            print("Exit")
            break







#gui=Tk(className='Instagram Bot')
#gui.geometry("500x200")

root=Tk()
Search_Hashtag=Entry(root)
Search_Entry=Entry(root)
def Expand_Window():
    #print("name")
    Search=Label(root,text="Search").grid(row=2,column=3)
    Search_Entry.grid(row=2,column=4)
    Submit_Search=Button(root,text="Submit Search For Followers",command=Submit_Followers).grid(row=3,column=3)
Insta_Followers = Button(root, text="Instagram Followers",command=Expand_Window)
Insta_Followers.grid(column=0,row=0)
Insta_Delete_Following = Button(root, text="Delete Followings",command=Del_Following)
Insta_Delete_Following.grid(row=1,column=0)
Insta_Follower_HashTag = Button(root, text="Instagram Followers With HashTag",command=Insta_Follower_HashTag)
Insta_Follower_HashTag.grid(column=0,row=2)
Page_Name=Label(root,text="     Username:-   ")
Password=Label(root,text="      Password:-   ")
Page_Name.grid(row=0,column=3)
Password.grid(row=1,column=3)
textEntry=tk.StringVar()
Page_Name_Entry=Entry(root,textvariable = textEntry,state=DISABLED)
textEntry.set("Almaari_pk")
password_entry=tk.StringVar()
Password_Entry=Entry(root,textvariable = password_entry,state=DISABLED)
password_entry.set("14august1947")
Page_Name_Entry.grid(row=0,column=4)
Password_Entry.grid(row=1,column=4)

#gui.mainloop()
root.mainloop()


# In[3]:


#def Submit_Followers():
#    Instagram_Followers(Search_Entry.get(),Page_Name_Entry.get(),Password_Entry.get())
#    
#
##This is Instagram Followers Code without HashTag
#total=0
#def follow_gain(page_name,driver):
#    
#    driver.get(page_name)
#    time.sleep(3)
#    try:
#        followers_list=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
#        followers_list.click()
#        time.sleep(2)
#        follower_pop(driver)
#        return 0
#    except:
#        try:
#            time.sleep(3)
#            Report=driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[1]')
#            Button_Name=Report.get_attribute('innerHTML')
#            if Button_Name=='Report a Problem':
#                print("Report a Problem")
#                return 1
#        except:
#            print("error")
#            return 0
#def follower_pop(driver):
#    count=0
#    global total
#    follower_popup=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
#    for i in range(0,10):
#        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',follower_popup)
#        time.sleep(1)
#    followers_button=driver.find_elements_by_class_name('sqdOP')
#    for i in range(len(followers_button)):
#        name=followers_button[i].get_attribute('innerHTML')
#        if name=='Follow':
#            count=count+1
#            followers_button[i].click()
#            time.sleep(3)
#            total=total+1
#            if count==50:
#                break
#        print(name+"   "+str(total))
#    if count<50:
#        follower_pop()
#def Instagram_Followers(getSearch,getusername,getpassword):
#    python_page_list=[]
#    driver = webdriver.Firefox()  
#    driver.get("https://www.instagram.com/accounts/login/")
#    time.sleep(5)
#    name=driver.find_element_by_name('username')
#    name.send_keys(getusername)
#    time.sleep(2)
#    password=driver.find_element_by_name('password')
#    password.send_keys(getpassword)
#    time.sleep(2)
#    login=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
#    login.click()
#    time.sleep(8)
#    search=driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
#    search.send_keys(getSearch)
#    time.sleep(3)
#    page_list=driver.find_elements_by_class_name('yCE8d')
#    print(len(page_list))
#    for i in range(len(page_list)):
#        adrs=page_list[i].get_attribute('href')
#        python_page_list.append(adrs)
#    for i in range(len(python_page_list)):
#        print(python_page_list[i])
#        return1=follow_gain(python_page_list[i],driver)
#        if return1==1:
#            print("Exit")
#            break


# In[ ]:





# In[ ]:




