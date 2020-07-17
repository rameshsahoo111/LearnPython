#!/bin/python3
#Author: Ramesh Sahoo
#Date: 2020-07-17
#Purpose: Tic Tac Toe Game - Play command line


from random import randint

## Master Box
master_box_loc = [1,2,3,4,5,6,7,8,9]

## Player1 & Player2 Selection sets
p1_sel_set = set()
p2_sel_set = set()

## Win sceniario dict sets
win_dict = {
'win_cn1':{1,5,9},
'win_cn2':{7,5,3},
'win_r1':{1,2,3},
'win_r2':{4,5,6},
'win_r3':{7,8,9},
'win_c1':{3,6,9},
'win_c2':{2,5,8},
'win_c3':{1,4,7}
}

## Required Styles
S1 = "="
S2 = "|"
S3 = ' '
S4 = '  '

## Tic Tac Toe Box
dummy_box = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

## Dummy Board
def dummy_tic_tac_toe():
  print(S3*8+S2+S3*3+S2)
  print(S3*6+'1'+S3+S2+' 2'+S3*1+S2+' 3')
  print(S1*8+S2+S1*3+S2+S1*8)
  print(S3*6+'4'+S3+S2+' 5'+S3*1+S2+' 6')
  print(S1*8+S2+S1*3+S2+S1*8)
  print(S3*6+'7'+S3+S2+' 8'+S3*1+S2+' 9')
  print(S3*8+S2+S3*3+S2)
  print("\n\n")

  print(S3*8+S2+S3*3+S2)
  print(S3*6+'O'+S3+S2+' O'+S3*1+S2+' X')
  print(S1*8+S2+S1*3+S2+S1*8)
  print(S3*6+'X'+S3+S2+' X'+S3*1+S2+' O')
  print(S1*8+S2+S1*3+S2+S1*8)
  print(S3*6+'X'+S3+S2+' O'+S3*1+S2+' X')
  print(S3*8+S2+S3*3+S2)
  print("\n")

## Actual Board
def tic_tac_toe():
  print(S3*8+S2+S3*3+S2)
  print(S3*6+str(dummy_box['1'])+S3+S2+S3+str(dummy_box['2'])+S3+S2+S3+str(dummy_box['3']))
  print(S1*8+S2+S1*3+S2+S1*8)
  print(S3*6+str(dummy_box['4'])+S3+S2+S3+str(dummy_box['5'])+S3+S2+S3+str(dummy_box['6']))
  print(S1*8+S2+S1*3+S2+S1*8)
  print(S3*6+str(dummy_box['7'])+S3+S2+S3+str(dummy_box['8'])+S3+S2+S3+str(dummy_box['9']))
  print(S3*8+S2+S3*3+S2)
  print("\n")

print('\nWelcome to the tic Tac Toe - Terminal Game!!')
print("Sample Tic Tac Toe Board looks like:\n")
dummy_tic_tac_toe()

print('\nSymbol of Player 1: O and Symbol of Player 2: X\n\nHere you are player 1 and the computer is Player 2\n')


## Select Winners
def select_winners(win_dict,p1_sel_set,p2_sel_set):
  for i in win_dict:
    if win_dict[i].issubset(p1_sel_set):
       return f'Player P1 is winner!!\n'
       #return f'Player P1 is winner!! selection:{p1_sel_set}\n'
    elif win_dict[i].issubset(p2_sel_set):
      return f'Player P2 is winner!!\n'
      #return f'Player P2 is winner!! selection:{p2_sel_set}\n'
          
  #return f'No winner found! selection P1:{p1_sel_set} selection P2:{p2_sel_set}'
  return 'Tie - No winner found!\n'


