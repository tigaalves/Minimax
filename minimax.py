playerTurn = True

def JogoDaVelha():
  tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]

  def getE(i, type):
    if(type == 0):
      if(tabuleiro[i] == "X" or tabuleiro[i] == "O"):
        return(tabuleiro[i])
      else:
        return(" ")

    if(type == 1):
      if(tabuleiro[i] == "X" or tabuleiro[i] == "O"):
        return("-")
      else:
        return(tabuleiro[i])

  def PrintarTabuleiro():
    print("")
    print("", getE(0, 0), "|", getE(1, 0), "|", getE(2, 0), "      ", getE(0, 1), "|", getE(1, 1), "|", getE(2, 1))
    print("---|---|---", "    ", "---|---|---")
    print("", getE(3, 0), "|", getE(4, 0), "|", getE(5, 0), "      ", getE(3, 1), "|", getE(4, 1), "|", getE(5, 1))
    print("---|---|---", "    ", "---|---|---")
    print("", getE(6, 0), "|", getE(7, 0), "|", getE(8, 0), "      ", getE(6, 1), "|", getE(7, 1), "|", getE(8, 1))
    print("")
  

  def GetNumber(player):
    while True:
      number = input("Choose a box for " + player + ": ")
      try:
        number = int(number)

        if number in range(1, 10):
          return number
        
        else:
          print("Digite um número válido! -_-")
        
      except ValueError:
        print("Eu preciso de um número! :|")
        continue

  def CheckarVencedor(thistabuleiro):
    count = 0

    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if thistabuleiro[x] == "X" and thistabuleiro[y] == "X" and thistabuleiro[z] == "X":
              if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                return 1

            if thistabuleiro[x] == "O" and thistabuleiro[y] == "O" and thistabuleiro[z] == "O":
              if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                return -1

    for v in range(9):
      if(thistabuleiro[v] == "X" or thistabuleiro[v] == "O"):
        count += 1

    if(count == 9):
      return 0
    return 5
  
  def Turn(player):
    n = GetNumber(player)
    if(tabuleiro[n-1] == "X" or tabuleiro[n-1] == "O"):
      print("Esse espaço está ocupado. Tente outro.")
      Turn(player)
    else:
      tabuleiro[n-1] = player


  def miniMax(current, depth, isMaximizing):
    rVal = 0
    newB = current[:]

    score = CheckarVencedor(newB)

    if(depth == 0):
      if(score == 5): 
        return 0

      return score
    
    if(score != 5):
      return score

    if(isMaximizing):
      minVal = -10
      for i in range(9):
        if(newB[i] != "X" and newB[i] != "O"):
          newB[i] = "X"
          rVal = miniMax(newB, depth-1, not isMaximizing)
          if(rVal > minVal):
            minVal = rVal
          newB[i] = i+1
      return minVal

    if(not isMaximizing):
      maxVal = 10
      for i in range(9):
        if(newB[i] != "X" and newB[i] != "O"):
          newB[i] = "O"
          rVal = miniMax(newB, depth-1, not isMaximizing)
          if(rVal < maxVal):
            maxVal = rVal
          newB[i] = i+1
      return maxVal


  
  def AITurn():
    newB = tabuleiro[:]

    winBox = 0

    minVal = -10
    print("Boa jogada, pensando......")
    for i in range(9):
      if(newB[i] != "X" and newB[i] != "O"):
        newB[i] = "X"
        receivedVal = miniMax(newB, 6, False)

        if(receivedVal > minVal):
          minVal = receivedVal
          winBox = i
        newB[i] = i+1
        

    
    tabuleiro[winBox] = "X"



  end = 5
  playerX = not playerTurn

  while end == 5:
    end = CheckarVencedor(tabuleiro)
    
    PrintarTabuleiro()
    
    if(end == -1):
      print("Parabéns! Jogador \'O\' ganhou")
    elif (end == 1):
      print("Parabéns! Jogador \'X\' ganhou")
    elif (end == 0):
      print("O jogo acabou em empate!")

    if(end == 5):
      if(playerX):
        AITurn()
      else:
        Turn("O")
      
      playerX = not playerX




while True:
  JogoDaVelha()
  inp = input("Jogar Novamente? Y/N: ")
  if (inp.lower() == "y"):
    print("Vamos jogar novamente!\n")
    playerTurn = not playerTurn
  else:
    break