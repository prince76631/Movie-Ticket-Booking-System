import random, string
# ********************************************************************************************

class Show:
    def __init__(self, show_name, duration):
        self.show_name = show_name
        self.duration  = duration

    def movie_details(self):
        return f'\nMovie = {self.show_name}\nDuration = {self.duration}'

    def play_details(self):
        return f'\nPlay = {self.show_name}\nDuration = {self.duration}'

    def concert_details(self):
        return f'\nConcert = {self.show_name}\nDuration = {self.duration}'


movie_data   = {'Avengers', 'Bahubali', 'Kgf', 'Pathaan', 'Animal', 'Jawan', 'Freedy', 'Holiday', 'Wanted'}
play_data    = {'Ashwamedh', 'Bahurupi', 'Loha Singh (play)', 'Bharat', 'Independence-day', 'Republic-day'}
concert_data = {'Fest-1', 'Fest-2', 'Fest-3', 'Fest-4', 'Fest-5', 'Fest-6', 'Fest-7', 'Fest-8', 'Fest-9'}

theater_data_1 = {'Luxe Cinemas' : 200, 'AMB Cinemas'   : 300, 'Sathyam Cinemas': 400}
theater_data_2 = {'PVR Cinemas'  : 200, 'Cinépolis'     : 300, 'INOX Movies'    : 400}
theater_data_3 = {'Regal Theatre': 200, 'Urvashi Cinema': 300, 'Globe Theatre'  : 400}

# ********************************************************************************************


class Theater:
    def __init__(self, name, location, capacity, price):
        self.name     = name
        self.location = location
        self.capacity = capacity
        self.price    = price

    def theater_details(self):
        return f'\nTheater_Name = {self.name}\nLocation = {self.location}\nCapacity = {self.capacity}\nPrice = {self.price}'

# ********************************************************************************************



class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def customer_details(self):
        return f'\nCustomer name : {self.name} \nCustomer mail : {self.email}'


# ********************************************************************************************


class Ticket:
    def __init__(self, ticket_id, show_name, c_name, seat_res, amount):
        self.ticket_id = ticket_id
        self.show_name = show_name
        self.c_name = c_name
        self.seat_res = seat_res
        self.amount = amount


    def gen_ticket(self):
        return f'\nTicket_id : {self.ticket_id}\nShow_name : {self.show_name}\nCustomer_name : {self.c_name}\nSeat_number : {self.seat_res}\nPrice : {self.amount}\n'

# ********************************************************************************************


while True:
    print('\nPlease select your interest (by name : )')
    print('\n1.MOVIE\n2.Play\n3.Concert')
    choice = input('\nEnter Your Choice (or q to exit) : ').lower().strip().lstrip()
    if choice == 'q':
        break

    if choice == 'movie':
        while True:
            print('\nPlease select your movie : ')
            print('\n', movie_data)
            movie_name = input("\nEnter Movie Name : ").capitalize().strip().lstrip()
            if movie_name in movie_data:
                movie = Show(movie_name, '3 hours')
                print(movie.movie_details())
                break
            else:
                print("\nSorry ",movie_name,choice, " is not available... ")

            
    elif choice == 'concert':
        while True:
            print('\nPlease select your concert : ')
            print('\n', concert_data)
            concert_name = input('\nEnter Concert Name : ').capitalize().strip().lstrip()
            if concert_name in concert_data:
                concert = Show(concert_name, '2 hours')
                print(concert.concert_details())
                break
            else:
                print("\nSorry ",concert_name,choice, " not available... ")
            

    elif choice == 'play':
        while True:
            print('\nPlease select your play : ')
            print('\n', play_data)
            play_name = input('\nEnter Play Name : ').capitalize().strip().lstrip()
            if play_name in play_data:
                play = Show(play_name, '1 hours')
                print(play.play_details())
                break
            else:
                print("\nSorry ",play_name,choice, " not available... ")
            

    else:
        print('\nWrong selection... ')
        continue
   
