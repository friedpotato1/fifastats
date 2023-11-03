try:
  while True:
   
   winner = str(input('Which player won > '))
   winner = winner.lower()
   wins = {}
   with open('winners.txt','a') as win:
      win.write(f'{winner}\n')
   with open ('winners.txt', 'r') as f:
      for stat in f:
        stat = stat.strip()
        wins.setdefault(stat,0)
        wins[stat] = wins[stat] + 1
   response = str(input('\nWould u like to see detailed stats (yes or no) : > \n'))
   response = response.lower()
   if response == 'yes' :
        print('\n',"Here are the detailed wins stats :\n")
        print('\t',wins)
except KeyboardInterrupt:
    print('\n\n\tQuiting...')
