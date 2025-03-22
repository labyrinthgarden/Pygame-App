import pygame,sys,random,time

def main():
    pygame.init()
    WIDTH,HEIGHT=500,700
    WI,HE=500,500
    WHITE=(255,255,255)
    win=pygame.display.set_mode((WIDTH,HEIGHT))
    icon=pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    background_image0=pygame.image.load('bg0.jpg')
    background_image0=pygame.transform.scale(background_image0,(WIDTH,HEIGHT))
    background_image1=pygame.image.load('bg1.jpg')
    background_image1=pygame.transform.scale(background_image1,(WIDTH,HEIGHT))
    background_image2=pygame.image.load('bg2.jpg')
    background_image2=pygame.transform.scale(background_image2,(WIDTH,HEIGHT))
    background_imagec=pygame.image.load('bgc.jpg')
    background_imagec=pygame.transform.scale(background_imagec,(WIDTH,HEIGHT))
    font0=pygame.font.Font('DirtyCrown.ttf',25)
    font1=pygame.font.Font('DirtyCrown.ttf',40)
    font2=pygame.font.Font('DirtyCrown.ttf',70)
    text01=font0.render('(PRESIONA "Q" PARA SALIR)',True,WHITE)
    text01_rect=text01.get_rect(center=(WIDTH//2,HEIGHT-60))
    text02=font0.render('(PRESIONA "R" PARA REINICIAR)',True,WHITE)
    text02_rect=text02.get_rect(center=(WIDTH//2,HEIGHT-40))
    text1=font1.render('PRESIONA "J" PARA JUGAR CON OTRO JUGADOR',True,(255,255,255))
    text1_rect=text1.get_rect(center=(WIDTH//2,(HEIGHT//6)*2))
    text12=font1.render('PRESIONA "C" PARA JUGAR CONTRA I.A',True,(255,255,255))
    text12_rect=text12.get_rect(center=(WIDTH//2,(HEIGHT//6)*4))
    x_image=pygame.image.load('x.png')
    o_image=pygame.image.load('o.png')
    si=pygame.mixer.Sound('si.wav')


    def JvJ():
        text2=font2.render('Turno de X',True,WHITE)
        text2_rect=text2.get_rect(center=(WIDTH//2,HEIGHT-110))
        board=[['' for _ in range(3)] for _ in range(3)]    
        player_turn='X'
        winner=None
        game_over=False
        def draw_board():
            for i in range(1,3):
                pygame.draw.line(win,WHITE,(0,i*HE//3),(WI,i*HE//3),3)
                pygame.draw.line(win,WHITE,(i*WI//3,0),(i*WI//3,HE),3)
            for row in range(3):
                for col in range(3):
                    if board[row][col]=='X':
                        draw_x(row,col)
                    elif board[row][col]=='O':
                        draw_o(row,col)
        def draw_x(row,col):
            cell_center_x=col*WI//3+(WI//3)//2
            cell_center_y=row*HE//3+(HE//3)//2
            x_rect=x_image.get_rect(center=(cell_center_x,cell_center_y))
            win.blit(x_image,x_rect)
        def draw_o(row,col):
            cell_center_x=col*WI//3+(WI//3)//2
            cell_center_y=row*HE//3+(HE//3)//2
            o_rect=o_image.get_rect(center=(cell_center_x,cell_center_y))
            win.blit(o_image,o_rect)
        def check_game_over():
            for row in range(3):
                if board[row][0]==board[row][1]==board[row][2]!='':
                    return board[row][0]
            for col in range(3):
                if board[0][col]==board[1][col]==board[2][col]!='':
                    return board[0][col]
            if board[0][0]==board[1][1]==board[2][2]!='':
                return board[0][0]
            if board[0][2]==board[1][1]==board[2][0]!='':
                return board[0][2]
            if all(board[row][col]!='' for row in range(3) for col in range(3)):
                return 'Empate'
            return None
        while not game_over:
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    game_over=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                    elif event.key==pygame.K_r:
                        main()
                try:
                    if winner is None and event.type==pygame.MOUSEBUTTONDOWN:
                        x,y=event.pos
                        col=x//(WI//3)
                        row=y//(HE//3)
                        if board[row][col]=='':
                            board[row][col]=player_turn
                            player_turn='O' if player_turn=='X' else 'X'
                            if player_turn=='X':
                                text2=font2.render('Turno de X',True,(255,255,255))
                            else:
                                text2=font2.render('Turno de O',True,(255,255,255))
                            si.play()
                    winner=check_game_over()
                    if winner=='Empate':
                        text2=font2.render('No hay ganador',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                    elif winner=='X':
                        text2=font2.render('Gana X',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                    elif winner=='O':
                        text2=font2.render('Gana O',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                except:pass
            win.blit(background_image2,(0,0))
            draw_board()
            win.blit(text2,text2_rect)
            win.blit(text01,text01_rect)
            win.blit(text02,text02_rect)
            pygame.display.update()
        pygame.quit()
        sys.exit()


    def M2():
        ch=1
        text1=font1.render('PRESIONA "1" PARA MODO NORMAL',True,(255,255,255))
        text1_rect=text1.get_rect(center=(WIDTH//2,(HEIGHT//6)*2))
        text12=font1.render('PRESIONA "2" PARA MODO SATANAS',True,(255,255,255))
        text12_rect=text12.get_rect(center=(WIDTH//2,(HEIGHT//6)*4))
        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_1:
                        text1=font1.render('PRESIONA "1" PARA MODO NORMAL',True,(255,0,0))
                        win.blit(background_imagec,(0,0))
                        win.blit(text1,text1_rect)
                        si.play()
                        pygame.display.update()
                        time.sleep(.3)
                        JvR()
                    elif event.key==pygame.K_2:
                        text12=font1.render('PRESIONA "2" PARA MODO SATANAS',True,(255,0,0))
                        if ch==1:
                            bgis=pygame.image.load('bgs2.jpg')
                        else:
                            bgis=pygame.image.load('bgs.jpg')
                        bgis=pygame.transform.scale(bgis,(WIDTH,HEIGHT))
                        win.blit(bgis,(0,0))
                        win.blit(text12,text12_rect)
                        pygame.display.update()
                        si.play()
                        time.sleep(.5)
                        JvS()
            win.blit(text1,text1_rect)
            win.blit(text12,text12_rect)
            pygame.display.update()
            win.blit(background_image1,(0,0))


    def JvR():
        text2=font2.render('Turno del Jugador (X)',True,WHITE)
        text2_rect=text2.get_rect(center=(WIDTH//2,HEIGHT-110))
        board=[['' for _ in range(3)] for _ in range(3)]
        player_turn='X'
        winner=None
        game_over=False
        def draw_board():
            for i in range(1,3):
                pygame.draw.line(win,WHITE,(0,i*HE//3),(WI,i*HE//3),3)
                pygame.draw.line(win,WHITE,(i*WI//3,0),(i*WI//3,HE),3)
            for row in range(3):
                for col in range(3):
                    if board[row][col]=='X':
                        draw_x(row,col)
                    elif board[row][col]=='O':
                        draw_o(row,col)
        def draw_x(row,col):
            cell_center_x=col*WI//3+(WI//3)//2
            cell_center_y=row*HE//3+(HE//3)//2
            x_rect=x_image.get_rect(center=(cell_center_x,cell_center_y))
            win.blit(x_image,x_rect)
        def draw_o(row,col):
            cell_center_x=col*WI//3+(WI//3)//2
            cell_center_y=row*HE//3+(HE//3)//2
            o_rect=o_image.get_rect(center=(cell_center_x,cell_center_y))
            win.blit(o_image,o_rect)
        def check_game_over():
            for row in range(3):
                if board[row][0]==board[row][1]==board[row][2]!='':
                    return board[row][0]
            for col in range(3):
                if board[0][col]==board[1][col]==board[2][col]!='':
                    return board[0][col]
            if board[0][0]==board[1][1]==board[2][2]!='':
                return board[0][0]
            if board[0][2]==board[1][1]==board[2][0]!='':
                return board[0][2]
            if all(board[row][col]!='' for row in range(3) for col in range(3)):
                return 'Empate'
            return None
        while not game_over:
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    game_over=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                    if event.key==pygame.K_r:
                        main()
                try:
                    if winner is None:
                        if player_turn=='X' and event.type==pygame.MOUSEBUTTONDOWN:
                            x,y=event.pos
                            col=x//(WI//3)
                            row=y//(HE//3)
                            if board[row][col]=='':
                                board[row][col]=player_turn
                                player_turn='O'
                                si.play()
                            winner=check_game_over()
                        if player_turn=='O' and winner==None:
                            m=[]
                            m1=[]
                            for x in range(3):
                                for y in range(3):
                                    if board[x][y]=='':
                                        m.append(x)
                                        m1.append(y)
                            rr=random.randint(0,len(m))
                            board[m[rr]][m1[rr]]='O'
                            player_turn='X'
                            si.play()
                            winner=check_game_over()
                    if winner=='Empate':
                        text2=font2.render('No hay ganador',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                    elif winner=='X':
                        text2=font2.render('Gana X',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                    elif winner=='O':
                        text2=font2.render('Gana O',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                except:pass
            win.blit(background_image2,(0,0))
            draw_board()
            win.blit(text2,text2_rect)
            win.blit(text01,text01_rect)
            win.blit(text02,text02_rect)
            pygame.display.update()
        pygame.quit()
        sys.exit()


    def JvS():
        text2=font2.render('Turno del Jugador (X)',True,WHITE)
        text2_rect=text2.get_rect(center=(WIDTH//2,HEIGHT-110))
        board=[['' for _ in range(3)] for _ in range(3)]
        player_turn='X'
        winner=None
        game_over=False
        def draw_board():
            for i in range(1,3):
                pygame.draw.line(win,WHITE,(0,i*HE//3),(WI,i*HE//3),3)
                pygame.draw.line(win,WHITE,(i*WI//3,0),(i*WI//3,HE),3)
            for row in range(3):
                for col in range(3):
                    if board[row][col]=='X':
                        draw_x(row,col)
                    elif board[row][col]=='O':
                        draw_o(row,col)
        def draw_x(row,col):
            cell_center_x=col*WI//3+(WI//3)//2
            cell_center_y=row*HE//3+(HE//3)//2
            x_rect=x_image.get_rect(center=(cell_center_x,cell_center_y))
            win.blit(x_image,x_rect)
        def draw_o(row,col):
            cell_center_x=col*WI//3+(WI//3)//2
            cell_center_y=row*HE//3+(HE//3)//2
            o_rect=o_image.get_rect(center=(cell_center_x,cell_center_y))
            win.blit(o_image,o_rect)
        def check_game_over():
            for row in range(3):
                if board[row][0]==board[row][1]==board[row][2]!='':
                    return board[row][0]
            for col in range(3):
                if board[0][col]==board[1][col]==board[2][col]!='':
                    return board[0][col]
            if board[0][0]==board[1][1]==board[2][2]!='':
                return board[0][0]
            if board[0][2]==board[1][1]==board[2][0]!='':
                return board[0][2]
            if all(board[row][col]!='' for row in range(3) for col in range(3)):
                return 'Empate'
            return None
        def minimax(board,depth,is_maximizing):
            if check_game_over()=='X':
                return -1
            if check_game_over()=='O':
                return 1
            if check_game_over()=='Empate':
                return 0
            if is_maximizing:
                best_score=-float('inf')
                for row in range(3):
                    for col in range(3):
                        if board[row][col]=='':
                            board[row][col]='O'
                            score=minimax(board,depth+1,False)
                            board[row][col]=''
                            best_score=max(score, best_score)
                return best_score
            else:
                best_score=float('inf')
                for row in range(3):
                    for col in range(3):
                        if board[row][col]=='':
                            board[row][col]='X'
                            score=minimax(board,depth+1,True)
                            board[row][col]=''
                            best_score=min(score,best_score)
                return best_score
        def best_move(board):
            best_score=-float('inf')
            best_move=None
            for row in range(3):
                for col in range(3):
                    if board[row][col]=='':
                        board[row][col]='O'
                        score=minimax(board,0,False)
                        board[row][col]=''
                        if score>best_score:
                            best_score=score
                            best_move=(row,col)
            return best_move
        while not game_over:
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    game_over=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                    elif event.key==pygame.K_r:
                        main()
                try:
                    if winner is None:
                        if player_turn=='X' and event.type==pygame.MOUSEBUTTONDOWN:
                            x,y=event.pos
                            col=x//(WI//3)
                            row=y//(HE//3)
                            if board[row][col]=='':
                                board[row][col]=player_turn
                                player_turn='O'
                                si.play()
                            winner=check_game_over()
                        if player_turn=='O' and winner==None:
                            row,col=best_move(board)
                            board[row][col]=player_turn
                            player_turn='X'
                            si.play()
                            winner=check_game_over()
                    if winner=='Empate':
                        text2=font2.render('No hay ganador',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                    elif winner=='X':
                        text2=font2.render('Gana X',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                    elif winner=='O':
                        text2=font2.render('Gana O',True,(255,255,255))
                        text2_rect=text2.get_rect()
                        text2_rect.center=(WIDTH//2,HEIGHT-110)
                except:pass
            win.blit(background_image2,(0,0))
            draw_board()
            win.blit(text2,text2_rect)
            win.blit(text01,text01_rect)
            win.blit(text02,text02_rect)
            pygame.display.update()
        pygame.quit()
        sys.exit()


    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_j:
                    text1=font1.render('PRESIONA "J" PARA JUGAR CON OTRO JUGADOR',True,(255,255,0))
                    win.blit(background_imagec,(0,0))
                    win.blit(text1,text1_rect)
                    pygame.display.update()
                    si.play()
                    time.sleep(.3)
                    JvJ()
                elif event.key==pygame.K_c:
                    text12=font1.render('PRESIONA "C" PARA JUGAR CONTRA I.A',True,(255,255,0))
                    win.blit(background_imagec,(0,0))
                    win.blit(text12,text12_rect)
                    pygame.display.update()
                    si.play()
                    time.sleep(.3)
                    M2()
        win.blit(text1,text1_rect)
        win.blit(text12,text12_rect)
        pygame.display.update()
        win.blit(background_image0,(0,0))
main()