####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E3'
strategy_name = 'Remember betrayal'
strategy_description = '''Betray if betrayed more than once in the past five rounds.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' # otherwise collude.
    '''
    recent_betrayal_count = 0
    if len(my_history) <= 5:
      return 'c'
    else:
      for i in range(1, 6):
        if 'b' in their_history[-i]:
          recent_betrayal_count += 1  
      if recent_betrayal_count >= 2:
        return 'b'
      else:
        return 'c'