# ********************************************************************************************


    while True:
        print('\nAvailable areas to watch:', choice.upper())
        print('\nArea pincode\n 1. 110045\n 2. 110046\n 3. 110047\n')
        
        pincode = input("\nEnter Area Pincode (by 1, 2, 3) : ").strip().lstrip()

        if pincode =='1' or pincode=='2' or pincode =='3':
          if pincode == '1':
            print("\nThere you can check out the theaters : ")
            print(theater_data_1)
            theater_name = input('\nEnter Theater Name : ').strip().lstrip()

            if theater_name in theater_data_1:
                theater = Theater(theater_name, 'Karol-Bagh', 800, theater_data_1[theater_name])
                print('\n', theater.theater_details())
                break

            else:
                print('\nNot available ..! ')

          elif pincode == '2':
            print("\nThere you can check out the theaters : ")
            print(theater_data_2)
            theater_name = input('\nEnter Theater Name : ').strip().lstrip()

            if theater_name in theater_data_2:
                theater = Theater(theater_name, 'Saket', 200, theater_data_2[theater_name])
                print('\n', theater.theater_details())
                break

            else:
                print('\nNot available ..! ')

          elif pincode == '3':
            print("\nThere you can check out the theaters : ")
            print(theater_data_3)
            theater_name = input('\nEnter Theater Name : ').strip().lstrip()

            if theater_name in theater_data_3:
                theater = Theater(theater_name, 'Sarita-Vihar',500, theater_data_3[theater_name])
                print('\n', theater.theater_details())
                break

            else:
                print('\nNot available ..! ')

        else:
            print('\nWrong selection ..! ')
            continue

# ********************************************************************************************

    while True:
       print('\nCustomer Options:')
       print('\n1. New customer\n2. Regular Customer (flat 30% off)')

       customer_type = input('\nEnter option number : ').strip().lstrip()
    


       if customer_type == '1':
            customer_name = input('\nEnter Your Name : ')
            customer_mail = input('\nEnter Your Mail ID : ')
            if customer_name.replace(" ", "").isalpha() and customer_mail.isalnum():
                customer = Customer(customer_name, customer_mail)
                print(customer.customer_details())
                
            else:
               print('! Invalid customer information ...')
               continue
               
# ********************************************************************************************


       elif customer_type == '2':
            customer_id = input('\nEnter Your Customer ID : ')
            if customer_id == '123':
               customer_name = input('\nEnter Your Name : ')
               customer_mail = input('\nEnter Your Mail ID : ')
               if customer_name.replace(" ", "").isalpha() and customer_mail.isalnum():
                  customer = Customer(customer_name, customer_mail)
                  theater.price -=  (theater.price * 30/100)
                  print(customer.customer_details())
                

               else:
                   print('! Invalid customer information ...')
                   continue
              
              
            else:
              print('Something went wrong....')
              continue


       else:
            print('Invalid Option')
            continue
        
# ********************************************************************************************
         
       seat = int(input('\nHow many seats do you want to book : '))

# ********************************************************************************************

       while True:
        print('\nUpdate setting\n1. Yes\n2. No ')
        update = input('\nPress (1 or 2) : ')

        if update == '1':
            print('\nWhat do you want to update')
            print('\n1. movie_name\n2. concert_name\n3. play_name\n4. Theater\n5. Customer_Name\n6. Seat\n7. Exit ')
# ********************************************************************************************

            option = input('\nEnter option number : ')

            if option == '1':
                if choice == 'movie':
                   print(movie_data)
                   m_name = input('\nEnter movie name :').capitalize().strip().lstrip()
                   if m_name in movie_data:
                      movie_name = m_name
                      print('\nMovie name updated ..')

                   else:
                      print('\n',m_name,' not found')
                      continue
                else:
                    print('\nYou have not selected for movie earlier : ')  
                    continue 
