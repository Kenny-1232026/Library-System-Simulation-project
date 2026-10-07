
def main_menu():
           x= input("Visit library (Yes/No): ").strip().capitalize()
           if x== ("Yes"):
                print("Main menu:")
                print('View all Books')
                print('Search book')
                print('Add book')
                print('Borrow book')
                print('View borrowed book')
                print('Returned book')
                print("Exit")
                y= input("Pick a menu: ").strip().capitalize()
                if y== "Add book":
                  l= input("What book do you want to add?: ")
                  def add_book():
                         curb= [['C2 closure', 'C3 closure'],['Tapda', 'TTFM', 'MMXM'], ['Time cycles', 'Candle science']]
                         borrowed= ['python', '33h7', 'lhs22', 'CS\'50']
                         for k in curb:
                               for h in k:
                                     if h == l:
                                         print('Book already in library')
                                         break
                               else:
                                     continue
                               break
                         else:
                                curb.insert(0,l)
                                print('Book added successfully')
                                print(curb) 
                  add_book()
                elif y== 'View all books':
                      print('Available books')
                      print('Borrowed books')
                      l= input("Available/Borrowed books?: ").strip().capitalize()
                      if l== "Available books":
                            print('C2 closure')
                            print('C3 closure')
                            print('Tapda')
                            print('TTFM')
                            print('MMXM')
                            print('Time cycles')
                            print('Candle science')
                      elif l== "Borrowed books":
                            print('Python')
                            print('33h7')
                            print('lhs22')
                            print('CS\'50')
                      else:
                            print("Could not process your response.")
                elif y== 'Search book' or y=='Borrow book':
                       def search_book():
                           l= input("Enter book name?: ")
                           curb= [['C2 closure', 'C3 closure'],['Tapda', 'TTFM', 'MMXM'], ['Time cycles', 'Candle science']]
                           borrowed= ['python', '33h7', 'lhs22', 'CS\'50']
                           for k in curb:
                                 for h in k:
                                       if h== l:
                                             print('Book is available.')
                                             m= input("Do you want to borrow this book?: ").strip().capitalize()
                                             if m== "Yes":
                                                   print('Congratulations your application for', l, 'was successful')
                                                   print('Visit our nearest branch with code:', l[0],26,l[2],l[3],7,)
                                                   for w in curb:
                                                          if l in w:
                                                                 w.remove(l)
                                                                 print('Currently available books', curb)
                                                          break
                                                   else:
                                                          print('Done')
                                             else:
                                                    print('Which book do you like?')
                                                    search_book()
                                             break
                                 else:
                                       continue
                                 break
                           else:
                               for j in borrowed:
                                       if j== l:
                                             print('Currently borrowed')
                                             break
                               else:
                                        print('This book is not available')
                       search_book()
                elif y== 'Return book':
                                        l= input("Enter book name: ")
                                        def return_book():
                                               curb= [['C2 closure', 'C3 closure'],['Tapda', 'TTFM', 'MMXM'], ['Time cycles', 'Candle science']]
                                               borrowed= ['python', '33h7', 'lhs22', 'CS\'50']
                                               for k in borrowed:
                                                      if k== l:
                                                             print("Thanks for using our library")
                                                             print("Visit our nearest branch with code:", 'R',l[1],26,l[0])
                                                             break
                                               else:
                                                     print('Book was not borrowed from this library.')
                                        return_book() 
                elif y== 'Exit':
                                        l= input("Do you really want to Exit?: ").strip().capitalize() 
                                        if l== 'Yes':
                                               print('Thanks for exploring our library')
                                        else:
                                               main_menu()
                else:
                       print('Invalid response.')
           else:
                  print('If you\'re ever interested in any book, make sure to visit our library.' )
                  print('Thank you')
main_menu() 

                       

  