## Fill boards 
def fill_board():

  # Player 1 inputs
  while master_box_loc != []:
    P1 = int(input("P1: Enter a num: "))    

    if P1 in master_box_loc:
      master_box_loc.pop(master_box_loc.index(P1))
      p1_sel_set.add(P1)
      dummy_box[str(P1)] = 'O'
      #print("\n\nP1 Move looks:")
      #print('\n')
      #tic_tac_toe()
      flag = 0
      
      winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
      if 'P1' in winner:
          return winner

      # Player 2 Logic
      while flag != 1 and master_box_loc != []:
          if 1 in p1_sel_set and 7 in p1_sel_set and 4 in master_box_loc:
              P2 = 4
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                  print('\n')
                  tic_tac_toe()
                  return winner

          elif 1 in p1_sel_set and 4 in p1_sel_set and 7 in master_box_loc:
              P2 = 7
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                print('\n')
                tic_tac_toe()
                return winner

          elif 2 in p1_sel_set and 3 in p1_sel_set and 1 in master_box_loc:
              P2 = 1
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                print('\n')
                tic_tac_toe()
                return winner

          elif 7 in p1_sel_set and 4 in p1_sel_set and 1 in master_box_loc:
              P2 = 1
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                print('\n')
                tic_tac_toe()
                return winner
                
          elif 1 in p1_sel_set and 3 in p1_sel_set and 2 in master_box_loc:
              P2 = 2
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                  print('\n')
                  tic_tac_toe()
                  return winner

          elif 1 in p1_sel_set and 5 in p1_sel_set and 2 in p1_sel_set and 3 in master_box_loc:
              P2 = 3
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                print('\n')
                tic_tac_toe()
                return winner

          elif 8 in p1_sel_set and 2 in p1_sel_set and 5 in master_box_loc:
              P2 = 5
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                  print('\n')
                  tic_tac_toe()
                  return winner

          elif P1 == 1 and P1 not in master_box_loc and 9 in master_box_loc:
              P2 = 9
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                  print('\n')
                  tic_tac_toe()
                  return winner

          elif P1 == 9 and P1 not in master_box_loc and 1 in master_box_loc:
              P2 = 1
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                print('\n')
                tic_tac_toe()
                return winner
          
          elif P1 == 7 and P1 not in master_box_loc and 3 in master_box_loc:
              P2 = 3
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                print('\n')
                tic_tac_toe()
                return winner

          elif P1 == 3 and P1 not in master_box_loc and 7 in master_box_loc:
              P2 = 7
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
               print('\n')
               tic_tac_toe()
               return winner

          elif 1 in p1_sel_set and 2 in p1_sel_set and 3 in master_box_loc:
              P2 = 3
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                print('\n')
                tic_tac_toe()
                return winner
        
          elif 2 in p1_sel_set and 5 in p1_sel_set and 8 in master_box_loc:
              P2 = 8
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                  print('\n')
                  tic_tac_toe()
                  return winner
  
          elif 1 in p1_sel_set and 2 in p1_sel_set and 5 in p1_sel_set and 8 in master_box_loc:
              P2 = 8
              master_box_loc.pop(master_box_loc.index(P2))
              p2_sel_set.add(P2)
              dummy_box[str(P2)] = 'X'
              #print("\n\nP2 Move looks:")
              print('\n')
              tic_tac_toe()
              print('\n')
              flag += 1

              winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
              if 'P2' in winner:
                  print('\n')
                  tic_tac_toe()
                  return winner

          elif master_box_loc  != []:
              P2 = randint(1,9)
              if P2 in master_box_loc:
                master_box_loc.pop(master_box_loc.index(P2))
                p2_sel_set.add(P2)
                dummy_box[str(P2)] = 'X'
                #print("\n\nP2 Move looks:")
                print('\n')
                tic_tac_toe()
                print('\n')
                flag += 1

                winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
                if 'P2' in winner:
                    print('\n')
                    tic_tac_toe()
                    return winner

          elif master_box_loc  == []:
                flag += 1        
          else:
            flag = 0

    else:
      if P1 > 9 or P1 <= 0:
        print(f'Out of Range {P1}')
      else:
        print(f"{P1} already selected\n")

  return winner  
  

winner = fill_board()
#winner = select_winners(win_dict,p1_sel_set,p2_sel_set)
print('\n')
tic_tac_toe()
print(winner)