# ********************************************************************************************
           

            elif option == '2':
                 if choice == 'concert':
                    print(concert_data)
                    c_name = input('\nEnter concert name :').capitalize().strip().lstrip()
                    if c_name in concert_data:
                       concert_name = c_name
                       print('\nConcert name updated ..')

                    else:
                       print('\n',c_name,'not found..') 
                       continue 
                 else:  
                     print('\nYou have not selected for concert earlier : ')
                     continue  

# ********************************************************************************************


            elif option == '3':
                 if choice == 'play':
                    print(play_data)
                    p_name = input('\nEnter play name :').capitalize().strip().lstrip()
                    if p_name in play_data:
                       play_name = p_name
                       print('\nPlay name updated .. ')

                    else:
                       print('\n',p_name,' not found')
                       continue 
                 else:
                     print('\nYou have not selected for play earlier : ')
                     continue  
                   
# ********************************************************************************************



            elif option == '4':
                 print('\nArea pincode\n 1. 110045\n 2. 110046\n 3. 110047\n')
                 pin = input('\nEnter your pincode : ')

                 if pin == '1':
                    print(theater_data_1)
                    t_name = input('\nEnter theater name : ').strip().lstrip()

                    if t_name in theater_data_1:
                       theater_name = t_name 
                       print('\ntheater name updated .. ') 

                    else:
                       print('\n',t_name,'unavailable .. ')
                       continue   

                 elif pin == '2':
                      print(theater_data_2)
                      t_name = input('\nEnter theater name : ').strip().lstrip()

                      if t_name in theater_data_2:
                         theater_name = t_name
                         print('\ntheater name updated .. ') 

                      else:
                         print('\n',t_name,'unavailable .. ')
                         continue  
                      
                 elif pin == '3':
                      print(theater_data_3)
                      t_name = input('\nEnter theater name : ').strip().lstrip()

                      if t_name in theater_data_3:
                         theater_name = t_name  
                         print('\ntheater name updated .. ')

                      else:
                         print('\n',t_name,'unavailable .. ')
                         continue 

 # ********************************************************************************************
                
            elif option == '5':
                 new_name = input('\nEnter new name : ')

                 if new_name.replace(" ", "").isalpha():
                    customer_name = new_name
                    print('\nCustomer name updated .. ')

                 else:
                    print('\nWrong name ')  
                    continue 

# ********************************************************************************************

            elif option == '6':
                 seat_resv = int(input('\nHow much seat do you reserve : '))

                 if seat_resv > 0 and seat_resv != "":
                  seat = seat_resv
                  print('\nSeat updated .. ')

                 else:
                    print('\nInvalid seat reservation .. ')
                    continue
                
# ********************************************************************************************
                   
            elif option == '7':
                break     

# ********************************************************************************************

            else:
                print('\nWrong selection ... ') 
                continue 

# ********************************************************************************************
                

        elif update == '2':
            break

# ********************************************************************************************

       
        else:
           print('\nWrong selection ...')
           continue

        
    
# ********************************************************************************************


       if seat > 0 and seat != '':
        
          character = string.ascii_uppercase + string.digits
          t_id = (''.join(random.choice(character) for _ in range(8)))
          random_number = [random.randint(1, theater.capacity) for _ in range(seat)]

# ********************************************************************************************

          if choice == 'movie':
               ticket = Ticket(t_id, movie_name, customer_name, random_number, theater.price*seat)
               print('\n****Ticket****')
               print(ticket.gen_ticket())
               print('****Successfully****')
               break
          
# ********************************************************************************************

          elif choice == 'concert':
                 ticket = Ticket(t_id, concert_name, customer_name, random_number, theater.price*seat)
                 print('\n****Ticket****')
                 print(ticket.gen_ticket())
                 print('****Successfully****')
                 break

# ********************************************************************************************

          elif choice == 'play':
                 ticket = Ticket(t_id, play_name, customer_name, random_number, theater.price*seat)
                 print('\n****Ticket****')
                 print(ticket.gen_ticket())
                 print('****Successfully****')
                 break
          
# ********************************************************************************************

       
       else:
           print('! Something went wrong while choosing seat..')
           continue
       
       
      
     



