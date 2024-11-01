#LFIO = Last In - First Out


#example on what happens as you are in a web browser and hit the back buttom to go to prior pages
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

last = browsing_session.pop()
print(last)
print("redirect", browsing_session[-1])

browsing_session.clear() #setting the browsing_session[] to empty, simulate going back to openiing page

if not browsing_session:
    print("disable back button")